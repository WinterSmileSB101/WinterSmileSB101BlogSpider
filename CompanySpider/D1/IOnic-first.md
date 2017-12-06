---
title: IOnic-first
date: 2017-03-27
date: 2017-03-27
categories: 
- WEB
- 前端开发
- IOnic AngularJS
tags: - IOnic
- 前端开发
- 混合 APP
- AngularJS
- cordova
---
> 版权声明：本文为 wintersmilesb101 -（个人独立博客– [http://wintersmilesb101.online](http://wintersmilesb101.online) 欢迎访问）博主原创文章，未经博主允许不得转载。### 今天是为了记录几个使用 IOnic，准确的说应该是安装 cordova 的时候的一个小坑，
##### 安装语句

``` cmd
$ npm install -g cordova ionic

```

``` cmd
sudo npm install -g cordova ionic

```
##### 但是在你安装完成之后使用 IOnic 的时候，他就会提示你如下问题：
![image](http://on792ofrp.bkt.clouddn.com/17-3-27/35147767-file_1490614494677_133f0.png)
##### 意思是你安装的 cordova 不是高版本的，需要安装高版本的，但是我们安装的时候一起安装了的啊，莫非他安装的不是最新版？不不，安装的是最新版，但是不是稳定版的，所以这里会提示这个错误，解决方式，输入如下代码：

``` cmd
$ npm install -g cordova@6.0.0

```
### 问题解决，最终如下：
![image](http://on792ofrp.bkt.clouddn.com/17-3-27/93612916-file_1490614777045_99b.png)
## 问题2：：使用

``` cmd
$ ionic start myApp tabs

```
## 或者

``` cmd
ionic start app --v2

```
## 会出现如下错误

``` cmd
Error with start undefined
Error Initializing app: There was an error with the spawned command: npminstall
There was an error with the spawned command: npminstall

```
## 解决办法，这个因该是由于那堵那啥的问题
### 1.VPN
### 2.
##### 1.npm install -g cnpm
##### 2.ionic start myApp –v2 –skip-npm (表示跳过 npm install package)
##### 3.进入 myApp   执行 cnpm install –save
### 3.用cnpm 代替npm 成为全局变量
##### 1.npm install -g cnpm –registry=https://registry.npm.taobao.org（淘宝镜像下载cnpm）
##### 2.npm config set registry=https://registry.npm.taobao.org(修改npm配置换源)3.输入 npm config list  可以查看..npmrc 是否修改正确或者nano ~/.npmrc   //打开配置文件registry =https://registry.npm.taobao.org   //写入配置文件
##### 3.然后正常执行 即可（注意权限问题）
