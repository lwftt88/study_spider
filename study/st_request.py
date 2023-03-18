import requests
import pprint



def ex01_get():
    """
    学习: Request Get方法,使用sogou搜索内容
    """
    url = 'https://www.sogou.com/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    content = input('请输出要搜索的内容：')
    resp = requests.get(f'{url}web?query={content}', headers=header)
    resp.encoding = 'utf-8'
    print(resp.text)
    print(resp.headers)
    print(resp.request.headers)

def ex02_post(): 
    url = 'https://fanyi.baidu.com/sug'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    data = {
        'kw':'dog'
    }  
    resp = requests.post(url, data=data, headers=header) 
    print(resp.json())
    
    

def ex03_get_with_parms():
    url = 'https://movie.douban.com/j/chart/top_list'
    
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    
    parms = {
        'type': '17',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }
    
    resp = requests.get(url, headers= header, params=parms)
    m_list = resp.json()
    pprint.pprint(resp.json())
    for m in m_list:
        print(m['title'], m['score'], m['vote_count'], m['regions'], m['release_date'])
    
if __name__ == '__main__':  
    # ex01_get()
    # ex02_post()
    
    ex03_get_with_parms()