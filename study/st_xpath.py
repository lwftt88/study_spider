from lxml import etree


xml = """
<book>
    <name>book1</name>
    <price>
        1.23
    </price>
    <author>
        <nick id="10086"> 周杰伦</nick>
        <nick id="10010"> 中国联通</nick>
        <div>
            <nick>这只是刚刚开始</nick>
        </div>
    </author>

    <partner>
        <nick id="1"> 中国</nick>
        <nick id="2"> 美国</nick>
    </partner>
</book>
"""

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<ul>
    <li><a href="http://www.baidu.comm">百度</a></li>
    <li><a href="http://www.google.comm">谷歌</a></li>
    <li><a href="http://www.baidu.comm">百度</a></li>
</ul>
<ol>
    <li><a href="http://www.feiji.comm">飞机</a></li>
    <li><a href="http://www.dapao.comm">大炮</a></li>
    <li><a href="http://www.huoche.comm">火车</a></li>
</ol>
<div class="job">刘德华</div>
<div class="common">周润发</div>
</body>
</html>
"""
 

def demo_xml():
    et = etree.XML(xml)
    request = et.xpath('/book')     # / 表示根节点
    print(request)
    
    request = et.xpath('/book/name')    # name子节点   
    print(request)
    
    request = et.xpath('/book/name/text()')[0]    # text() 拿文本   
    print(request.strip())

    request = et.xpath('/book//nick/text()')       # 拿到所有nick节点
    print(request)
    
    request = et.xpath('/book/*/nick/text()')       # 只拿子节点的nick
    print(request)
    
    request = et.xpath('/book/*/*/nick/text()')       # 只拿孙节点的nick
    print(request)

    request = et.xpath('/book/*/nick[@id="1"]/text()')       # 拿取id=1 的nick 子节点数据
    print(request)
    
    request = et.xpath('/book/partner/nick/@id')       # 拿取/book/partner/nick 的ID信息
    print(request)

def demo_html():
    et = etree.HTML(html)
    li_list = et.xpath('/html/body/ul/li[2]/a/text()')  # 获取 li 第二个节点a标签的内容 结果 ['谷歌']
    print(li_list)
    
    li_list = et.xpath('//li')  # 获取所有a标签的域名和文本
    for li in li_list:
        herf = li.xpath('./a/@href')[0]     # ./ 表示当前节点
        text = li.xpath('./a/text()')[0]
        print(text, herf)

if __name__ == '__main__':
    # demo_xml()
    demo_html()
    