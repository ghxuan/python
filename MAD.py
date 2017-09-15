#下载MAD排行榜上的视频
import os
import requests
from json import loads

#for获取aid并下载视频
def get_id(url):
    html=requests.get(url, params={'wd': 'python'})
    html=loads(html.text)
    htm=html['result']
    for i in htm:
        a=(i['id'])
        ur = ('you-get https://www.bilibili.com/video/av{}/').format(a)
        os.system(ur)

def main ():
    for i in range(1):
        # 2014+3=2017   从0开始
        i = 2014 + i
        for j in range(12):
            # 12个月
            j = j + 1
            if j == 4 or j == 6 or j == 9 or j == 11:
                k = 30
            else:
                k=31
                if j == 2:
                    if i%4==0:
                        k=29
                    else:
                        k=28
            timefrom = i * 10000 + j * 100 + 1
            timeto = i * 10000 + j * 100 + k
            url='https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&pic_size=160x100&order=click&copy_right=-1&cate_id=24&page=1&pagesize=20&time_from={}&time_to={}'.format(timefrom,timeto)
            get_id(url)

if __name__ == '__main__':
    main()
