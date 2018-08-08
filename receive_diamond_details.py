from function import *
from bs4 import BeautifulSoup, Comment


class DiamondDetail:
    def __init__(self, detail_url):
        """
        初始化页面代码
        :param detail_url:
        """
        html = request_html(detail_url)
        self.soup = BeautifulSoup(html, 'html.parser')

    def receive_images(self):
        """
        获取轮播图
        :return:
        """
        tags = self.soup.find(class_='show_pic_diam')
        dd = tags.find('dd')
        if dd is None:
            dd = tags.find('dt')
        images = dd.find_all('img')
        img_list = []
        for img in images:
            img_url = img.get('src')
            # 获取大图
            if img_url.find('150'):
                img_url = img_url.replace('150', '400')
            img_list.append(img_url)
        return img_list

    def receive_certificate_code(self):
        """
        获取证书编号
        :return:
        """
        tag = self.soup.find(class_='f_psys_inf inf_txtcer')
        cert_tag = tag.find('b')
        cert_code = ''
        if cert_tag is not None:
            cert_code = cert_tag.text
        return cert_code.strip()


detail = DiamondDetail('http://www.zbird.com/diamond/6067057.html')
# 图片
images = detail.receive_images()
# 证书编号
certificate_code = detail.receive_certificate_code()
print(certificate_code)
exit()
