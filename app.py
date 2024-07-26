import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Fungsi untuk memuat model dan melakukan prediksi
def value_predictor(to_predict_list):
    # Membentuk DataFrame dari list input
    to_predict_df = pd.DataFrame([to_predict_list], columns=[
        'Temperature', 'Humidity', 'Wind Speed', 'Precipitation', 'Cloud Cover',
        'Atmospheric Pressure', 'UV Index', 'Season', 'Visibility', 'Location'
    ])
    
    try:
        # Memuat model dari file
        with open('model.pkl', 'rb') as file:
            loaded_model = joblib.load(file)
        
        # Melakukan prediksi
        result = loaded_model.predict(to_predict_df)[0]
        
        # Pemetaan hasil prediksi ke kategori cuaca
        weather_mapping = {
            0: 'Cloudy',
            1: 'Rainy',
            2: 'Snowy',
            3: 'Sunny'
        }
        
        # Mengembalikan kategori cuaca sesuai hasil prediksi
        return weather_mapping.get(result, 'Unknown')
    except Exception as e:
        # Menangani error saat memuat model atau prediksi
        raise RuntimeError(f"Failed to predict weather: {e}")

# Antarmuka pengguna Streamlit
st.title("Weather Prediction")
st.write("Masukkan data cuaca untuk memprediksi jenis cuaca.")

# Input form
temperature = st.number_input('Temperature (°C)')
humidity = st.number_input('Humidity (%)')
wind_speed = st.number_input('Wind Speed (km/h)')
precipitation = st.number_input('Precipitation (%)')

cloud_cover = st.selectbox('Cloud Cover', options={
    'Clear': 0,
    'Cloudy': 1,
    'Overcast': 2,
    'Partly Cloudy': 3
})

atmospheric_pressure = st.number_input('Atmospheric Pressure (hPa)')
season = st.selectbox('Season', options={
    'Autumn': 0,
    'Spring': 1,
    'Summer': 2,
    'Winter': 3
})

location = st.selectbox('Location', options={
    'Coastal': 0,
    'Inland': 1,
    'Mountain': 2
})

uv_index = st.number_input('UV Index')
visibility = st.number_input('Visibility (km)')

# Tombol prediksi
if st.button('Predict'):
    to_predict_list = [
        temperature, humidity, wind_speed, precipitation,
        cloud_cover, atmospheric_pressure, uv_index, season,
        visibility, location
    ]
    
    try:
        result = value_predictor(to_predict_list)
        st.success(f"Predicted Weather Type: {result}")
    except RuntimeError as e:
        st.error(f"An error occurred: {str(e)}")
