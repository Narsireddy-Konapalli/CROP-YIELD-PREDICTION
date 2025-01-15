import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load("crop_model.pkl")

# Set the title of the app
st.title("Crop Yield Prediction")

# Create columns for the form layout
col1, col2 = st.columns(2)  # Two columns for the first row

# First row: Temperature, Rainfall
with col1:
    temperature = st.number_input("Enter Temperature value:",value=0.0, format="%.2f")

with col2:
    rainfall = st.number_input("Enter Rainfall value:", value=0.0, format="%.2f")

# Second row: Humidity, Crop Type
col3, col4 = st.columns(2)  # Two columns for the second row

with col3:
    humidity = st.number_input("Enter Humidity value:", value=0.0, format="%.2f")

with col4:
    crop_type = st.selectbox(
        "Select Crop Type:",
        ['Barley', 'Corn', 'Wheat', 'Soybeans', 'Rice']
    )

# Third row: Soil Type, Weather Condition
col5, col6 = st.columns(2)  # Two columns for the third row

with col5:
    soil_type = st.selectbox(
        "Select Soil Type:",
        ['Sandy', 'Loamy', 'Peaty', 'Clay', 'Silty']
    )

with col6:
    weather_condition = st.selectbox(
        "Select Weather Condition:",
        ['Sunny', 'Rainy', 'Stormy', 'Cloudy']
    )

# Button to make prediction
if st.button("Predict"):
    input_data = pd.DataFrame({
        'Numerical1': [temperature],
        'Numerical2': [rainfall],
        'Numerical3': [humidity],
        'Crop_Type': [crop_type],
        'Soil_Type': [soil_type],
        'Weather_Condition': [weather_condition]
    })

    # One-hot encoding for categorical variables
    encoded_data = pd.get_dummies(input_data, columns=['Crop_Type', 'Soil_Type', 'Weather_Condition'])
    
    # Ensure all columns are in the correct order
    expected_columns = [
        'temperature', 'rainfall', 'humidity',
        'Crop_Type_Barley', 'Crop_Type_Corn', 'Crop_Type_Wheat', 'Crop_Type_Soybeans', 'Crop_Type_Rice',
        'Soil_Type_Sandy', 'Soil_Type_Loamy', 'Soil_Type_Peaty', 'Soil_Type_Clay', 'Soil_Type_Silty',
        'Weather_Condition_Sunny', 'Weather_Condition_Rainy', 'Weather_Condition_Stormy', 'Weather_Condition_Cloudy'
    ]
    
    for col in expected_columns:
        if col not in encoded_data.columns:
            encoded_data[col] = 0
    encoded_data = encoded_data[expected_columns]

    # Prepare the feature list for prediction
    feature_list = []
    for value in encoded_data.iloc[0]:
        feature_list.append(value if isinstance(value, (int, float)) else bool(value))

    # Function to make a prediction
    def predict_from_list(feature_list):
        feature_array = np.array(feature_list).reshape(1, -1)
        prediction = model.predict(feature_array)
        return prediction[0]

    # Get the predicted crop yield
    predicted_value = predict_from_list(feature_list)

    # Display the prediction result
    st.success(f"Predicted Crop Yield (tons/hectare): {predicted_value:.2f}")
