import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Model Performance", page_icon="📈", layout="wide")

st.title("Model Performance")

results = pd.read_csv("../reports/model_results.csv")
importance = pd.read_csv("../reports/feature_importance.csv")

col1, col2, col3 = st.columns(3)

best_model = results.loc[results["R2 Score"].idxmax(), "Model"]
best_r2 = results["R2 Score"].max()
lowest_rmse = results["RMSE"].min()

col1.metric("Best Model", best_model)
col2.metric("Best R² Score", f"{best_r2:.4f}")
col3.metric("Lowest RMSE", f"{lowest_rmse:.2f}")

st.subheader("Model Comparison")

st.dataframe(results, use_container_width=True)

fig = px.bar(
    results,
    x="Model",
    y="R2 Score",
    color="Model",
    title="R² Score Comparison",
    text_auto=".3f"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.bar(
    results,
    x="Model",
    y="MAE",
    color="Model",
    title="MAE Comparison",
    text_auto=".2f"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.bar(
    results,
    x="Model",
    y="RMSE",
    color="Model",
    title="RMSE Comparison",
    text_auto=".2f"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.bar(
    importance,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Feature Importance",
    color="Importance"
)

fig.update_layout(yaxis={"categoryorder": "total ascending"})

st.plotly_chart(fig, use_container_width=True)