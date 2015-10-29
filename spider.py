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
print (html)
#print(data)