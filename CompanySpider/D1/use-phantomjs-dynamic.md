---
title: use-phantomjs-dynamic
date: 2017-03-24
date: 2017-03-24
categories: 
- 爬虫
- Node.js 爬虫
tags: - 爬虫
- Node.js
- 动态网页
- PhantomJS
---
> 版权声明：本文为 wintersmilesb101 -（个人独立博客– [http://wintersmilesb101.online](http://wintersmilesb101.online) 欢迎访问）博主原创文章，未经博主允许不得转载。##### 今天我们来学习如何使用 PhantomJS 来抓取动态网页，至于 PhantomJS 是啥啊什么的，看这里 我们这里就不再讨论 PhantomJS 的入门基础了。下面正题
##### 今天我们来抓取网易新闻 http://news.163.com/
![image](http://on792ofrp.bkt.clouddn.com/17-3-24/42068278-file_1490319843051_4972.png)

``` javascript
var page=require('webpage').create();

```
- page.content String：获取或设置当前页面的html。
- page.plainText String：这是一个只读属性，获取页面去除html标记的文本（考虑$.text()）。

``` javascript
var page = require('webpage').create();
phantom.outputEncoding="gbk";//指定编码方式
page.open("http://news.163.com/", function(status) {
if ( status === "success" ) {
console.log(page.content);//输出网页
} else {
console.log("网页加载失败");
}
phantom.exit(0);//退出系统
});

```
![image](http://on792ofrp.bkt.clouddn.com/17-3-24/63115879-file_1490320458928_d4ed.png)
![image](http://on792ofrp.bkt.clouddn.com/17-3-24/69246509-file_1490321926785_189d.png)

``` javascript
var pattern = 'ul li.newsdata_item div.ndi_main div a';

```
page.evaluate(fn, [param])  对于page打开的页面，往往需要与其进行一些交互。 page.evaluate()提供了在page打开页面的上下文（下文直接用page上下文指代）执行function的功能（类比Chrome开发者工具的控制台）。如下例：
在这个例子中， page.evaluate()接受两个参数，第一个是必需的，表示需要在page上下文运行的函数 fn；第二个是可选的，表示需要传给 fn的参数 param。 fn允许有一个返回值return，并且此返回值最终作为 page.evaluate()的返回值。这边对于刚刚命名的 param和return有一些额外的说明和注意事项。对于整个phantom进程而言， page.evaluate()是跑在一个沙盒中， fn无法访问一切phantom域中的变量；同样 page.evaluate()方法外部也不应该尝试访问page上下文中的内容。那么如果两个作用域需要交换一些数据，只能依靠 param和 return。不过限制很大， param和 return必须为能够转化为JSON字符串，换言之，只能是基本数据类型或者简单对象，像DOM 节点、$对象、function、闭包等就无能为力了。这个方法是同步的，如果执行的内容对后续操作不具备前置性，可以尝试异步方法以提高性能：page.evaluateAsync()。看懂了 API 我们接着干活，修改成如下89101112131415161718192021var page = require('webpage').create();phantom.outputEncoding="gbk";//指定编码方式page.open("http://news.163.com/", function(status) {if ( status === "success" ) {console.log(page.evaluate(function(){  var d = '';  //匹配 DOM 查询语句  var pattern = 'ul li.newsdata_item div.ndi_main div a img';  var c = document.querySelectorAll(pattern);//查询  var l = c.length;  //遍历输出  for(var i =0;i<l;i++){  					d=d+c[i].alt+'\n'//获取 alt 值  					}            return d;}));//输出网页标题} else {console.log("网页加载失败");}phantom.exit(0);//退出系统});
``` javascript
page.open('http://m.bing.com',function(status){
vartitle=page.evaluate(function(s){
returndocument.querySelector(s).innerText;
},'title');
console.log(title);
phantom.exit();
});

```
### 这里说明一下，我们在的到具体的标签之后，如果我们想获取比如 a 标签的 alt 属性的值 我们可以直接写 获取到的单个值.alt 就像上面的一样如果是获取 title 属性那么直接.title 就可以了，如果是获取标签内的文本，那么久通过.innerText 获取 怎么样是不是很简单呢
![image](http://on792ofrp.bkt.clouddn.com/17-3-24/54949103-file_1490323559159_1166a.png)

``` javascript
var page = require('webpage').create();
phantom.outputEncoding="gbk";//指定编码方式
page.open("http://news.163.com/", function(status) {
if ( status === "success" ) {
var res = page.evaluate(function(){
var d = '';
//匹配 DOM 查询语句 a 标签
var patternA = 'ul li.newsdata_item div.ndi_main div a img';
//匹配 DOM 查询语句 新闻内容 div
var patternNews = 'ul li.newsdata_item div.ndi_main div div div.news_title h3 a';
//匹配 DOM 查询语句 新闻标签 div
var patternNewsClass = 'ul li.newsdata_item div.ndi_main div div div.news_tag strong a';
var patternNewsKeyWords = 'ul li.newsdata_item div.ndi_main div div div.news_tag div a';
var c = document.querySelectorAll(patternA);//查询
var l = c.length;
//遍历输出
for(var i =0;i<l;i++){
d = d + "标题："+c[i].alt+'\n';
d = d + "图片链接: "+c[i].src+'\n';
d = d + '\n';
}
c = document.querySelectorAll(patternNews);//查询
l = c.length;
//遍历输出
for(var i =0;i<l;i++){
d +="新闻链接："+c[i].href+'\n';
d = d + '\n';
}
c = document.querySelectorAll(patternNewsClass);//查询
l = c.length;
//遍历输出
for(var i =0;i<l;i++){
d +="新闻类别："+c[i].innerText+'\n';
d = d + '\n';
}
c = document.querySelectorAll(patternNewsKeyWords);//查询
l = c.length;
//遍历输出
for(var i =0;i<l;i++){
d +="新闻关键词："+c[i].innerText+'\n';
d +="关键词链接："+c[i].href+'\n';
d = d + '\n';
}
d = d + '\n';
return d;
});//输出网页标题

console.log(res);
} else {
console.log("网页加载失败");
}
phantom.exit(0);//退出系统
});

```
##### 最后页面如下，强迫症的同学可以修改下代码让他显示更合理,那么就到这里，可以看到 使用 PhantomJS 抓取动态页面可谓是非常方便，不过就是加载速度上可能会慢一些。
![image](http://on792ofrp.bkt.clouddn.com/17-3-24/68164216-file_1490325466332_11060.png)
##### 补充一个，如果你想把结果保存为文件，又不想写代码 那么就用无所不能的 cmd 吧，通过 > 路径+文档名称 如我们这里 test.txt 在 E 盘根文件夹下，命令如下

``` cmd
phantomjs hello.js >E:\test.txt

```
![image](http://on792ofrp.bkt.clouddn.com/17-3-24/42824014-file_1490326430225_14f18.png)
##### 运行，可以看到已经存到文件里了
![image](http://on792ofrp.bkt.clouddn.com/17-3-24/98489690-file_1490326436738_118d3.png)
