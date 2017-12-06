---
title: node-spider-first
date: 2017-03-23
date: 2017-03-24
categories: 
- 爬虫
- Node.js 爬虫
tags: - 爬虫
- Spider
- Node.js
- 静态网页
---
> 版权声明：本文为 wintersmilesb101 -（个人独立博客– [http://wintersmilesb101.online](http://wintersmilesb101.online) 欢迎访问）博主原创文章，未经博主允许不得转载。##### 以上问题我们现在即将使用的 Node.js 全部是优势！
##### 同样，Node.js 也有劣势，Node.js 是单线异步，这样很容易导致爬取请求发起顺序和结果返回顺序不一致，因此我们需要添加上请求序列号，处理完的再重新排序来实现结果与请求一致。还有，Node.js 毕竟是前端，数据的处理相较而言要差的多，但是作为网站数据爬取绝对够了。废话不多说，下面进入 Node.js 爬虫,
##### Node.js 爬虫步骤

``` cmd
E:
cd E:\adt-bundle-windows-x86_64-20131030\Nodejs\nests_Dataget
npm init

```
- name - 包名。
- version - 包的版本号。
- description - 包的描述。
- homepage - 包的官网 url 。
- author - 包的作者姓名。
- contributors - 包的其他贡献者姓名。
- dependencies - 依赖包列表。如果依赖包没有安装，npm 会自动将依赖包安装在 node_module 目录下。
- repository - 包代码存放的地方的类型，可以是 git 或 svn，git 可在 Github 上。也就是你 Git 的仓库地址
- main - main 字段是一个模块ID，它是一个指向你程序的主要项目。就是说，如果你包的名字叫 express，然后用户安装它，然后require(“express”)。
- keywords - 关键字输入了 npm init 之后会依次出现下面的询问

``` cmd
$ npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg> --save` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
name: (node_modules) runoob                   # 模块名
version: (1.0.0) #模块版本
description: Node.js 测试模块(www.runoob.com)  # 描述
entry point: (index.js)
test command: make test
git repository: https://github.com/runoob/runoob.git  # Github 地址
keywords: #关键字
author: #作者
license: (ISC) #许可类型
About to write to ……/node_modules/package.json:      # 生成地址

{
"name": "runoob",
"version": "1.0.0",
"description": "Node.js 测试模块(www.runoob.com)",
……
}
Is this ok? (yes) yes

```
request，跟python里request功能一样。它的功能就是建立起对目标网页的链接，并返回相应的数据。是我们做爬虫的重要一步，没有数据我们去哪里爬？
cheerio的功能是用来操作 dom 元素的，他可以把 request 返回来的数据转换成可供 dom 操作的数据，更重要的 cheerio 的 api 跟 jquery 一样，用$来选取对应的dom结点，这样就可以想取啥就取啥，感谢强大的 DOM安装命令如下
``` cmd
npm install request --save
npm install cheerio

```
##### 界面如下
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/51169339-file_1490253009287_7683.png)
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/3449173-file_1490253051949_ceb0.png)
##### 4.接下来我们终于可以开始操作我们的 js 代码了

``` javascript
var request = require("request");
var cheerio = require("cheerio");

```

``` javascript
request('https://www.baidu.com/',function(err,result){
if(err){
console.log("错误："+err);
return;
}
console.log(result.body);
})

```
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/25028822-file_1490253074161_fd0b.png)
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/25327140-file_1490256714694_2dd2.png)

``` javascript
//把 html 装载到 cheerio 中
var $ = cheerio.load(result.body);
//通过 DOM 抓取网页数据
console.log($('title').text());

```
![image](http://on792ofrp.bkt.clouddn.com/17-3-23/95571980-file_1490256919828_17e6a.png)
