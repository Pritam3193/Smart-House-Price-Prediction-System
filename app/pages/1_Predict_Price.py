import streamlit as st
import pandas as pd
import joblib
import sqlite3

st.set_page_config(page_title="Predict Price", page_icon="💰")

st.title("House Price Prediction")

# Load Model
model = joblib.load("../models/best_house_price_model.pkl")
encoder = joblib.load("../models/furnishing_encoder.pkl")

# Input Fields
area = st.number_input("Area (sq ft)", 500, 20000, 3000)

bedrooms = st.slider("Bedrooms", 1, 10, 3)

bathrooms = st.slider("Bathrooms", 1, 10, 2)

stories = st.slider("Stories", 1, 5, 2)

parking = st.slider("Parking", 0, 5, 1)

mainroad = st.selectbox("Main Road", ["yes", "no"])

guestroom = st.selectbox("Guest Room", ["yes", "no"])

basement = st.selectbox("Basement", ["yes", "no"])

hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])

airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])

prefarea = st.selectbox("Preferred Area", ["yes", "no"])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)

if st.button("Predict Price"):

    furnishing = encoder.transform([furnishingstatus])[0]

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [1 if mainroad == "yes" else 0],
        "guestroom": [1 if guestroom == "yes" else 0],
        "basement": [1 if basement == "yes" else 0],
        "hotwaterheating": [1 if hotwaterheating == "yes" else 0],
        "airconditioning": [1 if airconditioning == "yes" else 0],
        "parking": [parking],
        "prefarea": [1 if prefarea == "yes" else 0],
        "furnishingstatus": [furnishing]
    })

    prediction = model.predict(input_data)

    st.metric(
        label="🏠 Estimated House Price",
        value=f"₹ {prediction[0]:,.2f}"
    )

    
    conn = sqlite3.connect("../database/housing.db")
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    area REAL,
    bedrooms INTEGER,
    bathrooms INTEGER,
    stories INTEGER,
    mainroad INTEGER,
    guestroom INTEGER,
    basement INTEGER,
    hotwaterheating INTEGER,
    airconditioning INTEGER,
    parking INTEGER,
    prefarea INTEGER,
    furnishingstatus TEXT,
    predicted_price REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

    cursor.execute("""
INSERT INTO predictions(
area,
bedrooms,
bathrooms,
stories,
mainroad,
guestroom,
basement,
hotwaterheating,
airconditioning,
parking,
prefarea,
furnishingstatus,
predicted_price
)
VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
""",(
area,
bedrooms,
bathrooms,
stories,
1 if mainroad=="yes" else 0,
1 if guestroom=="yes" else 0,
1 if basement=="yes" else 0,
1 if hotwaterheating=="yes" else 0,
1 if airconditioning=="yes" else 0,
parking,
1 if prefarea=="yes" else 0,
furnishingstatus,
float(prediction[0])
))

    conn.commit()
    conn.close()

    st.success("Prediction saved successfully!")