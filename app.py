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
    has_cr_card = st.sidebar.selectbox("Has Credit Card", [1, 0])  # 1 = Yes, 0 = No
    is_active_member = st.sidebar.selectbox("Is Active Member", [1, 0])
    estimated_salary = st.sidebar.number_input("Estimated Salary", 10000.00, 200000.00, 50000.00)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    geography = st.sidebar.selectbox("Geography", ["France", "Germany", "Spain"])

    # Encode categorical variables
    gender = 1 if gender == "Male" else 0
    geography_germany = 1 if geography == "Germany" else 0
    geography_spain = 1 if geography == "Spain" else 0

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
        'Geography_Spain': geography_spain
    }

    return pd.DataFrame(data, index=[0])

# Collect user input
input_df = user_input()

# Display input
st.subheader("📋 Customer Input Summary")
st.write(input_df)

# Predict button
if st.button("🔍 Predict"):
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    st.subheader("🎯 Prediction Result")
    st.write("⚠️ **Churn**" if prediction[0] == 1 else "✅ **Not Churn**")

    st.subheader("📊 Prediction Probabilities")
    st.write(f"**Not Churn**: {prediction_proba[0][0]:.2f}")
    st.write(f"**Churn**: {prediction_proba[0][1]:.2f}")
