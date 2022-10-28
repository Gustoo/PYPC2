#//main//li//div[@class='description']
#"//head/meta[@name='description']/@content"
#//main//li//div//img/@src
import streamlit as st
import math
import time
import random
import numpy as np
from PIL import Image
import urllib
from urllib import request,parse,error
from lxml import etree

message= ""
def getall(word):
    url = 'https://duel.wiki/card/list/?searchText={}'
    params = parse.quote(word)
    full_url = url.format(params)
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    time.sleep(random.randint(1, 2))
    try:
        req = request.Request(url=full_url,headers=header)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
    except urllib.error.URLError:
        st.error("软件升级中...")

    tree = etree.HTML(html)
    cardNAMES = tree.xpath("//main/ul/li//img/@alt")
    cardRES = len(tree.xpath("//main/ul/li"))
    snc=-1 #same name card
    if cardRES>1:
        for i in range(cardRES):
            if(word==cardNAMES[i]):
                snc = i
        if snc == -1:
        #print("请精确卡片名称后再次使用！")
            st.error("请精确卡片名称后再次使用！卡片名称参考:")
        #st.info("")
            for i in cardNAMES:
                st.info(i)
        else:
            Cardtype = tree.xpath("//main//li//div[@class='type']/text()")[snc]
            Cardkoka = tree.xpath("//main//li//div[@class='description']/text()")[snc]
            CardDL = tree.xpath("//main//li//div//img/@src")[snc]
            show(CardDL, word, Cardtype, Cardkoka)
    else:
        Cardtype = tree.xpath("//main//li//div[@class='type']/text()")[0]
        Cardkoka = tree.xpath("//main//li//div[@class='description']/text()")[0]
        #print(Cardtype)
        #print(Cardkoka)
        CardDL = tree.xpath("//main//li//div//img/@src")[0]
        show(CardDL, word, Cardtype, Cardkoka)


def show(CardDL,word,Cardtype,Cardkoka):
    urllib.request.urlretrieve(url=CardDL, filename="./yghimg/" + str(word) + ".jpg")
    # print("已成功下载卡片")
    img = Image.open("./yghimg/" + str(word) + ".jpg")
    img = img.resize((295, 430), Image.ANTIALIAS)
    # st.image(img)
    col1, col2 = st.columns(2)
    with col1:
        st.header("Card Image")
        st.image(img)
    with col2:
        st.header("Card Effect")
        st.write(Cardtype)
        st.write(Cardkoka)
        with open("./yghimg/" + str(word) + ".jpg", "rb") as file:
            btn = st.download_button(
                label="Download image",
                data=file,
                file_name=str(word) + ".jpg",
                mime="image/jpg",
            )
        if btn == True:
            success()

def success():
    st.success("The picture is downloaded successfully")

def APP():
    global message
    st.title('Yu-Gi-Oh Card Download')
    st.write("""By Ida&Gusto""")
    st.info("This software is used to query the card effect "
             "of YuGiOh, and it can directly help to download "
            "the card pattern for printing.")
    message = st.text_input("""Please Enter The Card Name""")




if __name__ == '__main__':
    APP()
    #word = input('请输入搜索内容:')
    if len(message) >1:

        getall(message)
    else:
        st.error("请精确卡片名称后使用！")

