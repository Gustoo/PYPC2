# 多页面spider

from urllib import request,parse
import time
import random


class PagesSpider(object):
    #网址
    def __init__(self):
        self.url='http://tieba.baidu.com/f?{}'

    #获取网页
    def get_html(self,url):
        header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "+
                "(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

        req=request.Request(url=url,headers=header)
        res=request.urlopen(req)
        html=res.read().decode("utf-8")
        return html


    #保存文件函数
    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)

    #入口函数
    def run(self):
        name=input('输入贴吧名：')
        sp=int(input('输入起始页：'))
        ep=int(input('输入终止页：'))

        for page in range(sp,ep+1):
            #约束条件
            pn=(page-1)*50
            params={
                'kw':name,
                'pn':str(pn)
            }
            #拼接URL地址
            params=parse.urlencode(params)
            url=self.url.format(params)
            #发请求
            html=self.get_html(url)
            #定义路径
            filename='{}-{}页.html'.format(name,page)
            self.save_html(filename,html)
            #提示
            print('第%d页抓取成功'%page)
            #每爬取一个页面随机休眠1-2秒钟的时间
            time.sleep(random.randint(1,2))

#以脚本的形式启动爬虫
if __name__=='__main__':
    start = time.time()
    spider = PagesSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f'%(end-start))





