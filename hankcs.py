import urllib
import urllib.request
import re
from collections import deque

url = 'http://www.hankcs.com/'
queue = deque()
queue.append(url)
visited = set()
cnt = 0

while queue:
	url = queue.popleft()
	#visited |=url
	visited |={url}
	print('已经抓取：'+str(cnt)+'正在抓取<---'+url)
	cnt+=1
	try:
		#urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
		#The optional timeout parameter specifies a timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used). 
		response = urllib.request.urlopen(url,timeout = 2)
	except:
		continue
	if 'html' not in response.getheader('Content-Type'):
		continue
	try:
		#这里为啥不能用html = response.read()而是必须加decode('utf-8')？
		html = response.read().decode('utf-8')
	except:
		continue
	
	pattern = re.compile('.*?href=\"(.+?)\"')
	#pattern = re.compile('href=\"(.+?)\"')
	for x in pattern.findall(html):
		if 'http' in x and x not in visited: 
			#print(x)
			queue.append(x)
			print('加入队列--->'+x)
	
