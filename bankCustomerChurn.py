import pandas as pd
import numpy as np
import joblib
import streamlit as st

customer_churn_model_pkl = r"C:\Users\Lenovo\OneDrive\Desktop\Juypter_projects\bank_customer_churn_model.pkl"
loaded_model = joblib.load(customer_churn_model_pkl)

st.header("Bank Customer Churn Prediction")


CreditScore = st.number_input("Enter the your Credit Score", min_value=300, max_value=850)

Geography = st.selectbox("Enter your country name ", ("France", "Spain", "Germany"))
Geography_dict = {"France":0, "Spain":1, "Germany":2}
Geography = Geography_dict[Geography]

Gender = st.selectbox("Enter the Sex ", ("Male", "Female"))
Gender_dict = {"Male":0, "Female":1}
Gender = Gender_dict[Gender ]

Age = st.number_input("Enter the Age", min_value=18, max_value=100)

Tenure = st.number_input("Enter your tenure in the bank", min_value=0, max_value=10)

Balance = st.number_input("Enter the Balance you have in the bank")

NumOfProducts = st.number_input("Enter the number of products you have in the bank", min_value=1, max_value=4)

HasCrCard = st.selectbox("Do you have Credit Card ", ("No", "Yes"))
HasCrCard_dict = {"No":0, "Yes":1}
HasCrCard = HasCrCard_dict[HasCrCard ]

IsActiveMember = st.selectbox("You are active member in the bank ", ("No", "Yes"))
IsActiveMember_dict = {"No":0, "Yes":1}
IsActiveMember = IsActiveMember_dict[IsActiveMember ]

EstimatedSalary = st.number_input("Enter the estimated salary", min_value=0.0, value=50000.0)

X_new = np.array([[CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]])

button = st.button("Submit")

if button:
    # Make the prediction using the loaded model
    result = loaded_model.predict(X_new)
    result = np.round(result[0])

    # Display the prediction result in a user-friendly way
    if result == 1:
        st.info("The customer is likely to churn.")
    else:
        st.info("The customer is unlikely to churn.")


