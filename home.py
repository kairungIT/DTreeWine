import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

# ===== ตั้งค่าหน้าเว็บ =====
st.set_page_config(
    page_title="🍷 Wine Classifier",
    page_icon="🍷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== Sidebar =====
with st.sidebar:
    st.markdown("## 🍷 SVM Classifier")
    st.markdown("---")
    st.markdown("""
    **แอปพลิเคชันจำแนกข้อมูล**  
    ใช้โมเดล SVM ในการวิเคราะห์
    """)
    st.markdown("---")
    st.markdown("### 📊 รายละเอียดของข้อมูล")
    st.markdown("- **Dataset:** Wine Dataset")
    st.markdown("- **Model:** Suport Vector")
    st.markdown("- **Features:** 13 คุณสมบัติ")
    st.markdown("- **Classes:** 3 ประเภท")
    st.markdown("---")
    st.markdown("### 🛠️ เทคโนโลยี")
    st.markdown("- Python 3.x")
    st.markdown("- scikit-learn")
    st.markdown("- Streamlit")


# โหลด Lottie จาก URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ตัวอย่างการใช้งาน
lottie_hello = load_lottieurl("https://lottie.host/3f647b41-61bf-4d39-93c3-0433420604cc/8NtmEbAWmO.json")

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