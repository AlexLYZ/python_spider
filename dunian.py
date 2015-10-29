import urllib
import urllib.request

data={}
data['word']='最美 女星'
#urllib.parse库对普通字符串转符合url的字符串
url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url=url+url_values

response = urllib.request.urlopen(full_url)
html = response.read()
print(html)