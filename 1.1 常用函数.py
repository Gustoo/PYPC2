import urllib.request
from urllib import request,parse
url = "https://duel.wiki/"
xiazai = "aaa.mp4" # aaa.jpg  aaa.html
urllib.request.urlretrieve(url,xiazai)

#user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
#查询UA 检查 network 刷新 UA 复制 变成字典
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

a = urllib.parse.urlencode() #多个键值对 &连接

# post请求   查字典 翻译等
# data = urllib.parse.urlencode().encode('utf-8')
# req = request.Request(url=url,data=data,headers=headers)

import json
a = json.loads()  #修改变量类型

encode = "utf-8"
with open("","w",encoding=encode) as fp:
    fp.write(a)

#cookie免密登录

#handler
handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)
respond = opener.open()

#IP代理 代理池
proxies = {}
request = urllib.request.Request(url=url,headers=header)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
respond = opener.open()

#xpath c+s+x
#xpath解析  etree.HTML()
from lxml import etree
tree = etree.parse()
list = tree.xpath("//ul/li") #//子孙节点  /子节点
# [@id] 有属性标签id的节点 "//ul/li[@id]"
# text()获取标签里的内容  [@id]/text()
# [@id = "ulink"]/text()
list = tree.xpath("//ul/li[@id = 'ulink']/@class")
#id中包含l的标签 contains "//ul/li[contains(@id,'l')]

# jsonPath BeautifulSoup

# ./yghimg/