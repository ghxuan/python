#爬取笔趣阁雪鹰领主小说
#如果想爬取其他此网站的小说，请替换url
import re
import requests
from time import sleep
from bs4 import BeautifulSoup

def main ():
    #打开小说的目录页替换就可以下载了
    url='http://www.biquge5200.com/2_2598/'
    html=requests.get(url)
    soup=BeautifulSoup(html.text,'lxml')
    title=soup.find_all('meta',property="og:title")
    title=title[0]["content"]
    title=str(title)+'.txt'
    #新建并打开txt
    f = open(title, 'w')
    print(title)
    soup=soup.find_all('dd')
    b = re.findall(r'href="(.*?)"',str(soup), re.S | re.M)
    a=len(soup)
    for i in range(a-9):
        htm=requests.get(b[i+9])
        sou = BeautifulSoup(htm.text, 'lxml')
        # sozj是小说的章节
        sozj = re.findall(r'<h1>(.*?)</h1>', str(sou), re.S | re.M)
        #so是小说的内容
        so= sou.find_all('div',id="content")
        s = re.findall(r'(.*?)<br/>', str(so), re.S | re.M)
        c=len(s)
        f.write(str(sozj[0]))
        f.write('\n')
        s0=s[0][19:]
        f.write(s0)
        f.write('\n')
        for j in range(c-1):
            f.write(s[j+1])
            f.write('\n')
        f.write('\n')
        print(sozj[0],'完')
        #防止出现错误，我曾使用过0.5,0.2,0.1都会出现错误，间隔太短
        sleep(1)
    f.close()

if __name__ == '__main__':
    main()
