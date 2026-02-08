import streamlit as st

# ==========================================
# 🔗 設定區 (請填入你的真實專案網址)
# ==========================================
TIGER_URL = "https://project-tiger.streamlit.app/" 
MO_URL = "https://project-01.streamlit.app/"

# ==========================================
# 🛠️ 頁面配置
# ==========================================
st.set_page_config(
    page_title="Nathan Su | Penglai Core", 
    page_icon="☯️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 👺 蓬萊賽博風格 CSS (Penglai Cyber Style)
st.markdown("""
<style>
    /* 1. 背景：賽博格線 */
    .stApp {
        background-color: #050505;
        background-image: 
            linear-gradient(rgba(0, 240, 255, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 240, 255, 0.05) 1px, transparent 1px);
        background-size: 30px 30px;
        color: #e0e0e0;
        font-family: 'Segoe UI', 'Microsoft JhengHei', sans-serif;
    }
    
    /* 2. 標題：霓虹光暈 */
    h1, h2, h3 {
        color: #00F0FF !important;
        text-shadow: 0 0 10px rgba(0, 240, 255, 0.6), 0 0 20px rgba(0, 240, 255, 0.4);
        font-family: 'Courier New', monospace; /* 科技感字體 */
        font-weight: 800;
    }
    
    /* 3. 專案卡片：HUD 風格 */
    .cyber-card {
        background-color: rgba(16, 20, 24, 0.8);
        border: 1px solid #00F0FF;
        border-radius: 4px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .cyber-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 25px rgba(0, 240, 255, 0.3);
        border-color: #00FF41; /* hover 變綠色 */
    }

    /* 裝飾線條 */
    .cyber-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, #00F0FF, transparent);
    }

    /* 4. 技術標籤：矩陣風格 */
    .tech-tag {
        display: inline-block;
        background-color: rgba(0, 255, 65, 0.1);
        border: 1px solid #00FF41;
        color: #00FF41;
        padding: 2px 10px;
        font-family: 'Courier New', monospace;
        font-size: 0.8rem;
        margin-right: 6px;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }

    /* 5. 按鈕優化 */
    .stButton button {
        background-color: transparent !important;
        border: 2px solid #FF0055 !important;
        color: #FF0055 !important;
        font-weight: bold !important;
        font-family: 'Courier New', monospace !important;
        transition: all 0.3s !important;
    }
    .stButton button:hover {
        background-color: #FF0055 !important;
        color: #000 !important;
        box-shadow: 0 0 15px #FF0055;
    }
    
    /* 分隔線 */
    hr {
        border-color: #333;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 👤 Header: 個人簡介 (專業文字 + 賽博視覺)
# ==========================================
col1, col2 = st.columns([3, 1])

with col1:
    st.title("蘇 玟 翰 (NATHAN SU)")
    st.markdown("### `Software Engineer` | `Tech Consultant`")
    st.info("""
    **核心價值：**
    將繁瑣的商業邏輯，煉化為高效的自動化系統。
    具備 **Python 全端開發**、**資料工程 (ETL)** 與 **系統架構設計** 能力。
    """)

with col2:
    # 這裡用一個賽博八卦圖示代替大頭照
    st.markdown("""
    <div style="text-align: center; font-size: 5rem; text-shadow: 0 0 20px #00FF41;">
        ☯️
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# 🚀 Projects: 實作展示
# ==========================================
st.header("📂 SYSTEM DEPLOYMENT (專案展示)")

p_col1, p_col2 = st.columns(2)

# --- Project 1: 虎爺 (後端邏輯) ---
with p_col1:
    st.markdown("""
    <div class="cyber-card">
        <h3>🐯 Project 虎爺 (Tiger Matrix)</h3>
        <p style="color: #00FF41;">>> Status: ONLINE</p>
        <div>
            <span class="tech-tag">Python</span>
            <span class="tech-tag">Pandas</span>
            <span class="tech-tag">Microservices</span>
        </div>
        <br>
        <p style="font-size: 0.95rem; line-height: 1.6;">
            <strong>【機率模擬系統】</strong><br>
            基於 Python 構建的高併發運算架構。
            <br><br>
            <strong>技術架構：</strong>
            <ul>
                <li><strong>Core Logic:</strong> 使用 NumPy 進行萬人級別的機率分佈演算 (Gacha Algorithm)。</li>
                <li><strong>Architecture:</strong> 採用 Stateless 設計，確保系統可水平擴展。</li>
                <li><strong>DevOps:</strong> 整合 GitHub Actions 實現自動化部署 (CI/CD)。</li>
            </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 啟動系統演示", TIGER_URL, use_container_width=True)

# --- Project 2: 靈驗 (政府級應用) ---
with p_col2:
    st.markdown("""
    <div class="cyber-card">
        <h3>⛩️ Project 靈驗 (M.O. System)</h3>
        <p style="color: #00FF41;">>> Status: ONLINE</p>
        <div>
            <span class="tech-tag">Data Visualization</span>
            <span class="tech-tag">Risk Algo</span>
            <span class="tech-tag">Gov-Tech</span>
        </div>
        <br>
        <p style="font-size: 0.95rem; line-height: 1.6;">
            <strong>【農業風險決策儀表板】</strong><br>
            源自雲林縣政府專案，數位轉型 (DX) 代表作。
            <br><br>
            <strong>技術架構：</strong>
            <ul>
                <li><strong>Algorithm:</strong> 整合氣象數據，透過加權算法即時計算「農損風險值」。</li>
                <li><strong>Dashboard:</strong> 將複雜數據轉化為動態可視化圖表，降低決策認知負載。</li>
                <li><strong>Impact:</strong> 作為決策支援系統 (DSS)，協助預判極端氣候風險。</li>
            </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("📊 進入戰情中心", MO_URL, use_container_width=True)

st.markdown("---")

# ==========================================
# 📜 Footer: 技術棧 (終端機風格)
# ==========================================
st.header("🛠️ TECH STACK_")

f_col1, f_col2, f_col3 = st.columns(3)

def code_block(title, items):
    items_html = "".join([f"<li>{item}</li>" for item in items])
    return f"""
    <div style="font-family: 'Courier New'; border-left: 2px solid #333; padding-left: 10px;">
        <strong style="color: #FF0055;">{title}</strong>
        <ul style="color: #888; font-size: 0.9rem; list-style-type: square;">
            {items_html}
        </ul>
    </div>
    """

with f_col1:
    st.markdown(code_block("Backend & Data", [
        "Python (FastAPI / Flask)",
        "SQL / NoSQL Database",
        "ETL Pipeline Design"
    ]), unsafe_allow_html=True)

with f_col2:
    st.markdown(code_block("Frontend & Viz", [
        "React.js / Three.js",
        "Streamlit / Dash",
        "UI/UX Prototyping"
    ]), unsafe_allow_html=True)

with f_col3:
    st.markdown(code_block("Infrastructure", [
        "Git / GitHub Actions",
        "Linux System Ops",
        "Cloud Deployment"
    ]), unsafe_allow_html=True)

st.markdown("<br><center style='color: #555; font-family: monospace;'>© 2026 PENGLAI OS. SYSTEM STABLE.</center>", unsafe_allow_html=True)