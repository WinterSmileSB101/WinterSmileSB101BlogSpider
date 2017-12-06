---
title: css-els
date: 2017-03-29
date: 2017-03-29
categories: 
- WEB
- 前端开发
- CSS
tags: - CSS
- 文字省略
---
> 版权声明：本文为 wintersmilesb101 -（个人独立博客– [http://wintersmilesb101.online](http://wintersmilesb101.online) 欢迎访问）博主转载文章，[原文地址](http://www.2cto.com/kf/201607/525572.html)。### 效果图
![image](http://www.2cto.com/uploadfile/Collfiles/20160712/20160712092250433.png)
### 上面的效果实现代码如下：

``` html
<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
<title></title>
<style type="text/css">
.inaline {
overflow: hidden;
white-space: nowrap;
text-overflow: ellipsis;
/*clip  修剪文本。*/
}

.intwoline {
display: -webkit-box !important;
overflow: hidden;
text-overflow: ellipsis;
word-break: break-all;
-webkit-box-orient: vertical;
-webkit-line-clamp: 3;
}
</style>
</head>

<body>
<p class="inaline">元素可提供相关页面的元信息（meta-information），比如针对搜索引擎和更新频度的描述和关键词。 标签位于文档的头部，不包含任何内容。 标签的属性定义了与文档相关联的名称/值对。</p>
<p style="width: 500px;border: 1px solid red;" class="intwoline">元素可提供相关页面的元信息（meta-information），比如针对搜索引擎和更新频度的描述和关键词。 标签位于文档的头部，不包含任何内容。 标签的属性定义了与文档相关联的名称/值对。元素可提供相关页面的元信息（meta-information），比如针对搜索引擎和更新频度的描述和关键词。 标签位于文档的头部，不包含任何内容。 标签的属性定义了与文档相关联的名称/值对。元素可提供相关页面的元信息（meta-information），比如针对搜索引擎和更新频度的描述和关键词。 标签位于文档的头部，不包含任何内容。 标签的属性定义了与文档相关联的名称/值对。元素可提供相关页面的元信息（meta-information），比如针对搜索引擎和更新频度的描述和关键词。 标签位于文档的头部，不包含任何内容。 标签的属性定义了与文档相关联的名称/值对。元素可提供相关页面的元信息（meta-information），比如针对搜索引擎和更新频度的描述和关键词。 标签位于文档的头部，不包含任何内容。 标签的属性定义了与文档相关联的名称/值对。元素可提供相关页面的元信息（meta-information），比如针对搜索引擎和更新频度的描述和关键词。 标签位于文档的头部，不包含任何内容。 标签的属性定义了与文档相关联的名称/值对。</p>
</body>
</html>

```
### 如果实现单行文本的溢出显示省略号同学们应该都知道用text-overflow:ellipsis属性来，当然还需要加宽度width属来兼容部分浏览。
##### 实现方法：

``` css
overflow:hidden;
text-overflow:ellipsis;
white-space:nowrap;

```
##### 效果如图：
![image](http://www.2cto.com/uploadfile/Collfiles/20160712/20160712092250434.png)
### 但是这个属性只支持单行文本的溢出显示省略号，如果我们要实现多行文本溢出显示省略号呢。
##### 接下来重点说一说多行文本溢出显示省略号，如下。

``` css
display:-webkit-box;
-webkit-box-orient:vertical;
-webkit-line-clamp:3;
overflow:hidden;

```
![image](http://www.2cto.com/uploadfile/Collfiles/20160712/20160712092250435.png)
##### 适用范围：
##### 因使用了WebKit的CSS扩展属性，该方法适用于WebKit浏览器及移动端；

``` plain
注：
-webkit-line-clamp用来限制在一个块元素显示的文本的行数。为了实现该效果，它需要组合其他的WebKit属性。常见结合属性：
display:-webkit-box;必须结合的属性，将对象作为弹性伸缩盒子模型显示。
-webkit-box-orient必须结合的属性，设置或检索伸缩盒对象的子元素的排列方式。

```

``` css
p{
position:relative;
line-height:20px;
max-height:40px;
overflow:hidden;}

p::after{
content:"...";
position:absolute;
bottom:0;
right:0;
padding-left:40px;
background:
-webkit-linear-gradient(left,transparent,#fff55%);
background:
-o-linear-gradient(right,transparent,#fff55%);
background:
-moz-linear-gradient(right,transparent,#fff55%);
background:
linear-gradient(toright,transparent,#fff55%);
}

```
##### 效果如下：
![image](http://www.2cto.com/uploadfile/Collfiles/20160712/20160712092250436.png)
##### 适用范围：
##### 该方法适用范围广，但文字未超出行的情况下也会出现省略号,可结合js优化该方法。

``` plain
注：

将height设置为line-height的整数倍，防止超出的文字露出。
给p::after添加渐变背景可避免文字只显示一半。
由于ie6-7不显示content内容，所以要添加标签兼容ie6-7（如：…）；兼容ie8需要将::after替换成:after。

```
![image](http://www.2cto.com/uploadfile/Collfiles/20160712/20160712092251437.png)
##### 文章点击进入详情：
##### 已知显示两行CSS：

``` css
.intwoline {
display: -webkit-box !important;
overflow: hidden;
text-overflow: ellipsis;
word-break: break-all;
-webkit-box-orient: vertical;
-webkit-line-clamp: 2;
}

```
##### 假设页面有3个:

``` html
<div class="color_lightBlack intwoline flag" style="border: 1px solid red;height: 40px;overflow: hidden;">
<p class="font14" style="font-size:14px;text-indent:28px;color:#111111;font-family:"">
1111掌众金融作为一家专注互联网消费金融的金融科技公司，掌众金融作为一家专注互联网消费金融的金融科技公司，掌众金融作为一家专注互联网消费金融的金融科技公司，掌众金融作为一家专注互联网消费金融的金融科技公司。
</p>
<p class="font14" style="font-size:14px;text-indent:28px;color:#111111;font-family:"">
2222掌众金融作为一家专注互联网消费金融的金融科技公司，掌众金融作为一家专注互联网消费金融的金融科技公司，掌众金融作为一家专注互联网消费金融的金融科技公司，掌众金融作为一家专注互联网消费金融的金融科技公司。
</p>
</div>

```
##### 添加 js

``` javascript
$(function() {
$(".flag").each(function(i) {
var str = '';
str = $(".flag:eq(" + i + ")").text();
$(".flag:eq(" + i + ")").empty().text(str);
})
});

```
### 为什么不用js 截取字符串，–》不知道屏幕宽度！！！！！！！！！！！
