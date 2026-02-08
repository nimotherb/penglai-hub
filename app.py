import streamlit as st

# ==========================================
# 🔗 設定區 (請填入你的真實專案網址)
# ==========================================
# 務必確認這裡填的是 Streamlit 部署後的網址
TIGER_URL = "https://project-tiger.streamlit.app/" 
MO_URL = "https://project-01.streamlit.app/"

# ==========================================
# 🛠️ 頁面配置
# ==========================================
st.set_page_config(
    page_title="Nathan Su | Technical Portfolio", 
    page_icon="💻", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 專業級 CSS (深色 IDE 風格)
st.markdown("""
<style>
    /* 全域設定 */
    .stApp {
        background-color: #0E1117;
        color: #C9D1D9;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* 標題與強調色 */
    h1, h2, h3 {
        color: #58A6FF !important; /* VS Code Blue */
        font-weight: 600;
    }
    
    /* 專案卡片容器 */
    .project-card {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 6px;
        padding: 20px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .project-card:hover {
        border-color: #58A6FF;
        box-shadow: 0 4px 12px rgba(88, 166, 255, 0.1);
    }
    
    /* 技術標籤 */
    .tech-tag {
        display: inline-block;
        background-color: #238636;
        color: #ffffff;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 500;
        margin-right: 5px;
        margin-bottom: 5px;
    }
    
    /* 連結按鈕優化 */
    .stButton button {
        width: 100%;
        border-radius: 4px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 👤 Header: 個人簡介
# ==========================================
col1, col2 = st.columns([3, 1])

with col1:
    st.title("蘇 玟 翰 (Nathan Su)")
    st.markdown("#### 軟體工程師 | 跨域技術顧問 | 自動化解決方案專家")
    st.markdown("""
    > 專注於將繁瑣的商業邏輯轉化為高效的自動化系統。
    > 具備 **Python 全端開發**、**資料工程 (ETL)** 與 **系統架構設計** 能力。
    > 擅長從使用者痛點出發，構建可擴展的數位解決方案。
    """)

with col2:
    # 這裡可以放你的大頭照，目前先用 icon 代替
    st.markdown("<div style='text-align: center; font-size: 4rem;'>👨‍💻</div>", unsafe_allow_html=True)

st.divider()

# ==========================================
# 🚀 Projects: 實作展示
# ==========================================
st.header("📂 精選專案 (Featured Projects)")

p_col1, p_col2 = st.columns(2)

# --- Project 1: 虎爺 (後端邏輯與機率模擬) ---
with p_col1:
    st.markdown("""
    <div class="project-card">
        <h3>🐯 Project 虎爺 (Tiger Matrix)</h3>
        <p><strong>類型：</strong>機率演算與微服務架構實作</p>
        <div>
            <span class="tech-tag">Python</span>
            <span class="tech-tag">Pandas</span>
            <span class="tech-tag">Streamlit</span>
            <span class="tech-tag">CI/CD</span>
        </div>
        <hr style="border-color: #30363D; margin: 10px 0;">
        <p style="font-size: 0.9rem; color: #8B949E;">
            這是一個基於 Python 構建的<strong>高併發機率模擬系統</strong>。
            <br><br>
            <strong>技術亮點：</strong>
            <ul>
                <li><strong>後端邏輯：</strong> 使用 NumPy 與 Pandas 進行高效能數值運算，模擬萬人同時在線的機率分佈 (Gacha Logic)。</li>
                <li><strong>架構設計：</strong> 採用 Stateless 架構，確保系統可水平擴展。</li>
                <li><strong>DevOps：</strong> 建立完整的開發流程，從 Local 環境測試、Cloudflare Tunnel 穿透驗證，到 GitHub 自動化部署至雲端。</li>
            </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 啟動系統演示", TIGER_URL, use_container_width=True)

# --- Project 2: 靈驗 (政府級儀表板) ---
with p_col2:
    st.markdown("""
    <div class="project-card">
        <h3>⛩️ Project 靈驗 (M.O. System)</h3>
        <p><strong>類型：</strong>農業數位轉型 (DX) 風險監控儀表板</p>
        <div>
            <span class="tech-tag">Data Visualization</span>
            <span class="tech-tag">Risk Algorithm</span>
            <span class="tech-tag">Gov-Tech</span>
        </div>
        <hr style="border-color: #30363D; margin: 10px 0;">
        <p style="font-size: 0.9rem; color: #8B949E;">
            源自<strong>雲林縣政府農業專案</strong>，旨在協助農民進行精準決策。
            <br><br>
            <strong>技術亮點：</strong>
            <ul>
                <li><strong>核心算法：</strong> 整合降雨量、風速與病蟲害指數，透過加權演算法即時計算「農損風險值」。</li>
                <li><strong>資料視覺化：</strong> 將複雜的氣象數據轉化為直觀的動態儀表板 (Dashboard)，降低使用者的認知負載。</li>
                <li><strong>應用場景：</strong> 作為決策支援系統 (DSS)，協助政府單位與農民預判極端氣候風險。</li>
            </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("📊 進入戰情中心", MO_URL, use_container_width=True)

st.divider()

# ==========================================
# 📜 Footer: 專業技能摘要
# ==========================================
st.markdown("### 🛠️ 技術棧 (Tech Stack)")
f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    st.markdown("**Backend & Data**")
    st.markdown("- Python (FastAPI / Flask)")
    st.markdown("- SQL / NoSQL Database")
    st.markdown("- ETL Pipeline Design")

with f_col2:
    st.markdown("**Frontend & Visualization**")
    st.markdown("- React.js / Three.js")
    st.markdown("- Streamlit / Dash")
    st.markdown("- UI/UX Prototyping")

with f_col3:
    st.markdown("**Infrastructure & Tools**")
    st.markdown("- Git / GitHub Actions")
    st.markdown("- Linux System Ops")
    st.markdown("- Cloud Deployment")

st.markdown("---")
st.caption("© 2026 Nathan Su. Built with Python & Streamlit.")