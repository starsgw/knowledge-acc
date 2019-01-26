#xpath的使用
import urllib.request
from lxml import etree

wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
                 <li class="item-1 item-0" name="item"><a href="link4.html">last item</a></li>
             </ul>
         </div>
        """
html=etree.HTML(wb_data)#创建html对象
# html=etree.parse('./test.html',etree.HTMLParser())#解析本地html文档
result=etree.tostring(html)#补全啦残缺的标签
web_data2=result.decode("utf-8")
# print(web_data2)

html=etree.HTML(web_data2)
# print(i for i in html.xpath("/html/body/div/ul/li/a"))#选取a节点
# print(html.xpath("//*"))#所有节点
#
# print(html.xpath("//li/a"))#两种不同的写法，结果相同，由特征来确定位置
# print(html.xpath("//ul//a"))

# print(html.xpath("//a[@href='link1.html']/../@class"))#获取href属性为link1.html的父节点的class
# print(html.xpath("//a[@href='link2.html']/parent::*/@class"))#通过parent::来选取父节点属性
# print(html.xpath("//li/a/@href"))#选取节点属性

# print(html.xpath("//li[@class='item-0']"))#选取某个属性
# print(html.xpath("//li[contains(@class,'item-0')]"))#若节点含有多个属性，则需要使用contains()方法，第一个参数传入属性名称，第二个属性传入属性值，若此属性包含所传入的属性值，就可以匹配
# print(html.xpath("//li[contains(@class,'item-0') and @name='item']"))#同时选取多个属性进行匹配，使用and连接，类似的还有or...

# print(html.xpath("//li[@class='item-1']/text()"))#无结果
# print(html.xpath("//li[@class='item-0']/text()"))#这个却有结果为['\n  ']，这是因为item-0的li标签在修复后有的li标签换行，会有换行符
# print(html.xpath("//li[@class='item-0']//text()"))#此时选取的内部文本为['first item', 'fifth item', '\n   ']，所以在选取时需要选取正确的标签，否则会夹杂不需要的文本
# print(html.xpath("//li[@class='item-0']/a/text()"))#选取a标签内的文本

# print(html.xpath("//li[1]/a/text()"))#按序选择节点，第一个节点下标为1，
# print(html.xpath("//li[last()]/a/text()"))#使用last()选择最后一个节点
# print(html.xpath("//li[last()-1]/a/text()"))#使用last()-1选择倒数第二个节点
# print(html.xpath("//li[position()<3]/a/text()"))#使用position()选取位置小于3的节点
#xpath提供100多种方法

# print(html.xpath("//a[@href='link2.html']/ancestor::*"))#调用ancestor轴获取祖先节点
# print(html.xpath("//li/attribute::*"))#获取所有属性值
# #.....

# 获取某个节点下的所有文本（作为一个整体）：
# print(节点.xpath('string(.)').strip())

#bs4的使用
from bs4 import BeautifulSoup

html2 = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story<span>test</span><p>test</p></b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup=BeautifulSoup(html2,'lxml')#初始化Beautiful Soup(使用xlml解析器)
#bs4支持的解析器有：html.parser/lxml/xml/html5lib
# print(soup.prettify())#使用prettify()方法可以将要解析的字符串以标准的缩进格式输出，但是修复是在初始化#在初始化时，就会将原html中的没有闭合的节点自动修复
# print(type(soup.title))#经过选择器选择后的后得到的结果都是Tag类型，Tag具有一些属性，如string
print(soup.title.string)#输出某个节点的文本内容
# print(soup.p.attrs)#返回的是字典形式/
#
# 注意：这里的p节点是第一个节点，获取的属性也是第一个节点的

# print(soup.p.attrs['name'])#获取name属性，就像从字典里获取键值
# print(soup.p['name'])#也可以直接从节点中获取属性
# print(soup.p['class'])#返回的列表,注意：name属性的值是唯一的，返回的是单个字符串，而class属性一个节点可能含有多个值，返回的是一个列表
# print(soup.p.contents)#返回所有直接子节点的列表，不会单独的返回子孙节点
# print(soup.p.children)#children:返回生成器类型的直接子节点的,需要用循环输出
# for i,child in enumerate(soup.p.children):
#     print(i,child)
# print(soup.p.descendants)#descendants:返回生成器类型的子孙节点
# for i,child in enumerate(soup.p.descendants): #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
#     print(i,child)

# print(soup.p.parent)#parent:获取元素的直接父节点。/第一个p节点的父节点是body,所以结果就是body节点及其内部的内容
# print(soup.p.parents)#parents:获取元素的祖先节点。返回生成器类型。

# print(soup.a.next_sibling)#返回下一个兄弟节点的text
# print(soup.a.previous_sibling)#返回上一个兄弟节点的text
# print(soup.a.next_sibling)#返回后面的所有兄弟节点的生成器
# print(soup.a.previous_sibling)#返回前面的所有兄弟节点的生成器

# print(soup.find_all(name="a"))#返回节点名为a的所有节点的列表
# print(soup.find_all(attrs="title"))#查询属性为title的节点，返回列表
# print(soup.find_all(attrs={'id':'link1'}))#查询id为link1的节点，返回列表
import re
print(soup.find_all(text=re.compile('story')))#结果返回所有匹配正则表达式额节点文本组成的列表
# print(soup.find(name="p"))#返回单个元素，也就是第一个匹配的元素/其他和find_all完全一样

#此外还有find_parents()/find_parent//find_next_siblings()...


# print(soup.select('p')[0])#使用css选择器
# print(soup.select('.title'))
# print(soup.select('#link1'))

# print(soup.select('p')[0]["class"])#获取属性
# print(soup.select('p')[0].get_text())#获取标签内的所有文本，并拼接
# print(soup.select('p span')[0].string)#需要定位到文本所在的节点，否则无法输出
