from urllib import request,parse

# 1.拼url地址
url = 'https://duel.wiki/card/list/?searchText={}'
word = input('请输入搜索内容:')
params = parse.quote(word)
#full_url = url + params
full_url = url.format(params)
print(full_url)

# 2.定义headers、获取解码网页
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
req = request.Request(url=full_url,headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')



