from urllib import request
import base64
from zlib import decompress

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
