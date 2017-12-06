---
title: Python3.7 爬虫（三）使用 Urllib2 与 BeautifulSoup 爬取网易云音乐歌单
date: 2017-04-08
date: 2017-04-09
categories: 
- 爬虫
- Python 爬虫
tags: - Python3
- 爬虫
- Urllib2
- BeautifulSoup4
- 网易云音乐
---
> 版权声明：本文为 wintersmilesb101 -（个人独立博客– [http://wintersmilesb101.online](http://wintersmilesb101.online) 欢迎访问）博主原创文章，未经博主允许不得转载。## 废话
在前面的的博客中我们已经能够使用 python3 配合自带的库或者第三方库抓取以及解析网页，我们今天来试试抓取网易云音乐的歌单信息
## 分析网页
要战胜敌人，必须要先了解敌人，然后设计对策，一招致命！首先浏览器打开网页,按下 F12：[http://music.163.com/#/discover/playlist](http://music.163.com/#/discover/playlist)
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/97112442-file_1491733756817_11fd6.png)
我们现在来分析网页点击右侧界面中的 Network 进入网络请求分析界面，如下：
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/6973030-file_1491737101600_42e2.png)
上图中我们可以看到请求还分了类型的，这里我们查看类型为 document 的条目，看着 playlist 条目比较像是包含歌单的文件，于是我们点击 playlist 条目：
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/12701192-file_1491737361762_63ac.png)
点击 preview， 如上图，我们左边的歌单在右边找到了，看来就是这个请求获取到了歌单。然后我们点击 Headers 界面，来到请求头信息界面：
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/47017176-file_1491737695288_d25c.png)
可以看到，这条请求的网址是：[[http://music.163.com/discover/playlist](http://music.163.com/discover/playlist)]([http://music.163.com/discover/playlist](http://music.163.com/discover/playlist)) ，向下翻还可以发现，host 为 music.163.com，下面我们就可以来获取网页数据了，不过现在网址变成了：[[http://music.163.com/discover/playlist](http://music.163.com/discover/playlist)]([http://music.163.com/discover/playlist](http://music.163.com/discover/playlist))
## 抓取 html
网页内容获取，按照三部曲来做
直接通过网址访问，看能否取到需要的 html (一般是不可能的)
通过设置 headers，一开始就设置一个 UA，如：'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}``` 不过一般来说是可以通过正确获得 html 的，但是有些网站会判断 host 是否是自己，所以有的时候我们还需要加上(这里以我们要访问的网易歌单界面来作为例子)：```'Host': 'music.63.com'

一开始能获取，多次调试后不能获取了？这个是网站检测到你的 IP 访问次数过多而禁止你访问了（也就是防止）我们就需要设置代理来避免这个问题。示例代码如下：
23456789import urllib2enable_proxy = Trueproxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})null_proxy_handler = urllib2.ProxyHandler({})if enable_proxy:    opener = urllib2.build_opener(proxy_handler)else:    opener = urllib2.build_opener(null_proxy_handler)urllib2.install_opener(opener)
``` plain
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}``` 不过一般来说是可以通过正确获得 html 的，但是有些网站会判断 host 是否是自己，所以有的时候我们还需要加上(这里以我们要访问的网易歌单界面来作为例子)：```'Host': 'music.163.com'

```
通过上面的分析我们就通过网址：[http://music.163.com/discover/playlist](http://music.163.com/discover/playlist) 来获取歌单，先直接获取，不设置 Headers，运行，发现就输出了：
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/29378890-file_1491738242783_438.png)
这样我们就可以开始解析 html 了，不过我还是建议添加上 UA 与 host ，养成一个习惯，不要每次都试来浪费时间。于是我们获取 html 的代码如下：

``` python
# 爬取网易云音乐的爬虫
# -*- coding: utf-8 -*-
import urllib.request
import urllib


def gethtml(url, headers={}):
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')
response.close()
return content


url = 'http://music.163.com/discover/playlist'
url = gethtml(url, headers={
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
'Host': 'music.163.com'
})
print(url)

```
## 解析 html
这里我们使用 BeautifulSoup4 使用 css 选择器来选择元素来解析 html ，回到浏览器 F12，来分析怎么获得需要的信息：
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/35806465-file_1491738755214_2afb.png)
如图，从上到下依次的信息是
- 歌单封面
- 歌单名称与链接
- 歌单播放量
- 歌单创建人以及创建人主页
那么我们现在就来以此通过css 选出包含内容的最小标签。封面图片 img 标签

``` python
soup.select('ul#m-pl-container li div img')
```

歌单名称与链接 a 标签

```python
soup.select('ul#m-pl-container li div a.msk')

```
歌单播放量 span 标签

``` python
soup.select('div.bottom span.nb')

```
歌单创建人与创建人主页

``` python
soup.select('ul#m-pl-container li p a')

```
然后我们通过遍历来输出这些标签中的信息，完整代码如下：

``` python
# 爬取网易云音乐的爬虫
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib

#获取网页
def gethtml(url, headers={}):
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')
response.close()
return content

#解析音乐列表网页
def parsehtmlMusicList(html):
soup = BeautifulSoup(html, 'lxml')
list_pic = soup.select('ul#m-pl-container li div img')
list_nameUrl = soup.select('ul#m-pl-container li div a.msk')
list_num = soup.select('div.bottom span.nb')
list_author = soup.select('ul#m-pl-container li p a')
n = 0
length = len(list_pic)
while n < length:
print('歌单图片：'+list_pic[n]['src']+'\n\n')
print('歌单名称：'+list_nameUrl[n]['title']+'\n\n歌单地址：'+list_nameUrl[n]['href']+'\n\n')
print('歌单播放量：'+list_num[n].text+'\n\n')
print('歌单作者：'+list_author[n]['title']+'\n\n作者主页：'+list_author[n]['href']+'\n\n\n')
n += 1


url = 'http://music.163.com/discover/playlist'
url = gethtml(url, headers={
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
'Host': 'music.163.com'
})
parsehtmlMusicList(url)

```
最终效果如下：
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/19355149-file_1491739358799_11116.png)
欢迎交流。
