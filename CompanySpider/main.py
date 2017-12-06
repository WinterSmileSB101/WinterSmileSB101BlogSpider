import urllib
import urllib.request as req
from bs4 import BeautifulSoup
import codecs
import os
import bs4
filePath = r"D:/GIT/Blog/WinterSmileSB101/source/_posts/old/"
url = "http://wintersmilesb101.online/"

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# 设置代理 IP，http 不行，使用 https
proxy = req.ProxyHandler({'https': 's1firewall:8080'})
auth = req.HTTPBasicAuthHandler()
# 构造 opener
opener = req.build_opener(proxy, auth, req.HTTPHandler)
# 添加 header
opener.addheaders = [('User-Agent', user_agent)]
# 安装 opener
req.install_opener(opener)
# 打开链接
conn = req.urlopen(url)
# 以 utf-8 编码获取网页内容
content = conn.read().decode('utf-8')
# 输出
# print(content)

# 生成 soup 对象，准备解析 html
soup = BeautifulSoup(content,'lxml')

# 获取页面数量
spans = soup.select('span.space')

pageHref = spans[spans.__len__()-1].nextSibling['href']
# get total num
pageNum = int(pageHref.split('/')[2])
print(pageNum)

# get other page
# urlBase = "http://wintersmilesb101.online/page/"
# index = 1
# while index <= pageNum:
#     # 索引大于 1 的时候需要重新指定 url
#     if index > 1:
#         url = urlBase+str(index)
#         print(url)
#         print('发送 页面网络请求 : '+url)
#         # 打开链接
#         conn = req.urlopen(url)
#         # 以 utf-8 编码获取网页内容
#         content = conn.read().decode('utf-8')
#         soup = BeautifulSoup(content, "lxml")
#
#     # 获取文章 list
#     articles = soup.find_all('article')
#
#     # 处理每篇文章
#     for article in articles:
#         # 获取创建时间
#         createTime = article.find('time', title="创建于").text.strip()
#         # 获取创建时间
#         updateTime = article.find('time', title="更新于").text.strip()
#         # 获取分类
#         categoies = article.find_all('a', attrs = {'itemprop': "url", 'rel': "index"})
#
#         # 分类的 url，Name
#         categoryUrl = ''
#         categoryName = ''
#         for category in categoies:
#             #print(category)
#             categoryUrl += category['href']+','
#             #print(categoryUrl)
#             categoryName += category.text.strip()+','
#             #print(categoryName)
#         categoryUrl = categoryUrl[0:categoryUrl.__len__()-1]
#         categoryName = categoryName[0:categoryName.__len__() - 1]
#         # 获取正文
#         urlMain = ''
#         link = article.link['href']
#         articleTitle = link.split('/')[link.split('/').__len__()-2]
#         # print(articleTitle)
#         # 转换中文 url 编码
#         urlMain = urllib.request.quote(link)
#         # 把多余的转换 : ==> %3A ，还原
#         urlMain = urlMain.replace('%3A', ':')
#         # print(urlMain)
#         print('发送 文章网络请求')
#         response = req.urlopen(urlMain)
#         mainContent = response.read().decode('utf-8')
#         # output content of page
#         # print(mainContent)
#         mainSoup = BeautifulSoup(mainContent,'lxml')
#         body = mainSoup.find('div', itemprop="articleBody")
#
#         blockquote = body.blockquote
#         if blockquote != None:
#             blockquoteText = blockquote.p.text
#             # print(blockquote.p)
#             extenalUrl = None
#             mineUrl = blockquote.p.a['href']
#             if blockquote.p.find('a', rel="external"):
#                 extenalUrl = blockquote.p.find('a', rel="external")['href']
#             # print(extenalUrl)
#             # 把其中的链接替换为 md 语法
#             if extenalUrl:
#                 blockquoteText = blockquoteText.replace("原文地址","[原文地址]("+extenalUrl+")")
#
#             blockquoteText = blockquoteText.replace(mineUrl,"["+mineUrl+"]("+mineUrl+")")
#         # 获取标签
#         tags = mainSoup.find_all('a', rel='tag')
#         # print(tags)
#         # 写入 md 文件
#         # 判断路径是否存在
#         if not os.path.exists(filePath + str(index)+'/'):
#             os.makedirs(filePath + str(index)+'/')
#         file = codecs.open(filePath + str(index)+'/'+articleTitle+'.md', "w", encoding='utf8')  # 指定文件的编码格式
#
#         # 写入前置申明
#         file.write('---\n')
#         file.write("title: "+articleTitle+'\n')
#         file.write("date: "+createTime+'\n')
#         file.write("date: " + updateTime+'\n')
#         file.write("categories: "+'\n')
#         for category in categoryName.split(','):
#             file.writelines('- '+category+'\n')
#         file.writelines("tags: ")
#         for tag in tags:
#             tag = tag.text.replace('# ', '')
#             file.writelines('- ' + tag+'\n')
#         file.writelines('---'+'\n')
#         # 写入引用块
#         if blockquote != None:
#             file.writelines('> '+blockquoteText)
#         # 遍历正文块，写入文件,注意遍历文档树的时候 next_sibling 是紧紧接着的，比如这里是 \n,所以需要两个
#         # print(blockquote.next_sibling.next_sibling)
#
#         for nextTag in body.children:
#             # print(nextTag)
#             # print(type(nextTag))
#             if type(nextTag) == bs4.element.NavigableString:
#                 continue
#             tagName = ''
#             codeType = ''
#             codeStart = ''
#             codeEnd = ''
#             tagContent = nextTag.text.strip()
#             if nextTag.name == 'h1':
#                 tagName = '# '
#                 file.write(tagName + tagContent + '\n')
#                 continue
#             if nextTag.name == 'h2':
#                 tagName = '## '
#                 file.write(tagName + tagContent + '\n')
#                 continue
#             if nextTag.name == 'h3':
#                 tagName = '### '
#                 file.write(tagName + tagContent + '\n')
#                 continue
#             if nextTag.name == 'h4':
#                 tagName = '##### '
#                 file.write(tagName + tagContent + '\n')
#                 continue
#             # 代码块
#             if nextTag.select('figure').__len__() > 0 or nextTag.name == 'figure':
#                 # 如果 select 的 length 大于 0 则表示这个元素是 包含 figure 的元素
#                 if nextTag.select('figure').__len__() > 0:
#                     nextTag = nextTag.select('figure')[0]
#
#                 codeType = nextTag['class'][nextTag['class'].__len__() - 1] + '\n'
#                 codeStart = '``` '
#                 codeEnd = '```\n'
#                 codeLine = ''
#                 lineNumber = nextTag.table.tr.find('td', attrs={'class': 'gutter'}).text
#                 code = nextTag.table.tr.find('td', attrs={'class': 'code'}).text
#                 tagContent = tagContent.replace(lineNumber, '').replace(code, '')
#                 # print(lineNumber)
#                 # print(code)
#                 # print(tagContent)
#                 for line in nextTag.table.tr.find('td', attrs={'class' : 'code'}).find_all('div'):
#                     codeLine += line.text.strip()+'\n'
#                 file.write(tagContent+'\n')
#                 file.write(codeStart + codeType + codeLine + '\n' + codeEnd)
#                 continue
#
#             # 无序列表
#             if nextTag.name == 'ul':
#                 for li in nextTag.find_all('li'):
#                     file.write('- ' + li.text.strip() + '\n')
#                     continue
#             # 有序列表
#             if nextTag.name == 'ol':
#                 olIndex = 1
#                 for li in nextTag.find_all('li'):
#                     file.write(olIndex + '. ' + li.text.strip() + '\n')
#                     olIndex += 1
#                 continue
#             if nextTag.name == 'p':
#                 # 为空表示是图片
#                 tagContent = nextTag.text.strip()
#                 if tagContent == '':
#                     file.write("![image](" + nextTag.find('img')['src'] + ")\n")
#                     continue
#                 else:
#                     links = nextTag.find_all('a')
#                     for link in links:
#                         tagContent = tagContent.replace(link.text, "[" + link['href'] + "](" + link['href'] + ")")
#                     file.write(tagContent + '\n')
#                     continue
#         file.close()
#     index = index+1

