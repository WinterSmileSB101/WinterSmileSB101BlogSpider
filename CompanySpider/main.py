import urllib
import urllib.request as req
from bs4 import BeautifulSoup

url = "http://wintersmilesb101.online/"

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# 设置代理 IP，http 不行，使用 https
proxy = req.ProxyHandler({'https': 's1firewall:8080'})
auth = req.HTTPBasicAuthHandler()
# 构造 opener
opener = req.build_opener(proxy, auth, req.HTTPHandler)
# 添加 header
opener.addheaders = [('User-Agent', user_agent)]
# 安装 opener
req.install_opener(opener)
# 打开链接
conn = req.urlopen(url)
# 以 utf-8 编码获取网页内容
content = conn.read().decode('utf-8')
# 输出
print(content)
