import urllib.request
import re
#返回http.client.HTTPResponse对象
#urllib.request.urlopen()抓取指定url的页面
response = urllib.request.urlopen(" http://baidu.com")
#response = urllib.urlopen("http://www.baidu.com/")
#data = response.getheader('http-equiv')
html = response.read().decode('UTF-8')
pattern = re.compile('meta http-equiv="refresh" content="0;url=(.+?)"')
for x in pattern.findall(html):
	print(x)
	response = urllib.request.urlopen(x)
	data = response.read()
	print(data)
	request = urllib.request.Request(x,headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
		'Connection':'keep-alive',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language':'zh-CN,zh;q=0.8',
		#'Accept-Encoding':'gzip, deflate, sdch'
	})
	response2 = urllib.request.urlopen(request)
	data2 = response2.read()
	print(data2)
print (html)
#print(data)