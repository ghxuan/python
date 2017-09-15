#下载b站收藏的视频和字幕，如果视频已失效就无法下载下来了
import os
import requests
from json import loads

#获得id号,并使用you-get下载视频和字幕(获取一个链接下载一个)
def get_aid(url):
	# 获得网页的源代码
	html = requests.get(url, params={'wd': 'python'})
	# 将html的type转换为str
	html = html.text
	# 网页的最前面及最后面有瑕疵，截取有用部位
	html = html[17:-1]
	# 将html的type通过json转换为字典
	htm = loads(html)
	# 将html的archives的30个内容取出
	ht = htm['data']['archives']
	# 取aid号
	for i in ht:
		a=(i['aid'])
		ur=('you-get https://www.bilibili.com/video/av{}/').format(a)
		os.system(ur)
	return ur

def main():
	#url1会暴露身份，获取网址在readme的gif中
	url1=''
	url2='&order=fav_time&jsonp=jsonp&callback=_jsonpxg70odvp4m'
	for i in range(31):
		#i+1是页数,31是全部页数
		url=url1+str(i+1)+url2
		aid=get_aid(url)

if __name__ == '__main__':
    main()
