import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ", layout="wide")

st.title("About This Project")

st.markdown("""
## Smart House Price Prediction & Analytics System

A machine learning web application that predicts house prices based on property features and provides interactive analytics through a Streamlit dashboard.

### Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- SQLite
- Joblib

### Machine Learning Models

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

### Features

- House Price Prediction
- Interactive Analytics Dashboard
- Model Performance Comparison
- Prediction History using SQLite
- Download Prediction History as CSV

### Dataset Features

- Area
- Bedrooms
- Bathrooms
- Stories
- Main Road
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Parking
- Preferred Area
- Furnishing Status

### Developed By

**Pritam Singh**

B.Tech Computer Science Engineering (Data Science)

### GitHub

https://github.com/Pritam3193/Smart-House-Price-Prediction-System
""")