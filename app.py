import streamlit as st

# ==========================================
# 🛠️ 設定區 (請把你的網址貼在這裡！)
# ==========================================
# 範例： "https://project-tiger-hanhan.streamlit.app/"
TIGER_URL = "https://project-tiger.streamlit.app/" 
MO_URL = "https://project-01.streamlit.app/"

# ==========================================
# 🎨 頁面設定
# ==========================================
st.set_page_config(page_title="翰翰的賽博道場", page_icon="☯️", layout="centered")

# 賽博龐克 CSS (按鈕特效)
st.markdown("""
<style>
    .stApp {
        background-color: #050505;
        background-image: linear-gradient(rgba(0, 255, 65, 0.1) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 255, 65, 0.1) 1px, transparent 1px);
        background-size: 20px 20px;
        color: #e0e0e0;
    }
    h1 {
        color: #00F0FF !important;
        text-shadow: 0 0 10px #00F0FF, 0 0 20px #00F0FF;
        font-family: 'Courier New', monospace;
        text-align: center;
    }
    .card {
        border: 2px solid #333;
        border-radius: 10px;
        padding: 20px;
        background-color: #111;
        text-align: center;
        margin-bottom: 20px;
        transition: transform 0.3s;
    }
    .card:hover {
        transform: scale(1.02);
        border-color: #00F0FF;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🖥️ 主畫面
# ==========================================
st.title("☯️ 蓬 萊 P E N G L A I")
st.caption("翰翰的數位作品集 | 萬機建醮・數據飛昇")

st.divider()

col1, col2 = st.columns(2)

# --- 左邊：虎爺 (財庫) ---
with col1:
    st.markdown("""
    <div class="card">
        <h2>🐯 Project 財庫</h2>
        <p>數位香油錢・機率演算</p>
        <p style="font-size: 0.8em; color: #888;">Python / Pandas / Gacha Logic</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 這裡就是超連結按鈕
    st.link_button("🚀 啟動虎爺矩陣", TIGER_URL, use_container_width=True)

# --- 右邊：M.O. (靈驗) ---
with col2:
    st.markdown("""
    <div class="card">
        <h2>⛩️ Project 靈驗</h2>
        <p>天巡者戰情・氣象監控</p>
        <p style="font-size: 0.8em; color: #888;">Streamlit / Data Viz / Risk Algo</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 這裡就是超連結按鈕
    st.link_button("📡 連線天巡者系統", MO_URL, use_container_width=True)

st.divider()

# --- 底部介紹 ---
st.markdown("### 👤 關於架構師")
st.info("""
我是翰翰，一名跨領域的 **賽博道士 (Cyber Taoist)**。
我擅長將傳統文化與現代技術結合，利用 Python 進行數據煉丹，
並透過 React 構建虛擬法壇。
""")

st.write("© 2026 PENGLAI OS. All rights reserved.")
