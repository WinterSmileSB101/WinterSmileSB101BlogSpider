---
title: node-spider-scend
date: 2017-03-23
date: 2017-03-24
categories: 
- 爬虫
- Node.js 爬虫
tags: - 爬虫
- Spider
- Node.js
- Json 字符串
- 动态网页
- 网易新闻
---
> 版权声明：本文为 wintersmilesb101 -（个人独立博客– [http://wintersmilesb101.online](http://wintersmilesb101.online) 欢迎访问）博主原创文章，未经博主允许不得转载。##### 上一篇中我们对百度首页进行了标题的爬取，本来打算这次直接对上次没有爬取到的推荐新闻进行爬取，谁知道网页加载出来没网页了，这是天要亡我大宋啊。。那我们直接去抓取网易新闻，进入网易新闻,我们要抓取的位置如下:
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/34448525-file_1490261201810_807e.png)
##### 首先来上爬取网站的测试
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/71601232-file_1490261572369_3333.png)
##### 这里可以看到我们的网络请求获取的数据并不为空，那么我们直接对网页的网络加载进行分析，红框的位置就是数据的请求
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/59803470-file_1490274042701_67ae.png)
##### 直接拖拽打开请求网址(先点击 header 然后就可以看到网址)
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/47264701-file_1490274230870_3177.png)
##### 打开页面如下
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/64554156-file_1490274698606_1257.png)
##### ,是不是很激动，这不就是数据嘛，还是 json 的，简直比获取网页源码还还解析，直接上代码

``` javascript
var request = require("request");
var cheerio = require("cheerio");
request('http://news.163.com/',function(err,result){
if(err){
console.log("错误："+err);
}
console.log(result.body);
})

```
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/74210596-file_1490261772161_113e7.png)

``` cmd
npm install superagent --save
npm install superagent-charset

```

``` javascript
const install = require('superagent-charset');
const request = require('superagent');
superagent = install(request);
superagent.get('http://news.163.com/').charset('gb2312').end(function(err,res) {
if(err) console.log(err);
console.log(res.text);
});

```
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/97516487-file_1490268273791_eb52.png)

``` cmd
npm install iconv-lite

```

``` javascript
var request = require('request');
var cheerio = require('cheerio');
var iconv = require('iconv-lite');
request.get({
url : 'http://temp.163.com/special/00804KVA/cm_yaowen.js?callback=data_callback',
encoding : null //让body 直接是buffer
}, function (err, response, body) {
//返回的body 直接就是buffer 了...
var buf =  iconv.decode(body, 'gb2312');
console.log(buf);
});

```
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/9069553-file_1490273522605_e993.png)
##### 终于可以开始进入正题了，我怕拉闸
##### 来解析网页，我们来分析分析要取到合适位置需要做些什么,这是个 json 字符串，结构如下所示

``` highlight
data(
[
{
title:'Node.js爬虫爬坑之路',
date:'2017-03',
athour:'wintersmilesb101',
blog:'wintersmilesb101.online'
}
]
)

```
##### 所以我们要做如下工作，先把外面的 data() 去掉，然后通过 JSON.parse(String) 把 json 字符串转换成 json 对象，然后我们就可以对变量直接进行操作了，是不是很方便
##### 代码如下，运行

``` javascript
var request = require('request');
var iconv = require('iconv-lite');
request.get({
url : 'http://temp.163.com/special/00804KVA/cm_yaowen.js?callback=data_callback',
encoding : null //让body 直接是buffer
}, function (err, response, body) {
//返回的body 直接就是buffer 了...
var buf =  iconv.decode(body, 'gb2312');
//去掉头部的 data_callback(
var str = buf.replace('data_callback(','');
//去掉尾部的 )
str = str.replace(')','');
//遍历输出数据，输出标题测试
var str1 = JSON.parse(str);
str1.forEach(function(s){
console.log(s.title);
});
});

```
##### 成功输出了！接着我们来补全我们的输出
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/72938976-file_1490278799901_124ee.png)
##### 修改后代码如下

``` javascript
var request = require('request');
var iconv = require('iconv-lite');
request.get({
url : 'http://temp.163.com/special/00804KVA/cm_yaowen.js?callback=data_callback',
encoding : null //让body 直接是buffer
}, function (err, response, body) {
//返回的body 直接就是buffer 了...
var buf =  iconv.decode(body, 'gb2312');
//去掉头部的 data_callback(
var str = buf.replace('data_callback(','');
//去掉尾部的 )
str = str.replace(')','');
var str1 = JSON.parse(str);
str1.forEach(function(s){
console.log('文章标题：'+s.title);
console.log('摘要：'s.digest);
console.log('文章链接：'+s.docurl);
console.log('内容链接：'+s.commenturl);
console.log('tienum：'+s.tienum);
console.log('tlastid：'+s.tlastid);
console.log('tlink：'+s.tlink);
console.log('标签：'+s.label);
console.log('时间：'+s.time);
console.log('新闻类别：'+s.newstype);
console.log('频道名称：'+s.channelname);
console.log('图片链接：'+s.imgurl);
});
});

```
##### 运行，大功告成，下次我们学习通过 pathomjs 来获取动态网页内容
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/35036394-file_1490278996843_1cd3.png)
