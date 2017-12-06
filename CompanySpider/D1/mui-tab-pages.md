---
title: mui-tab-pages
date: 2017-03-28
date: 2017-03-29
categories: 
- WEB
- 前端开发
- Hbuilder
- MUI
tags: - 前端开发
- 混合 APP
- MUI
- Hbuilder
- 多页面操作
- tab 导航
---
> 版权声明：本文为 wintersmilesb101 -（个人独立博客– [http://wintersmilesb101.online](http://wintersmilesb101.online) 欢迎访问）博主原创文章，未经博主允许不得转载。### 最近想入坑前端开发，也是为了开发 App 更快更接地气。在各种前端框架的纠结中我还是决定先入坑 MUI ，开坑不易，欢迎交流。
### OK，下面直接进入正题
### 我们今天来试试制作网易云 App 的 UI，界面如下：
![image](http://on792ofrp.bkt.clouddn.com/17-3-28/60486370-file_1490679058249_17b79.png)
### 那么就开始工作吧，首先下载 Hbulider，然后打开新建移动 App 选择 MUI 模板（不下载也可以，可以手动创建 MUI 项目，这里就不再赘述）。
### 然后打开 index.html,在 body 标签中添加如下代码

``` html
<!-- 主界面不动、菜单移动 -->
<!-- 侧滑导航根容器 -->
<div class="mui-off-canvas-wrap mui-draggable mui-slide-in">
<!-- 菜单容器 -->
<aside class="mui-off-canvas-left" id="offCanvasSide">
<div class="mui-scroll-wrapper">
<div class="mui-scroll">
<!-- 菜单具体展示内容 -->

</div>
</div>
</aside>
<!-- 主页面容器 -->
<div class="mui-inner-wrap">
<!-- 主页面标题 -->
<header class="mui-bar mui-bar-nav" style="margin-top: 10px;background-color: #FF0000;">
<a class="mui-icon mui-action-menu mui-icon-bars mui-pull-left" href="#offCanvasSide"></a>
<div class=" mui-segmented-control" style="margin:-4px 100px 0px 100px;align-content: center;
align-self: center; ">
<a class="mui-control-item mui-active" id="mine" style="background-color: #FF0000; color: #cococo;">我的</a>
<a class="mui-control-item" id="discory" style="background-color: #FF0000;">发现</a>
<a class="mui-control-item" id="dynamic" style="background-color: #FF0000;">动态</a>
</div>
</header>
<div class="mui-off-canvas-backdrop"></div>

```
##### 其中我们的侧滑栏可以直接通过联想代码块快速实现触发语句

``` html
moffcanvas

```
##### 其实你不用打完就会出现可以选择的代码块，对应的代码块都有作用解释，这样可以很快的选择到需要的代码块。上述代码有几个注意的地方：

``` html
ios:
打开应用的manifest.json文件，切换到代码视图，在plus -> distribute -> apple 下添加UIReserveStatusbarOffset节点并设置值为false。
注意：
1. 真机运行不生效，需提交App云端打包后才生效；
2. 此功能仅在iOS7及以上系统有效。
android:
打开应用的manifest.json文件，切换到代码视图，在plus -> distribute -> google 下添加ImmersedStatusbar节点并设置值为true。
注意：
1. 真机运行不生效，需提交App云端打包后才生效；
2. 此功能仅在Android4.4及以上系统有效。

配置系统状态栏样式

iOS平台可支持对系统状态栏样式的配置，在应用manifest.json文件的plus->distribute->apple下添加UIStatusBarStyle进行控制，默认值为"UIStatusBarStyleDefault"。

UIStatusBarStyleDefault  默认样式，iOS6及以下系统状态栏为黑底白字，iOS7及以上系统用于定义系统状态栏上文字颜色为黑字（适用于浅色背景）

UIStatusBarStyleBlackOpaque  深色背景色样式，iOS6及以下系统状态栏为黑底白字，iOS7及以上系统用于定义系统状态栏上文字颜色为白色（适用于深色背景）

UIStatusBarStyleBlackTranslucent  iOS6及以下系统在启动界面为灰底白字，iOS7及以上系统与UIStatusBarStyleBlackOpaque效果一样

设置系统状态栏背景颜色（iOS7及以上生效）

iOS平台可支持对系统状态栏背景颜色的配置，在应用manifest.json文件的plus->distribute->apple下添加StatusBarBackground进行控制：
值为字符串类型，格式为"#RRGGBB"格式，如红色为"#FF0000"；默认值为白色。

App云端打包设置系统状态栏背景颜色操作方式

双击应用的manifest.json文件，切换到“代码视图”，在apple节点下添加StatusBarBackground节点.

```
##### 在 MUI 中有一个创建子页面的方法

``` javascript
/*在mobile app开发过程中，经常遇到卡头卡尾的页面，此时若使用局部滚动，在android手机上会出现滚动不流畅的问题； mui的解决思路是：将需要滚动的区域通过单独的webview实现，完全使用原生滚动。具体做法则是：将目标页面分解为主页面和内容页面，主页面显示卡头卡尾区域，比如顶部导航、底部选项卡等；内容页面显示具体需要滚动的内容，然后在主页面中调用mui.init方法初始化内容页面。*/

mui.init({
subpages:[{
url:your-subpage-url,//子页面HTML地址，支持本地地址和网络地址
id:your-subpage-id,//子页面标志
styles:{
top:subpage-top-position,//子页面顶部位置
bottom:subpage-bottom-position,//子页面底部位置
width:subpage-width,//子页面宽度，默认为100%
height:subpage-height,//子页面高度，默认为100%
......
},
extras:{}//额外扩展参数
}]
});
/*参数说明：styles表示窗口属性，参考5+规范中的WebviewStyle；特别注意，height和width两个属性,即使不设置，也默认按100%计算；因此若设置了top值为非"0px"的情况，建议同时设置bottom值，否则5+ runtime根据高度100%计算，可能会造成页面真实底部位置超出屏幕范围的情况；left、right同理。*/

```
##### 可以看到我们可以通过上述方法创建子页面实现分页，但是这只是一个页面，那么要怎么实现多页面的切换呢？这里就要引入 H5 webView相关的操作了，关于 H5 webview 的相关 API 可以看这里 H5 webview API，我们这里用到的是 getWebviewById,他会返回一个 WebviewObject窗口对象 我们就在这个对象上做文章。下面来书写 JS 代码：

``` javascript
<script type="text/javascript" charset="utf-8">

mui.plusReady(function(){
console.log("当前页面URL："+plus.webview.currentWebview().getURL());
//给标签为 mine 的元素（也就是我们的我的 tab ）添加 tap 事件，这里由于 click 的延迟太高，故用 tap 事件。
document.getElementById("mine").addEventListener('tap',function(){
//获取到当前的 webview 根据标签也就是下面定义的子页面 id
var cur = plus.webview.getWebviewById("contentHtml");
//判断是否是此页面
if(cur.getURL()!="htmlFile/mine.html")
{
//不是就要切换页面为当前 tab 是指向的页面
console.log("显示我的");
cur.loadURL("htmlFile/mine.html")
}
});

document.getElementById("discory").addEventListener('tap',function(){
var cur = plus.webview.getWebviewById("contentHtml");
if(cur.getURL()!="htmlFile/discory.html")
{
console.log("显示我的");
cur.loadURL("htmlFile/discory.html")
}
});

document.getElementById("dynamic").addEventListener('tap',function(){
var cur = plus.webview.getWebviewById("contentHtml");
if(cur.getURL()!="htmlFile/dynamic.html")
{
console.log("显示我的");
cur.loadURL("htmlFile/dynamic.html")
}
});
});
//MUI 的初始化，添加子页面（默认页面是 “我的” 界面，这里的子页面 id 就要被用于以后 tab 点击事件中获取 webview 的 id，特别），
mui.init({
subpages:[
{
url:'htmlFile/mine.html',
id:'contentHtml',
styles:{
top:'55px'
}
}
]
});
</script>

```
##### 对应的要注意的地方以及解释上面代码里已经说的很清楚了，至于其他的 3 个页面，我是另外写好的，你们也要写出页面，url 中填写你们要跳转的页面的地址就好了（网络地址或者本地地址），这里我就不说其他页面怎么建立了
##### 运行如下，仔细看就能发现一个问题，我们列表的最下面一项没有显示出来，也就是说页面没有完全显示出来，
![image](http://on792ofrp.bkt.clouddn.com/17-3-28/1993638-file_1490681679787_3dd1.gif)
##### 解决方法：在创建子页面的时候我们设置了top 的话就要也设置 bottom 否者会导致页面显示不完全！（仔细看看前面官方文档就会发现，这就是不认真看文档的锅），下面修改 jS 代码：

``` javascript
mui.init({
subpages:[
{
url:'htmlFile/mine.html',
id:'contentHtml',
styles:{
top:'55px',
bottom:'0px'
}
}
]
});

```
##### 然后保存，最好重新编译一次（这种更新不知道为什么我的如果不重新编译就不会出现正确的效果），停止调试，再开始调试，结果如下( 多 tab 页面的实时切换就完成了)：
![image](http://on792ofrp.bkt.clouddn.com/17-3-28/49375012-file_1490682072759_b4ea.gif)
### 已知问题，侧边栏会被子页面覆盖，目前想法是通过 zindex 调整，但是试过无用。
