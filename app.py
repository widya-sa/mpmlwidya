import streamlit as st
import numpy as np
import joblib

# Load the pre-trained model
model = joblib.load('model_with_smote_enn.sav')

# Define a function for prediction
def predict_weather(inputs):
    prediction = model.predict([inputs])
    weather_mapping = {
        0: 'Cloudy',
        1: 'Rainy',
        2: 'Snowy',
        3: 'Sunny'
    }
    return weather_mapping.get(prediction[0], 'Unknown')

# Streamlit app
st.title("Weather Prediction by Widya S.A.")

# Input fields
temperature = st.number_input("Temperature", format="%.2f")
humidity = st.number_input("Humidity", format="%.2f")
wind_speed = st.number_input("Wind Speed", format="%.2f")
precipitation = st.number_input("Precipitation (%)", format="%.2f")
cloud_cover = st.selectbox("Cloud Cover", [0, 1, 2, 3])
atmospheric_pressure = st.number_input("Atmospheric Pressure", format="%.2f")
uv_index = st.number_input("UV Index", format="%.2f")
season = st.selectbox("Season", [0, 1, 2, 3])
visibility = st.number_input("Visibility (km)", format="%.2f")
location = st.selectbox("Location", [0, 1, 2])

# Predict button
if st.button("Submit"):
    inputs = [temperature, humidity, wind_speed, precipitation, cloud_cover, atmospheric_pressure, uv_index, season, visibility, location]
    result = predict_weather(inputs)
    st.write(f"The predicted weather is: {result}")
