import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Bank Customer Churn Prediction", layout="centered")

st.title("🏦 Bank Customer Churn Prediction App")
st.markdown("Enter customer details below to predict if the customer is likely to leave the bank.")

# Input fields
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 100, 30)
tenure = st.slider("Tenure (Years with bank)", 0, 10, 3)
balance = st.number_input("Account Balance", min_value=0.0, value=50000.0)
num_of_products = st.selectbox("Number of Products", [1, 2, 3, 4])
has_cr_card = st.selectbox("Has Credit Card?", ["Yes", "No"])
is_active_member = st.selectbox("Is Active Member?", ["Yes", "No"])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=100000.0)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

# Convert inputs
gender = 1 if gender == "Male" else 0
has_cr_card = 1 if has_cr_card == "Yes" else 0
is_active_member = 1 if is_active_member == "Yes" else 0

# One-hot encoding for geography
geo_france = 0
geo_germany = 0
geo_spain = 0

if geography == "Germany":
    geo_germany = 1
elif geography == "Spain":
    geo_spain = 1
# France is the base case (drop_first=True), so all zeros

# Create input array
input_data = np.array([[
    credit_score, gender, age, tenure, balance,
    num_of_products, has_cr_card, is_active_member, estimated_salary,
    geo_germany, geo_spain
]])

# Prediction
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ The customer is likely to **churn**. (Risk Score: {probability:.2f})")
    else:
        st.success(f"✅ The customer is likely to **stay**. (Confidence: {1 - probability:.2f})")
