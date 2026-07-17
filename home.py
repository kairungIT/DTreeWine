import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

# โหลด Lottie จาก URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ตัวอย่างการใช้งาน
lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_Hs2j1y.json")

if lottie_hello:
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",  # low | medium | high
        height=300,
        width=300,
        key="hello"
    )