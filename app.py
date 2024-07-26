import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load('model_with_smote_enn.sav')

# Streamlit app
st.title("Weather Prediction by Widya S.A.")

def predict_weather(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, -1)
    result = model.predict(to_predict)[0]
    weather_mapping = {
        0: 'Cloudy',
        1: 'Rainy',
        2: 'Snowy',
        3: 'Sunny'
    }
    return weather_mapping.get(result, 'Unknown')

# Input fields
temperature = st.number_input("Temperature", format="%.2f")
humidity = st.number_input("Humidity", format="%.2f")
wind_speed = st.number_input("Wind Speed", format="%.2f")
precipitation = st.number_input("Precipitation (%)", format="%.2f")
cloud_cover = st.selectbox("Cloud Cover", [0, 1, 2, 3], format_func=lambda x: ["Clear", "Cloudy", "Overcast", "Partly Cloudy"][x])
atmospheric_pressure = st.number_input("Atmospheric Pressure", format="%.2f")
uv_index = st.number_input("UV Index", format="%.2f")
season = st.selectbox("Season", [0, 1, 2, 3], format_func=lambda x: ["Autumn", "Spring", "Summer", "Winter"][x])
visibility = st.number_input("Visibility (km)", format="%.2f")
location = st.selectbox("Location", [0, 1, 2], format_func=lambda x: ["Coastal", "Inland", "Mountain"][x])

# Button to predict
if st.button("Submit"):
    to_predict_list = [
        temperature, humidity, wind_speed, precipitation, cloud_cover,
        atmospheric_pressure, uv_index, season, visibility, location
    ]
    result = predict_weather(to_predict_list)
    st.write(f"The predicted weather is: {result}")
