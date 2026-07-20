import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analytics", page_icon="📊", layout="wide")

st.title("Housing Analytics Dashboard")

BASE_DIR = Path(__file__).resolve().parents[2]

df = pd.read_csv(BASE_DIR / "data" / "cleaned_housing.csv")

st.sidebar.header("Filters")

min_price, max_price = st.sidebar.slider(
    "Price Range",
    int(df["price"].min()),
    int(df["price"].max()),
    (
        int(df["price"].min()),
        int(df["price"].max())
    )
)

filtered_df = df[
    (df["price"] >= min_price) &
    (df["price"] <= max_price)
]


col1, col2, col3 = st.columns(3)

col1.metric("Total Houses", len(filtered_df))

col2.metric(
    "Average Price",
    f"₹ {filtered_df['price'].mean():,.0f}"
)

col3.metric(
    "Average Area",
    f"{filtered_df['area'].mean():,.0f} sq.ft"
)

st.divider()

fig = px.histogram(
    filtered_df,
    x="price",
    nbins=30,
    title="House Price Distribution"
)

st.plotly_chart(fig, use_container_width=True)

fig = px.scatter(
    filtered_df,
    x="area",
    y="price",
    color="furnishingstatus",
    size="bedrooms",
    hover_data=["bathrooms", "stories", "parking"],
    title="Area vs Price"
)

st.plotly_chart(fig, use_container_width=True)

bedroom = filtered_df.groupby("bedrooms")["price"].mean().reset_index()

fig = px.bar(
    bedroom,
    x="bedrooms",
    y="price",
    title="Average Price by Bedrooms"
)

st.plotly_chart(fig, use_container_width=True)

stories = filtered_df.groupby("stories")["price"].mean().reset_index()

fig = px.bar(
    stories,
    x="stories",
    y="price",
    title="Average Price by Stories"
)

st.plotly_chart(fig, use_container_width=True)

corr = filtered_df.select_dtypes(include="number").corr()

fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    title="Correlation Heatmap"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Dataset Preview")

st.dataframe(filtered_df)
