import urllib.request
import http.cookiejar

#用报头创建opener
def makeMyopener(head = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
	'Connection':'keep-alive',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language':'zh-CN,zh;q=0.8',
}):
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	header = []
	for key,value in head.items():
		elem = [key,value]
		header.append(elem)
	opener.addheaders = header
	return opener
#写文件操作只包含三步，1：打开文件（指定打开方式）；2：数据写入文件	；3：关闭文件
def saveFile(data):
	save_path = 'D:\\temp.out'
	f_obj = open(save_path,'wb')#w以ascii文件打开文件，wb用于打开二进制文件
	f_obj.write(data)
	f_obj.close()

oper = makeMyopener()
#用opener对象的open函数打开URL
response = oper.open('http://www.baidu.com/',timeout = 1000)
data = response.read()
saveFile(data)
print(data)