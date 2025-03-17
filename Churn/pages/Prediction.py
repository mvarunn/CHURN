import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model and encoder
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct paths relative to the script directory
model_path = os.path.join(script_dir, '../ChurnClassifier.pkl')
encoder_path = os.path.join(script_dir, '../LabelEncoder.pkl')

# Load model and encoder
model = joblib.load(model_path)
encoder = joblib.load(encoder_path)


# Load the trained model and encoder
# import os
# model_path = os.path.abspath('../Model/ChurnClassifier.pkl')
# model = joblib.load(model_path)

# model = joblib.load('Model\ChurnClassifier.pkl')

# Function to make predictions
def predict_churn(input_data):
    prediction = model.predict([input_data])
    return prediction

# Streamlit UI
st.title('Customer Churn Prediction')

st.write("""
### Please enter the following details to predict customer churn:
""")

# Input fields for the user to fill in (based on your dataset columns)
city = st.selectbox('City', [
    'Los Angeles', 'San Diego', 'San Jose', 'Sacramento', 'San Francisco', 
    'Fresno', 'Long Beach', 'Oakland', 'Stockton', 'Bakersfield', 
    'Glendale', 'Riverside', 'Berkeley', 'Whittier', 'Pasadena', 
    'Santa Barbara', 'Anaheim', 'San Bernardino', 'Modesto', 'Irvine'
])

from sklearn.preprocessing import LabelEncoder

# List of cities (same as during training)
cities = [
    'Los Angeles', 'San Diego', 'San Jose', 'Sacramento', 'San Francisco', 
    'Fresno', 'Long Beach', 'Oakland', 'Stockton', 'Bakersfield', 
    'Glendale', 'Riverside', 'Berkeley', 'Whittier', 'Pasadena', 
    'Santa Barbara', 'Anaheim', 'San Bernardino', 'Modesto', 'Irvine'
]

# Fit the encoder here
# encoder_path = os.path.abspath('../Model/LabelEncoder.pkl')
# encoder = joblib.load(encoder_path)
# encoder = joblib.load('Model\LabelEncoder.pkl') 
encoder.fit(cities)

# Encode the selected city
encoded_city = encoder.transform([city])[0]

latitude = st.number_input('Latitude', format="%.6f")
longitude = st.number_input('Longitude', format="%.6f")
gender = st.selectbox('Gender', ['Male', 'Female'])
senior_citizen = st.selectbox('Senior Citizen', ['Yes', 'No'])
partner = st.selectbox('Partner', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['Yes', 'No'])
tenure_months = st.slider('Tenure (Months)', 0, 72, 12)
phone_service = st.selectbox('Phone Service', ['Yes', 'No'])
multiple_lines = st.selectbox('Multiple Lines', ['Yes', 'No', 'No phone service'])
internet_service = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
online_backup = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
device_protection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
tech_support = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])
streaming_tv = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])
streaming_movies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'])
contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
paperless_billing = st.selectbox('Paperless Billing', ['Yes', 'No'])
payment_method = st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly_charges = st.slider('Monthly Charges', 20.0, 120.0, 70.0)
total_charges = st.slider('Total Charges', 20.0, 1000.0, 500.0)
churn_score = st.slider('Churn Score', 0.0, 100.0, 50.0)
cltv = st.slider('CLTV', 1000.0, 10000.0, 5500.0)

# Preparing the input data for prediction (the order should match the model's training features)
input_data = [
    encoded_city, latitude, longitude,
    1 if gender == 'Male' else 0,
    1 if senior_citizen == 'Yes' else 0,
    1 if partner == 'Yes' else 0,
    1 if dependents == 'Yes' else 0,
    tenure_months,
    1 if phone_service == 'Yes' else 0,
    1 if multiple_lines == 'Yes' else 0,
    1 if internet_service == 'DSL' else (2 if internet_service == 'Fiber optic' else 0),
    1 if online_security == 'Yes' else 0,
    1 if online_backup == 'Yes' else 0,
    1 if device_protection == 'Yes' else 0,
    1 if tech_support == 'Yes' else 0,
    1 if streaming_tv == 'Yes' else 0,
    1 if streaming_movies == 'Yes' else 0,
    1 if contract == 'One year' else (2 if contract == 'Two year' else 0),
    1 if paperless_billing == 'Yes' else 0,
    1 if payment_method == 'Electronic check' else (2 if payment_method == 'Bank transfer (automatic)' else (3 if payment_method == 'Credit card (automatic)' else 0)),
    monthly_charges,
    total_charges,
    churn_score,
    cltv
]

# Button to trigger prediction
if st.button('Predict Churn'):
    prediction = predict_churn(input_data)
    if prediction == 1:
        st.write("#### This customer is likely to churn.")
    else:
        st.write("#### This customer is likely to stay.")
