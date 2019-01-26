from pyquery import PyQuery as pq
import requests

html = '''<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item <a>test</a> </span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul></div>'''

doc=pq(html)#1.字符串初始化
# print(doc("li"))


#URL初始化
# doc2=pq(url="https://www.baidu.com/",encoding="utf-8")#2.url初始化
#PyQuery这个对象会先请求这个url,然后用得到的html内容完成初始化
# print(doc2("title"))
#相当于：

# doc3=pq(requests.get("https://www.baidu.com/").text)#乱码
# doc31=pq(requests.get("https://www.baidu.com/").content)
# print(doc3)
# print(doc31)
# print(doc31("title"))

#文件初始化(解析本地文件)
# # doc4=pq(filename="demo.html",encoding="utf-8")
# with open("./demo.html",encoding="utf-8") as f:
#     content=f.read()
#     # print(content)
# doc4=pq(content)
# print(doc4("title"))

#基本css选择器
# print(doc(".item-0 .bold a"))

#4.查找节点
#find（）：查找符合的节点及其所以子孙节点
lis=doc.find('.item-0')
print("lis",lis)
span=doc.find('span')
print("span",span)

#children（）：查找子节点
lis2=doc.children('span')
print("lis2",lis2)


