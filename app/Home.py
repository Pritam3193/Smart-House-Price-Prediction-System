import streamlit as st

st.set_page_config(
    page_title="Smart House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.main{
    background-color:#f8fafc;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1{
    color:#0f172a;
    text-align:center;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #1e3a8a, #2563eb);
    border: none;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.3);
}

[data-testid="stMetricLabel"] {
    color: #ffffff !important;
    font-size: 18px;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-size: 38px;
    font-weight: bold;
}

div.stButton > button{
    width:100%;
    border-radius:10px;
    background:#2563eb;
    color:white;
    height:50px;
    font-size:18px;
}

div.stButton > button:hover{
    background:#1d4ed8;
    color:white;
}

section[data-testid="stSidebar"]{
    background:#0f172a;
}

section[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

st.title("🏠 Smart House Price Prediction & Analytics System")

st.markdown(
"""
<div style="text-align:center;font-size:20px;color:gray;">
Predict house prices using Machine Learning and explore interactive analytics.
</div>
""",
unsafe_allow_html=True
)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(" Houses", "545")

with col2:
    st.metric(" ML Models", "4")

with col3:
    st.metric("Best R²", "0.89+")

st.write("")
st.write("")

st.info(
"""
<- Use the sidebar to explore the application.

### Available Modules

-  House Price Prediction
-  Analytics Dashboard
-  Model Performance
-  Prediction History
- About Project
"""
)

st.write("")

st.success(" Built using Python, Streamlit, Scikit-learn, Plotly and SQLite.")