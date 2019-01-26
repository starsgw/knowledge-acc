from pymongo import MongoClient

# conn=MongoClient("mongodb://localhost:27017/")
# conn2=MongoClient('localhost',27017)  #mongoDb URI格式

# db=conn2.pythonndb#使用实例来访问数据库


#连接mongodb
conn =MongoClient("localhost",27017)
db=conn.test3#指定数据库名为test3，若没有则自动创建
my_set=db.test3_set#指定集合名为test3_set，若没有则自动创建
#注意：db和collection都是延时创建的，在添加Document时才真正创建

#增
# my_set.insert({"name":"sgw","age":"22"})#insert插入一个列表多条数据不用遍历，效率高， save需要遍历列表，一个个插入
# my_set.save({"name":"sgw","age":"22"})

# users=[{"name":"wl"},{"name":"shc"},{"neme":"wwj"},{"name":"wst"}]
# my_set.insert(users)
# my_set.save(users)

#查询全部，查找返回的对象集
# for i in my_set.find():
#     print(i)
#查询单个
# for i in my_set.find({"name":"wl"}):
#     print(i)
    #或
# print(my_set.find_one({"name":"wl"}))
#查找并修改：(修改后返回修改前的数据)
#find_one_and_updete({"name":"sgw"},{"$set":{"name":"wl"}})

#正则表达式：查询时，使用正则表达式作为限定条件，语法与JavaScript的正则表达式相同，{“x”:/[abc]/}
# print([i for i in my_set.find({"name":/[sgw]/})])    ????????????
# print([i for i in my_set.find({"name":{"$regex":".*sgw"}})])#name为匹配的键，".*sgw"为匹配的正则
# print([i for i in my_set.find({"age"})])

# print([i for i in my_set.find({"name":{"$ne":"sgw"}})])#获取除啦name为sgw以外的所有文档
# print([i for i in my_set.find({"name":{"$in":["shc"，"wl"]}})])#匹配在数组中的文档
# print([i for i in my_set.find({"name":{"$nin":["shc","wl"]}})])#匹配不在数组中的文档

#操作符$all与$in类似，不过$all要求所有属性都匹配，$in操作符值要求文档中的一个属性匹配即可：
# print([i for i in my_set.find({"name":{"$all":["shc","wl"]}})])

#在单个查询中可以使用$or操作符搜索多个表达式，它将返回满足其中任何一个条件的文档。与$in不同，$or允许同时指定键和值，而不是指定值：
# print([i for i in my_set.find({"$or":[{"name":"shc"},{"age":18}]})])


#改
# update命令格式：
# db.collection.update(criteria,objNew,upsert,multi)
# 参数说明：
# criteria：查询条件
# objNew：update对象和一些更新操作符
# upsert：如果不存在update的记录，是否插入objNew这个新的文档，true为插入，默认为false，不插入。
# multi：默认是false，只更新找到的第一条记录。如果为true，把按条件查询出来的记录全部更新。

# $inc修改器：将指定属性的值增加特定的步长，如果键不存在则创建它。
# set修改器：用来指定一个键的值，如果不存在则创建它。
# $push：数组修改器，如果指定的键存在，则向已有的数组末尾加入一个元素，键不存在则会创建一个新的数组。

# my_set.update({"name":"sgw"},{"$set":{"age":18}})
# my_set.update({"name":"wl"},{"$set":{"name":"wlhahaha"}})#前面数据用于查找的条件，后面则为修改后的数据

#批量添加某个没有的字段
# db.member.update(
#     {"is_auth" : {$exists : false}},#查找条件
#     {"$set" : {"new" : 0}},#新增字段
#     false,
#     true
# )

#删
# my_set.remove({"name":"sgw"})#删除匹配的所有数据

# id=my_set.find_one({"name":"sgw"})["_id"]#查找指定Id,然后进行删除
# my_set.remove(id)

# users=[{"name":"wlhahaha"},{"name":"shc"},{"neme":"wwj"},{"name":"wst"}]
# db.users.remove()#批量删除    ？？？？？？？？

