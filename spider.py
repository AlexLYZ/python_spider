import urllib.request
#返回http.client.HTTPResponse对象
#urllib.request.urlopen()抓取指定url的页面
response = urllib.request.urlopen("http://www.baidu.com/")
#response = urllib.urlopen("http://www.baidu.com/")
html = response.read()
print (html)