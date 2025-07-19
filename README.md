# 📘 DeveloperHub Task 3 – Customer Churn Prediction using ML

## 📌 Task Objective

This task focuses on building a classification model to identify bank customers who are likely to leave (churn) based on their demographic and account activity data using supervised machine learning.

---

## 📁 Dataset

- **Name:** Churn Modelling Dataset  
- **Source:** [Kaggle – Churn Modelling Dataset](https://www.kaggle.com/datasets/shubhendra7/customer-churn-prediction)

---

## 📊 Features

| Feature          | Description                        |
|------------------|------------------------------------|
| CreditScore      | Customer's credit score            |
| Geography        | Country of residence               |
| Gender           | Male or Female                     |
| Age              | Age of the customer                |
| Tenure           | Number of years with the bank      |
| Balance          | Account balance                    |
| NumOfProducts    | Number of products with the bank   |
| HasCrCard        | Whether they have a credit card    |
| IsActiveMember   | Whether they are active            |
| EstimatedSalary  | Estimated salary in dollars        |

### 🎯 Target

- `Exited`:  
  - 1 = Churned  
  - 0 = Not Churned

---

## 🛠️ Tools & Libraries Used

- `Pandas` – Data loading & cleaning  
- `Matplotlib & Seaborn` – Visualizations  
- `Scikit-learn` – Model training and evaluation  
- `Streamlit` – Web-based app interface  
- `Pickle` – Saving trained model and encoder

---

## 🚀 Approach

### 1. Dataset Loading & Understanding
- Loaded the dataset using `pandas.read_csv()`
- Inspected data using `.head()`, `.info()`, `.describe()`

### 2. Data Cleaning & Preparation
- Removed irrelevant columns: `RowNumber`, `CustomerId`, `Surname`
- Encoded categorical variables:
  - `Geography`, `Gender` using `LabelEncoder`
- Scaled numerical features with `StandardScaler`

### 3. Exploratory Data Analysis (EDA)
- Count plots for `Geography`, `Gender`, and `IsActiveMember`
- Histograms for numerical features
- Heatmap of feature correlations
- Churn distribution analysis

### 4. Model Training & Evaluation
- Data split: 80% training / 20% testing
- Trained multiple classifiers:
  - Logistic Regression
  - Decision Tree Classifier
  - Random Forest Classifier
- Best model (Random Forest) saved using `pickle`
- Also saved the encoder (`encoder.pkl`) for real-time prediction use

### 5. Evaluation Metrics
- Accuracy Score
- Confusion Matrix
- Classification Report
- Feature Importance (from Random Forest)

---

## 📊 Results & Insights

- **Best Model:** Random Forest Classifier
- **Key Influential Features:**
  - Age
  - Geography
  - Balance
  - IsActiveMember

#### 🔍 Insights:
- Customers who are older, inactive, and have a high balance tend to churn more
- Geography impacts churn – some regions had higher churn rates

---

## ✅ Conclusion

This project demonstrates a complete ML pipeline:

- Data preprocessing & transformation  
- EDA and visualization  
- Multiple model training & selection  
- Model evaluation with metrics  
- Real-time deployment using Streamlit

The model can assist banks in proactive retention strategies by flagging potential churners early.

---

## 🖥️ Streamlit Web App

Try the deployed app here:  
🔗 [Customer Churn Prediction App](https://customer-churn-prediction-app-eappheqvayifhc9cou8ytwv.streamlit.app/)


