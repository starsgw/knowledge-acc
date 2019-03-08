#mkdir   makedirs

import os

path ="F:\\test\\test2"

try:
    os.mkdir(path)
    print("1:","创建成功")
except:
    print("2:","创建失败")
    try:
        os.makedirs(path)
        print("3:","创建成功")
    except:
        print("4:","创建失败")

# 通过上面的例子可以很好的理解，os.mkdir()只对路径的最后一级目录进行创建，
# 如果前几级目录不存在，会报错！
# 而os.makedirs()可以创建多级目录，如果路径的目录都不存在，都可以创建出来。

#补充：
os.getcwd()
# 返回当前进程的工作目录。
print("5:",os.getcwd())

os.listdir(path)
#返回指定路径下的文件和文件夹列表。
print("6:",os.listdir(path))#不给path参数则返回当前文件所在目录的所有文件名

os.walk(path)
#该函数可以得到一个三元tupple(dirpath, dirnames, filenames).
# 参数含义：
# dirpath：string，代表目录的路径；
# dirnames：list，包含了当前dirpath路径下所有的子目录名字（不包含目录路径）；
# filenames：list，包含了当前dirpath路径下所有的非目录子文件的名字（不包含目录路径）。
for root, dirs, files in os.walk(path):
        print(root) #当前目录路径
        print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件

#os.path模块常用方法补充:

path="D:/PyCharm 2018.3/daima/pachong/2018.11.30/os模块.py"

os.path.abspath(path)
print("7:",os.path.abspath("os模块.py"))
# 返回path规范化的绝对路径
#结果："D:/PyCharm 2018.3/daima/pachong/2018.11.30/os模块.py"

print("8:",os.path.split(path))
# 将path分割成目录和文件名二元组返回。
#结果：('D:/PyCharm 2018.3/daima/pachong/2018.11.30', 'os模块.py')

os.path.dirname(path)
# 语法：os.path.dirname(path)
# 功能：去掉最后一个目录名（或者文件名），返回目录/其实就是os.path.split(path)的第一个元素
print("9:",os.path.dirname(path))
#结果："D:/PyCharm 2018.3/daima/pachong/2018.11.30/os模块.py"
print("10:",os.path.dirname("D:/PyCharm 2018.3/daima/pachong/2018.11.30"))
#结果：D:/PyCharm 2018.3/daima/pachong

os.path.dirname(__file__)
print("11:",os.path.dirname(__file__))
#获取当前运行脚本的绝对路径
#结果:D:/PyCharm 2018.3/daima/pachong/2018.11.30

print("12:",os.path.basename(path))
#结果：os模块.py/
# 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素。
print("13:",os.path.basename("D:/PyCharm 2018.3/daima/pachong"))#这里pachong被当做文件处理了
#结果：pachong
# 所以应该这样：
print("14:",os.path.basename("D:/PyCharm 2018.3/daima/pachong/"))#无文件，结果返回空值

os.path.exists(path)
# 如果path存在，返回True；如果path不存在，返回False。
print("15:",os.path.exists("D:/PyCharm 2018.3/daima/"))
# 结果：True

os.path.isabs(path)
# 如果path是绝对路径，返回True。
print("16:",os.path.isabs(path))

os.path.isfile(path)
# 如果path是一个存在的文件，返回True。否则返回False。
print("17:",os.path.isfile("D:/PyCharm 2018.3/daima/"))
#结果：False

os.path.isdir(path)
# 如果path是一个存在的目录，则返回True。否则返回False。
print("18:",os.path.isdir(path))#目录后面有文件，结果返回False
print("19:",os.path.isdir("D:/PyCharm 2018.3/daima/"))#结果返回True

os.path.join("path1","path2","path3....")
# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略。
print("20:",os.path.join("D:","test","test2"))
#结果：D:test\test2
#由于第一个参数省略，所以需要改为：
print("21:",os.path.join("D:\\","test","test2"))


# 还有一些如下：

# os.path.commonprefix(list)
# 返回list中，所有path共有的最长的路径。
# >>> os.path.commonprefix(['/home/td','/home/td/ff','/home/td/fff'])
# '/home/td'

os.path.normpath(path)
# 规范化路径
# >>> os.path.normpath('c://windows\\System32\\../Temp/')
# 'c:\\windows\\Temp'

os.path.splitdrive(path)
# 返回（drivername，fpath）元组
# >>> os.path.splitdrive('c:\\windows')
# ('c:', '\\windows')

os.path.getsize(path)
# 返回path的文件的大小（字节）。
# >>> os.path.getsize('c:\\boot.ini')
# 299L

os.path.splitext(path)
# 分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作

os.path.getatime(path)
# 返回path所指向的文件或者目录的最后存取时间

os.path.getmtime(path)
# 返回path所指向的文件或者目录的最后修改时间