# 读取特殊页面并且存入文件（代码冗余，日后重构代码）
aboutUrl = url+'about'
# 打开链接
conn = req.urlopen(aboutUrl)
# 以 utf-8 编码获取网页内容
content = conn.read().decode('utf-8')
# 输出
# print(content)

# 生成 soup 对象，准备解析 html
soup = BeautifulSoup(content,'lxml')

# 判断路径是否存在
if not os.path.exists(filePath+'about/'):
    os.makedirs(filePath+'about/')
file = codecs.open(filePath+'about/简历.md', "w", encoding='utf8')  # 指定文件的编码格式

body = soup.body.main.div.div.div.div
# print(body)
for nextTag in body.children:
    # print(nextTag)
    # print(type(nextTag))
    if type(nextTag) == bs4.element.NavigableString:
        continue
    tagName = ''
    codeType = ''
    codeStart = ''
    codeEnd = ''
    tagContent = nextTag.text.strip()
    if nextTag.name == 'h1':
        tagName = '# '
        file.write(tagName + tagContent + '\n')
        continue
    if nextTag.name == 'h2':
        tagName = '## '
        file.write(tagName + tagContent + '\n')
        continue
    if nextTag.name == 'h3':
        tagName = '### '
        file.write(tagName + tagContent + '\n')
        continue
    if nextTag.name == 'h4':
        tagName = '##### '
        file.write(tagName + tagContent + '\n')
        continue
    # 代码块
    if nextTag.select('figure').__len__() > 0 or nextTag.name == 'figure':
        # 如果 select 的 length 大于 0 则表示这个元素是 包含 figure 的元素
        if nextTag.select('figure').__len__() > 0:
            nextTag = nextTag.select('figure')[0]

        codeType = nextTag['class'][nextTag['class'].__len__() - 1] + '\n'
        codeStart = '``` '
        codeEnd = '```\n'
        codeLine = ''
        lineNumber = nextTag.table.tr.find('td', attrs={'class': 'gutter'}).text
        code = nextTag.table.tr.find('td', attrs={'class': 'code'}).text
        tagContent = tagContent.replace(lineNumber, '').replace(code, '')
        # print(lineNumber)
        # print(code)
        # print(tagContent)
        for line in nextTag.table.tr.find('td', attrs={'class' : 'code'}).find_all('div'):
            codeLine += line.text.strip()+'\n'
        file.write(tagContent+'\n')
        file.write(codeStart + codeType + codeLine + '\n' + codeEnd)
        continue

    # 无序列表
    if nextTag.name == 'ul':
        for li in nextTag.find_all('li'):
            file.write('- ' + li.text.strip() + '\n')
            continue
    # 有序列表
    if nextTag.name == 'ol':
        olIndex = 1
        for li in nextTag.find_all('li'):
            file.write(olIndex + '. ' + li.text.strip() + '\n')
            olIndex += 1
        continue
    if nextTag.name == 'p':
        # 为空表示是图片
        tagContent = nextTag.text.strip()
        if tagContent == '':
            file.write("![image](" + nextTag.find('img')['src'] + ")\n")
            continue
        else:
            links = nextTag.find_all('a')
            for link in links:
                tagContent = tagContent.replace(link.text, "[" + link['href'] + "](" + link['href'] + ")")
            file.write(tagContent + '\n')
            continue
file.close()
print('写入完成')