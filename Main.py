import urllib.request
import urllib
import os
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

url = input('url 입력 : ')
domain = input('도메인 입력 : ')

html = urllib.request.urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all('img')

point = input('저장위치 입력 : ') + "\\"

n = 0
for i in img:
    imgUrl = i.attrs['src']
    name = imgUrl.split('/')
    filename = point + name[len(name)-1]
    print(imgUrl)
    print(name[len(name)-1])

    if(imgUrl in "http"):
        urllib.request.urlretrieve(imgurl, +filename)

    else:
        a = (domain+imgUrl)
        print(a)
        urllib.request.urlretrieve(a, filename)
    n += 1
print('d')