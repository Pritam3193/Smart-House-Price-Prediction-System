import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Prediction History",
    page_icon="🗄",
    layout="wide"
)

st.title("🗄 Prediction History")

conn = sqlite3.connect("../database/housing.db")

try:

    df = pd.read_sql_query(
        "SELECT * FROM predictions ORDER BY id DESC",
        conn
    )

    st.metric("Total Predictions", len(df))

    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Prediction History",
        csv,
        "prediction_history.csv",
        "text/csv"
    )

except Exception:

    st.warning("No predictions available.")

conn.close()