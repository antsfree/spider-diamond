from function import *
from bs4 import BeautifulSoup, Comment

detail_url = 'http://www.zbird.com/diamond/6046003.html'

html = request_html(detail_url)
soup = BeautifulSoup(html, 'html.parser')
# 获取轮播图
tags = soup.find(class_='show_pic_diam')
images = tags.find_all('img')
img_list = []
for img in images:
    img_list.append(img.get('src'))
print(img_list)
exit()
img_url = []
for tag in tags:
    img = tag.find('img')
    img_url.append(img.get('src'))
print(img_url)
exit()
img_tags = tags.img
print(img_tags)
