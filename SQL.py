#从w3chool下载sql教程并转为pdf
import pdfkit
import requests
from bs4 import BeautifulSoup

def get_url_list(url):
    html = requests.get(url)
    #网页的编码是gb2312，需要encoding一下
    html.encoding = 'gbk'
    soup = BeautifulSoup(html.text, 'html5lib')
    soup=soup.find_all(id='course')[0]
    soup=soup.find_all('li')
    f=open('a.html','w')
    #加charset为utf-8，否则乱码
    f.write('<head><meta charset="UTF-8"></head>')
    op = {
        'page-size': 'Letter',
        'encoding': 'utf-8',
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    for i in soup:
        url='http://www.w3school.com.cn'+i.a.get('href')
        print(url)
        htm= requests.get(url)
        htm.encoding = 'gbk'
        sou = BeautifulSoup(htm.text, 'html5lib')
        sou = sou.find_all(id="maincontent")[0]
        sou=str(sou)
        f.write(sou)
    f.close()
    #写入pdf
    pdfkit.from_file('a.html', 'SQL.pdf',options=op)

def main():
    url = 'http://www.w3school.com.cn/sql/index.asp'
    get_url_list(url)

if __name__ == '__main__':
    main()