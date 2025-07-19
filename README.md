📘 DeveloperHub Task 3 – Customer Churn Prediction using ML
📌 Task Objective
This task focuses on building a classification model to predict whether a bank customer is likely to leave the bank (churn) or not, based on demographic and account activity data.

📁 Dataset
Name: Churn Modelling Dataset
Source: Kaggle

📊 Features:
CreditScore

Geography

Gender

Age

Tenure

Balance

NumOfProducts

HasCrCard

IsActiveMember

EstimatedSalary

🎯 Target:
Exited (0 = Not Churned, 1 = Churned)

🛠️ Tools & Libraries Used
Pandas – Data loading & preprocessing

Matplotlib & Seaborn – Data Visualization

Scikit-learn – Model training, evaluation

Streamlit – Web-based deployment

Pickle – Saving trained model and encoder

🚀 Approach
1. Dataset Loading & Understanding
Used pandas.read_csv() to load the dataset

Explored with .info(), .describe(), .value_counts()

2. Data Cleaning & Preparation
Dropped irrelevant features like RowNumber, CustomerId, and Surname

Encoded categorical features:

Label Encoding: Gender

One-Hot Encoding: Geography

Scaled numerical features using StandardScaler

3. Exploratory Data Analysis (EDA)
Visualized churn distribution using bar plots

Analyzed age, balance, and salary distributions

Correlation heatmap to detect feature relationships

Box plots and bar graphs to compare churn vs. features

4. Model Training & Testing
Split dataset into training (80%) and testing (20%)

Trained models:

Logistic Regression

Decision Tree

Random Forest Classifier

Selected best-performing model based on accuracy

Saved model and encoder using pickle

5. Evaluation Metrics
Accuracy Score

Confusion Matrix

Classification Report

ROC Curve (if applicable)

📊 Results & Insights
Random Forest achieved the highest accuracy in predicting churn.

Key Influencing Features: Age, Balance, Geography, and IsActiveMember

Encoding and feature scaling significantly improved model performance

✅ Conclusion
This task covered the full machine learning pipeline:

Data preprocessing

Exploratory analysis

Feature encoding and scaling

Model training and testing

Evaluation

Deployment via Streamlit

The final model helps financial institutions proactively identify customers likely to leave and retain them through better engagement.

🖥️ Streamlit Web App
Try the deployed model here:
🔗 Customer Churn Prediction App

🔗 Useful Links
Scikit-learn Documentation

Streamlit Docs

Matplotlib Docs

Seaborn Docs

🧾 Submitted as part of the Developer Hub Internship Program
