#//main/ul/li
import urllib
from urllib import request,parse
from lxml import etree
url = 'https://duel.wiki/card/list/?searchText={}'
word = input('请输入搜索内容:')
params = parse.quote(word)
full_url = url.format(params)
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
req = request.Request(url=full_url,headers=header)
res = request.urlopen(req)
html = res.read().decode('utf-8')
tree = etree.HTML(html)
cardRES = len(tree.xpath("//main/ul/li"))
#//main/ul/li//img/@alt
if cardRES>1:
    cardNAMES = tree.xpath("//main/ul/li//img/@alt")
    for i in cardNAMES:
        print(i)