#pop   ?????????????????????
#移除最后一个元素(-1为移除第一个)
# my_set.update({'name':"sgw"}, {'$pop':{'age':18}})
# for i in my_set.find({'name':"lisi"}):
#     print(i)
#输出：{'_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'age': 18, 'name': 'lisi', 'li': [1, 2, 3, 4, 4]}

#pull （按值移除）
#移除3
# my_set.update({'name':"lisi"}, {'$pop':{'li':3}})

#pullAll （移除全部符合条件的）
# my_set.update({'name':"lisi"}, {'$pullAll':{'li':[1,2,3]}})
# for i in my_set.find({'name':"lisi"}):
#     print(i)
#输出：{'name': 'lisi', '_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'li': [4, 4], 'age': 18}#pop
#移除最后一个元素(-1为移除第一个)
# my_set.update({'name':"lisi"}, {'$pop':{'li':1}})
# for i in my_set.find({'name':"lisi"}):
#     print(i)
#输出：{'_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'age': 18, 'name': 'lisi', 'li': [1, 2, 3, 4, 4]}

#pull （按值移除）
#移除3
# my_set.update({'name':"sgw"}, {'$pop':{'age':"22"}})

#pullAll （移除全部符合条件的）
# my_set.update({'name':"lisi"}, {'$pullAll':{'li':[1,2,3]}})
# for i in my_set.find({'name':"lisi"}):
#     print(i)
#输出：{'name': 'lisi', '_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'li': [4, 4], 'age': 18}
# ????????????????


#条件操作符
#  >   :$gt
# <   :$lt
# >+  :$gte
# <=  :￥lte

#例：查询集合中age大于25的所有记录
# for i in my_set.find({"age":{"$gt":10,"$lt":20}}):
#     print(i,"aaaa")

#在MongoDB中使用sort()方法对数据进行排序，sort()方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序，-1为降序。
# for i in my_set.find({"name":"sgw"}).sort([("age",1)]):
#     print(i)
#limit()方法用来读取指定数量的数据
#skip()方法用来跳过指定数量的数据
#下面表示跳过两条数据后读取6条
# for i in my_set.find().skip(2).limit(1):
#     print(i)
# skip(), limilt(), sort()三个放在一起执行的时候，执行的顺序是先 sort(), 然后是 skip()，最后是显示的 limit()。

#通过$slice获取的文档将只包含数组中特定范围的值。通过该操作符还可以获取结果中每页的n项数据，该特性通常被称为分页。
# 理论上，操作符$slice结合了limit()和skip()函数的功能；
# 不过，limit()和skip()无法作用于数组，而$slice可以。该操作符接受两个参数：第一个参数表示将要返回数据项的总数；
# 第二个参数是可选的，如果使用了该参数，那么第一个参数将用于定义偏移，第二个参数用于定义限制。参数limit可以使用负值。
# for i in my_set.find({"name":"sgw"},{"name":{"$slice":[2,2]}}):
#     print(i)

# mongodb命令：
# db.collections_name.ensureIndex({"url":1},{unique:true});
#设置唯一索引

# db.copyDatabase(fromdb, todb, fromhost, username, password)
# #从远程主机复制数据库到本地，或从本地复制数据库到远程主机

# db.getCollection('keywords_cn_tmpForCopy1').find().forEach(function(d){ db.getSiblingDB('Runoob')['key_cn'].insert(d); });
#在一个主机中从一个库中将一个集合复制一份到另一个集合


# 不同服务器之间集合的迁移：(cmd指令)
# 先进入到mongodb文件夹
# 下载到本地
# mongodump -h 192.168.8.211:27017 -c wenku_links -d baiduwenku -o E:\mongodb_data
# 拷贝到服务器
# mongoimport -h 192.168.2.112:27017 -d doc -c Sougou_pdf_url /file:D:\mongo\Sougou_pdf_url\Sougou_pdf_url.json。
