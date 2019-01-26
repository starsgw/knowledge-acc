import hashlib

# 用于加密相关的操作，代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法

# MD5：
# def func_MD5(string):
#     hash=hashlib.md5()
#     hash.update(string.encode())
#     m=hash.hexdigest()
#     print(m)
#
# func_MD5("sgw")

# sha1:
# def func_sha1(string):
# #     hash=hashlib.sha1()
# #     hash.update(string.encode())
# #     m=hash.hexdigest()
# #     print(m)
# # func_sha1("sgw")

# ######## sha256 ########
def func_sha256(string):
    hash = hashlib.sha256()
    hash.update(string.encode())
    print(hash.hexdigest())
func_sha256("123")
# ######## sha384 ########
def func_sha384(string):
    hash = hashlib.sha384()
    hash.update(string.encode())
    print(hash.hexdigest())
func_sha384("123")
# ######## sha512 ########
def func_sha512(string):
    hash = hashlib.sha512()
    hash.update(string.encode())
    print(hash.hexdigest())

func_sha512("123")
'''
以上加密算法虽然厉害,但存在缺陷，可通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。
'''

def func_MD5_deep(string):
    hash=hashlib.md5(("sdfgdfsgsdf").encode())    #key加密
    hash.update(string.encode())
    m=hash.hexdigest()
    print(m)

func_MD5_deep("123")
