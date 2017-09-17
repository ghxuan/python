#下载p站插画排行榜图片,从20140101到20171231,可能会有重复(请忍耐)
import requests
from json import loads

#获取图片下载地址并下载图片
def get_url(url):
    hea = {
        'referer': ' ',
        'user-agent': 'Mozilla/5.0(X11;Linuxx86_64) AppleWebKit/537.36(KHTML, likeGecko) Chrome / 60.0.3112.78Safari / 537.36'
    }
    html=requests.get(url)
    html=loads(html.text)
    html=html['contents']
    for i in html:
        #ur是图片地址及做修改后的地址
        ur=i['url']
        #id是图片的号
        id=ur[65:73]
        #以id号给图片命名
        name = id + ur[87:91]
        #home是本地下载的地址
        home='/home/x/Pictures/pixiv/'+name
        hea['referer'] = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id={}'.format(id)
        ur=ur[0:19]+'/img-original'+ur[40:76]+ur[87:91]
        htm=requests.get(ur,headers=hea)
        with open(home, 'wb') as file:
            file.write(htm.content)

def main():
    for i in range(4):
        # 2014+3=2017   从0开始
        i = 2014 + i
        for j in range(12):
            # 12个月
            j = j + 1
            if j == 4 or j == 6 or j == 9 or j == 11:
                k = 30
            else:
                k = 31
                if j == 2 and i % 4 == 0:
                    k = 29
                else:
                    if j == 2:
                        k = 28
            for n in range(k):
                data=i*10000+j*100+n+1
                url = 'https://www.pixiv.net/ranking.php?mode=daily&content=illust&date={}&p=1&format=json&tt=2515210a99b6ab1f46fe00734cd03970'.format(data)
                get_url(url)

if __name__ == '__main__':
    main()