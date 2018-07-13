#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
from function import request_html

url_diamond = "http://www.zbird.com/diamond/"


def main():
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

    print(attr_map)


if __name__ == '__main__':
    main()
