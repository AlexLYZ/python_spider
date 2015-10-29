import urllib
import urllib.request

data={}
data['word']='最美 女星'
url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url=url+url_values

response = urllib.request.urlopen(full_url)
html = response.read()
print(html)