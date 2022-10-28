import streamlit as st
import math
import numpy as np
from PIL import Image

st.title('Yu-Gi-Oh Card Download',)
st.write("""By Ida&Gusto""")
st.info("This software is used to query the card effect "
         "of YuGiOh, and it can directly help to download the card pattern for printing.")

message = st.text_input("""Please Enter The Card Name""")
img = Image.open("yghimg/增殖的G.jpg")
img = img.resize((295,430),Image.ANTIALIAS)
#st.image(img)
col1,col2  = st.columns(2)
with col1:
    st.header("Card Image")
    st.image(img)
with col2:
    st.header("Card Effect")
    st.write("怪兽/效果")
    st.write("这个卡名的①的效果1回合只能使用1次，对方回合也能发动。"
             "①：把这张卡从手卡送去墓地才能发动。这个回合，以下效果适用。"
             "每次对方对怪兽的特殊召唤成功，自己必须从卡组抽1张。")

st.error("!!!!!")
#st.color_picker("#FF0000")
#base="light"