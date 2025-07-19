import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# App title
st.title("🧠 Bank Customer Churn Prediction App")

# Sidebar input form
st.sidebar.header("Enter Customer Data")

def user_input():
    credit_score = st.sidebar.slider("Credit Score", 300, 900, 650)
    age = st.sidebar.slider("Age", 18, 100, 35)
    tenure = st.sidebar.slider("Tenure", 0, 10, 3)
    balance = st.sidebar.number_input("Balance", 0.00, 300000.00, 50000.00)
    num_of_products = st.sidebar.selectbox("Number of Products", [1, 2, 3, 4])
    has_cr_card = st.sidebar.selectbox("Has Credit Card", [0, 1])
    is_active_member = st.sidebar.selectbox("Is Active Member", [0, 1])
    estimated_salary = st.sidebar.number_input("Estimated Salary", 10000.00, 200000.00, 50000.00)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    geography = st.sidebar.selectbox("Geography", ["France", "Germany", "Spain"])

    # Encode categorical
    gender = 1 if gender == "Male" else 0
    geography_france = 1 if geography == "France" else 0
    geography_germany = 1 if geography == "Germany" else 0

    # Manual one-hot encoding
    data = {
        'CreditScore': credit_score,
        'Gender': gender,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_of_products,
        'HasCrCard': has_cr_card,
        'IsActiveMember': is_active_member,
        'EstimatedSalary': estimated_salary,
        'Geography_Germany': geography_germany,
        'Geography_Spain': 1 - geography_france - geography_germany  # If not France or Germany, then Spain
    }

    return pd.DataFrame(data, index=[0])

input_df = user_input()

# Show input
st.subheader("Customer Input Data")
st.write(input_df)

# Predict
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

# Show result
st.subheader("Prediction")
st.write("Churn" if prediction[0] == 1 else "Not Churn")
st.subheader("Prediction Probability")
st.write(prediction_proba)
