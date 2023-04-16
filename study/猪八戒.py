"""_summary_
1. 拿页面源代码
2. 从页面源代码提取想要的数据。价格，名称，公司名称
"""

import re
from lxml import etree
import requests
import pprint

def run(page_num):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    params = {
        'indexAlias': 'wzjs',
        'size': '20',
        'pageNum': f'{page_num}',
        'fromBizType': '1',
        'fromSite': '1',
    }
    url = 'https://chaoyang.zbj.com/index2022/seo/service/searchservice'
    resp = requests.get(url, params=params)
    resp.encoding = 'utf-8'
    
    # et = etree.HTML(resp)
    # p = et.xpath('//div[@class="service-card-wrap"]/div')
    
    # pprint.pprint(resp.json())
    
    for entity in resp.json().get('data'):
        # pprint.pprint(entity)
        price = entity.get('price').get('format')
        sale_count = entity.get('saleCount').get('format')
        name = entity.get('name')
        print(f'name:{name:50} price:{price:10} count:{sale_count:10}')
        
    # print(len(resp.json().get('data')))
    
if __name__ == '__main__':
    for i in range(1,50):
        run(i)


