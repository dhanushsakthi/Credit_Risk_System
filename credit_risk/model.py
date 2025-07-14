import streamlit as st
import pickle
import numpy as np

with open(r"C:\Users\Lab\Downloads\credit_risk\model_selection.pkl","rb") as model_file:
    model=pickle.load(model_file)

st.title("Credit Risk System")
st.write("Enter the flower measurements to classify the species.")

person_age = st.slider("person_age", min_value=15.0, max_value=100.0, step=1.0)
person_income = st.slider("person_income", min_value=25000.0, max_value=100000.0, step=1.0)
person_home_ownership = st.slider("person_home_ownership",min_value=0.0, max_value=1.0, step=1.0)
person_emp_length=st.slider("  person_emp_length",min_value=15.0, max_value=100.0, step=1.0)
loan_grade = st.slider("loan_grade",min_value=282.0, max_value=1080.0, step=1.0)
loan_amnt = st.slider("loan_amnt", min_value=15000.0, max_value=200000.0, step=1.1)
loan_int_rate = st.slider("loan_int_rate", min_value=9.99, max_value=24.0, step=1.1)
loan_percent_income=st.slider("loan_percent_income", min_value=9.99, max_value=24.0, step=1.1)
cb_person_default_on_file = st.slider("cb_person_default_on_file",min_value=2.0, max_value=30.0, step=1.0)
cb_person_cred_hist_length = st.slider("cb_person_cred_hist_length", min_value=2.0, max_value=30.0, step=1.0)
loan_intent=st.slider("loan_intent",min_value=442.0, max_value=340.0, step=1.0,key="cb_person_cred_hist_length_slider")
loan_intent_HOMEIMPROVEMENT=st.slider("loan_intent_HOMEIMPROVEMENT",min_value=15.0, max_value=100.0, step=1.0)
loan_intent_EDUCATION=st.slider("loan_intent_EDUCATION", min_value=9.99, max_value=24.0, step=1.1)
loan_intent_MEDICAL=st.slider("loan_intent_MEDICA", min_value=15.0, max_value=100.0, step=1.0)
loan_intent_PERSONAL=st.slider("loan_intent_PERSONAL", min_value=15.0, max_value=100.0, step=1.0)
loan_intent_VENTURE=st.slider("loan_intent_VENTURE", min_value=15.0, max_value=100.0, step=1.0)

if st.button("Predict"):
    features = np.array([[person_age,person_income,person_home_ownership,person_emp_length,loan_grade,loan_amnt,loan_int_rate,cb_person_default_on_file,cb_person_cred_hist_length,loan_intent,loan_intent_HOMEIMPROVEMENT,loan_intent_EDUCATION,loan_intent_MEDICAL,loan_intent_PERSONAL,loan_intent_VENTURE]])
    prediction = model.predict(features)
    st.write(f"Predicted value: {prediction[0]}")
    