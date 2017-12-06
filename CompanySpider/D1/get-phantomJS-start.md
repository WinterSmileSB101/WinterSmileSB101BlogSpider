---
title: get-phantomJS-start
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
> 版权声明：本文为 wintersmilesb101 -（个人独立博客– [http://wintersmilesb101.online](http://wintersmilesb101.online) 欢迎访问）博主原创文章，未经博主允许不得转载。##### 既然是入门，那我们就从人类的起源。。PhantomJS 来说起吧。
![image](http://on792ofrp.bkt.clouddn.com/17-3-24/90993504-file_1490317582237_67a4.png)

``` javascript
var page = require('webpage').create();
phantom.outputEncoding="gbk";//指定编码方式
page.open("http://news.163.com/", function(status) {
if ( status === "success" ) {
console.log(page.title);//输出网页标题
} else {
console.log("网页加载失败");
}
phantom.exit(0);//退出系统
});

```
![image](http://on792ofrp.bkt.clouddn.com/17-3-24/5757122-file_1490318527067_13804.png)
#####　好了我们已经跑的第一个　ＰｈａｎｔｏｍＪＳ程序了，其他的就是一些属性的介绍，[http://blog.csdn.net/mecho/article/details/45888465](http://blog.csdn.net/mecho/article/details/45888465)
