from urllib import request
import base64
from zlib import decompress
import os


def request_html(page_url):
    with request.urlopen(page_url) as f:
        data = f.read()
    res = data.decode('utf-8')
    return res


# 基于页面 ajax 接口返回的数据解密接口
def request_api(api_url):
    with request.urlopen(api_url) as f:
        data = f.read()
    res = base64.b64decode(data)
    res = decompress(res, -8)
    res = res.decode('utf-8')
    return res


def get_request_info(request_url):
    with request.urlopen(request_url) as f:
        return f.info()


def read_file(file_path):
    """
    文件读取
    :param file_path:
    :return:
    """
    if not os.path.isfile(file_path):
        return 'error file path'
    with open(file_path, 'r', encoding='utf-8') as f:
        f.seek(0)
        res = f.read()
        return res
