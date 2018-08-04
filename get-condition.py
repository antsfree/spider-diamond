#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, Comment
import re
from function import request_html
import os
from json import dumps
import pymysql
from config import *


def condition():
    """
    获取钻石查询参数及对应值
    :return:
    """
    html = request_html(DIAMOND_URL)
    soup = BeautifulSoup(html, 'html.parser')
    # 过滤注释代码
    comments = soup.findAll(text=lambda text: isinstance(text, Comment))
    [comment.extract() for comment in comments]
    # list
    elements = soup.find('div', {'id': 'searchBgMore'}).children
    attr_map = []
    text = ''
    # 过滤空行
    elements = filter(filter_line_break, elements)
    for element in elements:
        children = filter(filter_line_break, element.children)
        for child in children:
            try:
                if child['class'][0]:
                    class_name = child['class'][0]
                    # 匹配中文说明
                    match_name = re.match(r'search(.*)Img', class_name)
                    if match_name:
                        text = child.get_text()
                    # 匹配数组 key 和 value 值
                    match_mark = re.match(r'search(.*)Name', class_name)
                    if match_mark:
                        # 获取数组 key 值
                        attributes = child.li.attrs
                        key = attributes['key']
                        value = []
                        for li in child.ul:
                            if li == "\n":
                                continue
                            li_attributes = li.attrs
                            # 提取各自标签的 title 属性
                            try:
                                li_title = li_attributes['title']
                            except Exception:
                                li_title = li_attributes['key2']
                            value.append({'title': li_title, 'value': li_attributes['key2']})
                        attr_map.append({'name': text, 'mark': key, 'values': value})
            except Exception:
                continue
    return attr_map


def filter_line_break(data):
    """
    过滤换行符
    :param data:
    :return:
    """
    if data != "\n":
        return data


def store_condition_data(data, file):
    """
    查询条件存储
    """
    file_info = os.path.split(file)
    # 文件路径 & 文件名
    file_dir, file_name = file_info
    # 判断路径
    if not os.path.isdir(file_dir):
        os.mkdir(file_dir)
    # 判断文件
    if not os.path.exists(file):
        os.system(r'touch %s' % file)
    # 写文件
    with open(file, 'w+', encoding='utf-8') as f:
        data = dumps(data)
        f.write(data)
        f.seek(0)
        res = f.read()
        return res


def store_data(data):
    """
    写入数据库
    :param data:
    :return:
    """
    connect = pymysql.Connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_DATABASE,
        charset=DB_CHARSET
    )
    cursor = connect.cursor()
    for v in data:
        c_str = "INSERT INTO diamond_conditions (`name`, `mark`) VALUES ('" + v['name'] + "','" + v['mark'] + "')"
        try:
            cursor.execute(c_str)
            id = connect.insert_id()
        except Exception:
            id = None
        if id is None:
            print('Insert Failed : ' + c_str)
            exit()
        v_str = "INSERT INTO diamond_condition_values (`condition_id`, `title`, `value`) VALUES "
        v_sql = ""
        for value in v['values']:
            v_sql += "('" + str(id) + "','" + value['title'] + "','" + value['value'] + "'),"
        v_str += v_sql[:-1]
        try:
            cursor.execute(v_str)
            # 提交
            connect.commit()
        except Exception:
            # 提交回滚
            connect.rollback()


def main():
    attr_map = condition()
    # 写数据库
    store_data(attr_map)
    # 写文件操作
    store_condition_data(attr_map, CONDITION_FILE_DIR)
    if os.path.exists(CONDITION_FILE_DIR):
        print('Successful access to conditions !')


if __name__ == '__main__':
    main()
