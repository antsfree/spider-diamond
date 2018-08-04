#!/usr/bin/env python3
# -*- coding: utf-8 -*-
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = ''
DB_DATABASE = 'diamond'
DB_CHARSET = 'utf8'

# 钻石接口 URL
BASE_API_URL = 'http://www.zbird.com/apidiamond/ajaxdiamondNative/'
# 单页显示条数
PAGE_SIZE = '20'
# 全球搜索
GLOBAL_SEARCH = '2'
# 国内搜索
DOMESTIC_SEARCH = '1'
# 默认搜索条件
DEFAULT_SEARCH_CONDITION = 'priStoneWeight/0.3-10000/'

# 钻石首页
DIAMOND_URL = "http://www.zbird.com/diamond/"
# 条件数据文件路径
CONDITION_FILE_DIR = "./data/condition.json"