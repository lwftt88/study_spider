import re 


def demo01():
    
    s = '我今年18，我有200000元'
    
    # 匹配所有
    r = re.findall('a', 'abcdabc')
    print(r)    # ['a', 'a']
    
    # 匹配所有数字
    r = re.findall('\d+', s)
    print(r)    #  ['18', '200000']
    
    # 迭代器
    r = re.finditer('\d+', s)
    for i in r:
        print(i.group())
    # 18
    # 200000
    
    # 匹配第一个符合条件的字符
    r = re.search('\d+', s)
    print(r.group())
    # 18
    
    # 提前编译一个正则
    obj = re.compile('\d+')
    r = obj.findall(s)
    print(r)
    # ['18', '200000']
    
def demo02():
    
    s = '''
    <div> <span id="10086">中国移动</span> </div>
    <div> <span id="10010">中国联通</span> </div>
    '''
    
    # 匹配字符串
    obj = re.compile('<span id="\d+">.*?</span>')
    r = obj.findall(s)
    print(r)
    # ['<span id="10086">中国移动</span>', '<span id="10010">中国联通</span>']

    # 使用()提取指定的内容
    obj = re.compile('<span id="(\d+)">(.*?)</span>')
    r = obj.findall(s)
    print(r)
    # [('10086', '中国移动'), ('10010', '中国联通')]
    
    # 使用()提取指定的内容，并且指定名称方便取值
    obj = re.compile('<span id="(?P<ID>\d+)">(?P<Name>.*?)</span>')
    r = obj.finditer(s)
    for i in r:
        print(i.group('ID'), i.group('Name'))
    # [('10086', '中国移动'), ('10010', '中国联通')]

if __name__ == '__main__':
    # demo01()
    demo02()