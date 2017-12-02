import urllib
import urllib.request
from bs4 import BeautifulSoup

url = "http://wintersmilesb101.online/"

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
})
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')
print(content)
