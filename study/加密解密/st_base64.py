import base64


def base64_encode():
    bs = '这是一组测试数据，用来测试base64编码'.encode('utf-8')
    # base64主要处理字节用的
    print(bs)
    # 把字节按照base64的规则进行编码。编码成base64的字符串

    b_base64 = base64.b64encode(bs)     # 进行base64编码，编码结果为字节
    s = b_base64.decode('utf-8')        # 进行解码，转换成字符串
    print(b_base64)                     # 输出字节形式的base64编码                        
    print(s)                            # 输出字符串形式的base64编码
    return s

def base64_decode(s):
    bs = base64.b64decode(s)
    print(bs)
    source_s = bs.decode('utf-8')
    print(source_s)

if __name__ == '__main__':
    s = base64_encode()
    
    base64_decode(s)