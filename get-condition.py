#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
from function import request_html
import os
from json import dumps

url_diamond = "http://www.zbird.com/diamond/"
condition_file = "./data/condition.json"


def condition():
    """
    获取钻石查询参数及对应值
    :return:
    """
    html = request_html(url_diamond)
    soup = BeautifulSoup(html, 'html.parser')
    # list
    elements = soup.find('div', {'id': 'searchBgMore'}).children
    attr_map = []
    text = ''
    for element in elements:
        if element == "\n":
            continue
        for child in element.children:
            # 判断不为空行
            if child == "\n":
                continue
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
                            except Exception as e:
                                li_title = li_attributes['key2']
                            value.append({'title': li_title, 'value': li_attributes['key2']})

                        attr_map.append({'name': text, 'mark': key, 'values': value})
            except Exception as e:
                continue

    return attr_map


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


def main():
    attr_map = condition()
    print(attr_map)
    # 写文件操作
    store_condition_data(attr_map, condition_file)
    if os.path.exists(condition_file):
        print('Successful access to conditions !')


if __name__ == '__main__':
    main()
