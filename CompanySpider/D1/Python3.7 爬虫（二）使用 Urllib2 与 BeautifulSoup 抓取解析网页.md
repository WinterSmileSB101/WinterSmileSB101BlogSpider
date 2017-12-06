---
title: Python3.7 爬虫（二）使用 Urllib2 与 BeautifulSoup 抓取解析网页
date: 2017-04-08
date: 2017-04-09
categories: 
- 爬虫
- Python 爬虫
tags: - Python3
- 爬虫
- Urllib2
- BeautifulSoup4
---
> 版权声明：本文为 wintersmilesb101 -（个人独立博客– [http://wintersmilesb101.online](http://wintersmilesb101.online) 欢迎访问）博主原创文章，未经博主允许不得转载。## 开篇
上一篇中我们通过原生的 re 模块已经完成了网页的解析，对于熟悉正则表达式的童鞋来说很好上手，但是对于萌新来说，还是有一定难度以及复杂度的，那么这里我们就来使用第三方解析包来解析获取到的网页吧。
## BeautifulSoup
官方的 BeautifulSoup 是这样的：
``` plain
Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。
Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。
Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。

```
而且这个支持多种解析方式，以及解析方式中也可以加上正则表达式来过滤结果，是不是已经迫不及待要试试这个第三方库了？那么看看[[http://beautifulsoup.readthedocs.io/zh_CN/latest/](http://beautifulsoup.readthedocs.io/zh_CN/latest/)]([http://beautifulsoup.readthedocs.io/zh_CN/latest/](http://beautifulsoup.readthedocs.io/zh_CN/latest/))，如果看不到超链的：[http://beautifulsoup.readthedocs.io/zh_CN/latest/](http://beautifulsoup.readthedocs.io/zh_CN/latest/) ，或者看看这篇博文，[[http://cuiqingcai.com/1319.html](http://cuiqingcai.com/1319.html)]([http://cuiqingcai.com/1319.html](http://cuiqingcai.com/1319.html)) : [http://cuiqingcai.com/1319.html](http://cuiqingcai.com/1319.html) ,文档说的很清楚，从安装到使用，所以我这里就不再添足了。下面直接讲怎么使用它来解析一篇网页，我们这里还是以 [http://www.qiushibaike.com/imgrank/](http://www.qiushibaike.com/imgrank/) 来实验。
## 获取网页内容
网址：[http://www.qiushibaike.com/imgrank/](http://www.qiushibaike.com/imgrank/)网页内容以及我们想要获取的信息如下：
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/4266580-file_1491711270558_5f86.png)
下面解释一下上图中几个位置的对应信息
- 作者信息
- 段子文字部分
- 段子图片部分（如果没有图片则没有这个元素）
- 段子评分以及评论
我们这里还是通过 Urllib2 来获取网页内容，代码如下：

``` python
# -*- coding: utf-8 -*-
import urllib
import urllib.request

url = "http://www.qiushibaike.com/imgrank/"
print(url)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
req = urllib.request.Request(url, headers={
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
})
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')
print(content)

```
运行,网页获取成功：
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/14740586-file_1491710935660_6128.png)
## 解析 Html
下面就是解析了，先引入包
``` python
from bs4 import BeautifulSoup

```
### 分别解析
然后使用解析，这里我们先来获取作者头像链接，尾部添加代码如下：

``` python
soup = BeautifulSoup(content, "lxml")
items = soup.select("div.author a img")
for item in items:
print(item['src'])

```
这里我是用的解释器是 lxml 这里你也可以使用原生的 html.parser，不过 html.parser 解析速度一般而且对中文支持不是很好，所以这里我们用解析快对中文支持好的 lxml 具体的解释器文档请看 [http://beautifulsoup.readthedocs.io/zh_CN/latest/](http://beautifulsoup.readthedocs.io/zh_CN/latest/)
我使用的方式是：css 选择器，因为我粗略还是有点 Web 功底，所以感觉这个比较顺手，你们可以选择其他方式，看自己喜好了，建议多看 [http://beautifulsoup.readthedocs.io/zh_CN/latest/](http://beautifulsoup.readthedocs.io/zh_CN/latest/) 来熟悉这个库的使用。想要使用css选择器但是不熟悉 css 的可以看看这里 [http://www.uisdc.com/css-selector](http://www.uisdc.com/css-selector)
运行结果如下,是不是很简单？：
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/72364438-file_1491712058576_15dc9.png)
### 一次性解析
通过上面的解析，我们已经会使用 BeautifulSoup来进行解析 html 了那么这次来解析剩下的东西，最终代码如下：
``` python

# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib.request

url = "http://www.qiushibaike.com/"
print(url)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
req = urllib.request.Request(url, headers={
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
})
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')
print(content)
soup = BeautifulSoup(content, "lxml")
items1 = soup.select("div.author a img")
items2 = soup.select("a div.content span")
items3 = soup.select("div.thumb a img")
n = 0
length1 = len(items1)
length3 = len(items3)
while n < length1:
print('作者信息：\n名称：'+items1[n]['alt']+'\n头像链接：'+items1[n]['src']+'\n\n')
print('段子信息：\n段子：'+items2[n].text+'\n')
#以免有些没有图片的段子报错
if n < length3:
print('段子图片链接：'+items3[n]['src']+'\n\n\n')
else:
print('\n\n\n')
n += 1

```
运行，结果：
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/72021861-file_1491716802757_e01d.png)
可以看到我们的数据已经全部取出来了。
## 获取全部网页段子
那么想要获取全部的段子怎么办？网页中下方有页数，先通过主页获取一个html 然后得到页数 后面通过 [http://www.qiushibaike.com/imgrank/page/](http://www.qiushibaike.com/imgrank/page/) +页数就可以了，比如我们这里的首页其实也可以表示为 [http://www.qiushibaike.com/imgrank/page/](http://www.qiushibaike.com/imgrank/page/)1 ，表示之后通过循环或者递归调用爬取即可。
