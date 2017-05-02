# -*- coding: utf-8 -*
import requests
import re
from bs4 import BeautifulSoup

#煎蛋#
def get_img():
    x = 0
    res = requests.get('http://jandan.net/ooxx')
    soup = BeautifulSoup(res.text, 'html.parser')
    for index, each in enumerate(soup.find_all("a", target="_blank", class_="view_img_link")):
        with open('H:\Pic2\{}.jpg'.format(index), 'wb') as file:
            file.write(requests.get('http:'+each.attrs['href'], stream=True).content)
            x += 1
            print str(x)+'张图片已抓取!'


if __name__ == '__main__':
    get_img()

