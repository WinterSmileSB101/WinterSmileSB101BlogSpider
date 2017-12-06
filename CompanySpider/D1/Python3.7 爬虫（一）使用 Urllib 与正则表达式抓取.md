---
title: Python3.7 爬虫（一）使用 Urllib 与正则表达式抓取
date: 2017-04-08
date: 2017-04-09
categories: 
- 爬虫
- Python 爬虫
tags: - Python3
- 爬虫
- Urllib2
- 正则表达式
---
> 版权声明：本文为 wintersmilesb101 -（个人独立博客– [http://wintersmilesb101.online](http://wintersmilesb101.online) 欢迎访问）博主原创文章，未经博主允许不得转载。## 我们今天就一起来通过 Python3 自带库 Urllib 与正则表达式来抓取糗事百科。废话不多说，下面正题：
### 分析网址
通过浏览器进入糗事百科首页，[[http://www.qiushibaike.com/](http://www.qiushibaike.com/)]([http://www.qiushibaike.com/](http://www.qiushibaike.com/))你会看到如下界面：然后按下F12，进入开发者模式，感觉貌似没什么特殊的嘛。那么直接通过 [[http://www.qiushibaike.com/](http://www.qiushibaike.com/)]([http://www.qiushibaike.com/](http://www.qiushibaike.com/)) 网址进行爬取。
### 准备工作
既然是第一篇，那么必不可少的就是环境的搭建以及编辑器的选取。
这里环境的搭建我就不多说了 廖雪峰廖老师的教程中说的很清楚,Python一点都不了解的童鞋可以先看看这个学习一下，我也整理了 PDF 以及 EPUB 版本，观看或者下载，地址
至于编辑器，我这里推荐 vscode，好看开源插件多,这里再介绍开发 python 时候的辅助插件，地址新建项目文件夹任意找一个位置，只要你自己觉得舒服的地方新建一个项目文件夹，比如我的项目位置是：E:\adt-bundle-windows-x86_64-203030\python\3.x\projects\demo
``` cmd
E:\adt-bundle-windows-x86_64-20131030\python\3.x\projects\demo

```
### 新建文件
我这里是使用的 vscode 选中文件夹右键通过vscode打开，而后在软件中的文件夹上右键新建文件，输入 
``` plain
然后输入如下语句：
```python
# -*- coding: utf-8 -*-
import urllib.request
import urllib

url = "http://www.qiushibaike.com"
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
print(content)

```
运行，出师不利啊，看看提示，说是没有响应。
##### 访问网页无响应
其实就是网站的 UA 防护，一般的网站都要检查是否是浏览器在进行访问，所以我们这里的方式就是设置请求头，最简答的设置一个浏览器类型好了。为上述代码添加如下代码,并且修改打开url 为 req：
``` python
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
req = urllib.request.Request(url, headers={
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
})

```
### 再次运行,这里网页太长就不贴完了。
![image](http://on792ofrp.bkt.clouddn.com/17-4-8/85847293-file_1491656241405_70a9.png)
### 提取自己想要的信息
前面我们已经拿到了网页 html 想做什么都随便我们了，这里我们要使用这些 html 来获得我们想要的信息。比如这里我们要获取每条段子的文字或者图片链接那么再次回到浏览器，按下 F12，点击 Elements 面板，效果如下：
从上图可以发现，我们需要的信息在右边，1 位置是发布者，发布者头像等，2 位置就是我们所需要的文字内容了，3 位置就是我们的图片了，没有图片的话是没有 3 位置的 div 的。
### 设计正则表达式
这里给出一个学习 Python3 re 模块正则表达式，对正则表达式不了解的可以看看，想要深入了解请自行百度正则表达式，[http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html](http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html)
我们要匹配的内容如下：
``` html
<a href="/article/118848511" target="_blank" class="contentHerf">
<div class="content">
<span>今天去相亲了！去之前，媒人拿出了张照片 说女方喜欢拍古装艺术照 我一看照片 虽然只露出眼睛和眉毛，但从我阅人无数的经验来看，此女子也应该还不错！可回来之后，我生气的质问媒人 完全跟照片不一样啊 媒人说.....你是不是把照片拿反了.....</span>
</div>
</a>

<div class="thumb">
<a href="/article/118848511" target="_blank">
<img src="http://pic.qiushibaike.com/system/pictures/11884/118848511/medium/app118848511.jpg" alt="完全跟照片不一样啊">
</a>
</div>

```
先来匹配文字部分吧，
``` python
'<div.*?class="content">\n*?<span.*?</span>\n*?</div>'

```
使用 re 模块进行正则匹配，添加 re``` 引用，并且追加下面代码到文件末尾
``` plain
```python
pattern = re.compile('<div.*?class="content">\n*?<span.*?</span>\n*?</div>')
items = re.findall(pattern, content)
for item in items:
print(item)

```
运行：可以看到我们已经取出需要的标签了
![image](http://on792ofrp.bkt.clouddn.com/17-4-8/42316034-file_1491659592251_5971.png)
不过可以看到，这里我们获取到了只是标签的位置，这里我们需要的是内容，所以需要去掉我们不需要的部分，通过字符串的 replace(old,new) 可以实现这一点，修改代码如下：
``` python
b = '<div class="content"><span>'
for item in items:
temp = item.replace('\n', '')
temp = temp.replace('</span></div>', '')
print(temp.replace(b, '')+'\n')

```
再次运行：
![image](http://on792ofrp.bkt.clouddn.com/17-4-8/84188870-file_1491662005565_12201.png)
可以看到已经是纯文本了。
### 获取图片段子
编写正则表达式

``` python
'<a.*?>\n<img.*?>'

```
写入代码：
``` python



```
运行：
![image](http://on792ofrp.bkt.clouddn.com/17-4-8/14164501-file_1491662403193_3fa9.png)
和上面一样，获取到了标签，但是我们需要准确的数据，这里我们再使用一次正则表达式匹配网址：
``` python
'http:.*[JPEG|jpg]'

```
修改代码如下：
``` python
for item in items:
resp = re.compile('http:.*[JPEG|jpg]')
res = resp.findall(item)
print(res[0])

```
运行：
![image](http://on792ofrp.bkt.clouddn.com/17-4-8/99243932-file_1491663434712_16972.png)
图片地址取出来了
### 一次完成工作
下面我们来把上面的工作合到一起完成,这里就要提到一个概念 分组，[http://blog.csdn.net/seetheworld518/article/details/49302829](http://blog.csdn.net/seetheworld518/article/details/49302829)概念解释如下：
##### 正则表达式分组
分组就是用一对圆括号“()”括起来的正则表达式，匹配出的内容就表示一个分组。从正则表达式的左边开始看，看到的第一个左括号“(”表示第一个分组，第二个表示第二个分组，依次类推，需要注意的是，有一个隐含的全局分组（就是0），就是整个正则表达式。分完组以后，要想获得某个分组的内容，直接使用group(num)和groups()函数去直接提取就行。
例如：提取代码中的超链接中的文本
``` python
>>> s='<div><a href="https://support.google.com/chrome/?p=ui_hotword_search" target="_blank">更多</a><p>dfsl</p></div>'
>>> print re.search(r'<a.*>(.*)</a>',s).group(1)
更多
或者
>>> print re.match(r'.*<a.*>(.*)</a>',s).group(1)
更多

```
按照上面的分组匹配以后，我们就可以拿到我们想拿到的字串，但是如果我们正则表达式中括号比较多，那我们在拿我们想要的字串时，要去挨个数我们想要的字串时第几个括号，这样会很麻烦，这个时候Python又引入了另一种分组，那就是命名分组，上面的叫无名分组。
##### 命名分组
命名分组就是给具有默认分组编号的组另外再给一个别名。命名分组的语法格式如下：
(?P正则表达式)#name是一个合法的标识符如：提取字符串中的ip地址
``` python
>>> s = "ip='230.192.168.78',version='1.0.0'"
>>> re.search(r"ip='(?P<ip>\d+\.\d+\.\d+\.\d+).*", s)
>>> res.group('ip')#通过命名分组引用分组
'230.192.168.78'

```
##### 存在的一个坑
这里有一个匹配模式的坑，关于匹配模式：
re.compile() 函数还接受可选的第二个参数，用以设置匹配模式。可选的匹配模式有：
re.IGNORECASE：忽略大小写，同 re.I。
re.MULTILINE：多行模式，改变^和$的行为，同 - re.M。
re.DOTALL：点任意匹配模式，让’.’可以匹配包括’\n’在内的任意字符，同 re.S。
re.LOCALE：使预定字符类 \w \W \b \B \s \S 取决于当前区域设定， 同 re.L。
re.ASCII：使 \w \W \b \B \s \S 只匹配 ASCII 字符，而不是 Unicode 字符，同 re.A。
re.VERBOSE：详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。主要是为了让正则表达式更易读，同re.X。例如，以下两个正则表达式是等价的：
``` python
a = re.compile(r"""\d +  # the integral part
\.    # the decimal point
\d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")

```
看到这里是不是很兴奋啊？这样可以简化很多操作，那么来试试：
``` python
pattern = re.compile('<div.*?class="content">.*?<span>(.*?)</span>.*?</div>', re.S)
items = re.findall(pattern, content)

```
还没等运行呢，就报错了。。
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/82590970-file_1491698178159_13ce.png)
神马，说不存在？我去，什么意思，[https://docs.python.org/3.7/library/re.html?highlight=re#module-re](https://docs.python.org/3.7/library/re.html?highlight=re#module-re)莫非是在逗我吗？仔细研究，搞了半天，扫描了 3 遍[https://docs.python.org/3.7/library/re.html?highlight=re#module-re](https://docs.python.org/3.7/library/re.html?highlight=re#module-re)之后，终于发现了，你丫的藏的这么深！
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/64724203-file_1491698502237_17e1a.png)
原来在 Python 3.6 之后，把以前的 re.S 等等的 flag 全部转移到 RegexFlag 中了，所以我们要改变用法 把 改写成 ```re.RegexFlag.S```, 这次没有报错误了，运行(perfect nice！)：
``` plain

![image](http://on792ofrp.bkt.clouddn.com/17-4-9/23522085-file_1491698778621_16868.png)


### 我们的代码修改
于是我们根据分组以及模式匹配就可以非常简单的取到对应位置的正则表达式的值，修改正则表达式如下，现在我们一口气获取到内容与图片,最终代码：
```python
# -*- coding: utf-8 -*-
import urllib.request
import urllib
import re

url = "http://www.qiushibaike.com/imgrank/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
req = urllib.request.Request(url, headers={
'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
})
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')
print(content)
patternPic = re.compile('<a.*?>\n<img src="(.*?)".*?>')
pattern = re.compile('<div.*?class="content">.*?<span>(.*?)</span>.*?</a>'+'(.*?<div.*?"stats".*?</div>)', re.RegexFlag.S)
items = re.findall(pattern, content)
for item in items:
print(isinstance(item, str))
print()
if re.search('img', item[1]):
#再次匹配
patternA = re.compile('<a.*?>.*?<img src="(.*?)".*?>', re.RegexFlag.S)
img = patternA.findall(item[1])
print('段子：==> '+item[0], '\n\n', '段子图片：==> '+img[0]+'\n\n\n')
else:
print('段子：==> '+item[0], '\n\n\n')

```
效果如下：
![image](http://on792ofrp.bkt.clouddn.com/17-4-9/48412357-file_1491704503266_13654.png)
那么我们的爬虫就算是完成了，你也可以完善一下，比如说爬取用户的信息以及评论等最后欢迎交流学习。
