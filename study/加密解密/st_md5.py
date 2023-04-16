from hashlib import md5, sha1, sha224, sha256, sha384 # 都是一样的使用方法

def demo01():
    """_summary_
    普通MD5算法，可能通过穷举法进行破解
    """
    obj = md5()
    obj.update('alex'.encode('utf-8'))
    # obj.update('ceshi'.encode('utf-8'))   # 可以添加多个被加密的内容

    bs = obj.hexdigest()

    print(bs)       # 输出32位小写哈希值 534b44a19bf18d20b71ecc4eb77c572f
    
def demo02():
    """_summary_
    加掩之后的MD5算法，很难被破解
    """
    salt = b'suibianxiedianshemo'
    obj = md5(salt)
    obj.update('alex'.encode('utf-8'))
    bs = obj.hexdigest()
    print(bs)       # 输出32位小写哈希值 5156a6b29c3cabc40cf72ec4d50985ed
    
def demo03():
    """_summary_
    针对文件进行MD5运算
    """
    salt = b'suibianxiedianshemo'
    obj = md5(salt)
    
    with open('./study/h.html', mode='rb') as f:
        for line in f:
            obj.update(line)
            
    bs = obj.hexdigest()
    print(bs)       # 输出32位小写哈希值 820624bcaf3fb56f10255aa4a11928ff
    
if __name__ == '__main__':
    # demo02()
    demo03()