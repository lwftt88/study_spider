from urllib.parse import urlencode, unquote

def url_encode():
    """_summary_
    https://www.baidu.com/s?wd=md5%E5%9C%A8%E7%BA%BF%E5%8A%A0%E5%AF%86

    url base64 编码
    """
    base_url = 'https://www.baidu.com/s?'
    params_dic = {
        'wd': 'md5在线加密'
    }
    result = urlencode(params_dic)
    print(base_url+result)
    
def url_unquote():
    """_summary_
    https://www.baidu.com/s?wd=md5%E5%9C%A8%E7%BA%BF%E5%8A%A0%E5%AF%86
    
    url base 解码
    """
    url = 'https://www.baidu.com/s?wd=md5%E5%9C%A8%E7%BA%BF%E5%8A%A0%E5%AF%86'
    result = unquote(url)
    print(result)

    

if __name__ == '__main__':
    url_encode()
    url_unquote()