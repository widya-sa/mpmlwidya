import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Fungsi untuk memuat model dan melakukan prediksi
def value_predictor(to_predict_list):
    columns = [
        'Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)', 'Cloud Cover',
        'Atmospheric Pressure', 'UV Index', 'Season', 'Visibility (km)', 'Location'
    ]
    to_predict_df = pd.DataFrame([to_predict_list], columns=columns)
    
    try:
        with open('model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
        
        result = loaded_model.predict(to_predict_df)[0]
        
        weather_mapping = {
            0: 'Cloudy',
            1: 'Rainy',
            2: 'Snowy',
            3: 'Sunny'
        }
        
        return weather_mapping.get(result, 'Unknown')
    except Exception as e:
        raise RuntimeError(f"Failed to predict weather: {e}")

# Menambahkan CSS untuk background dan styling
st.markdown("""
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');
    
    body {
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-image: url('https://wallpapercave.com/wp/wp12086198.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        padding: 20px;
        color: #333;
    }
    .stButton>button {
        background-color: #f9dcc4;  /* Warna beige untuk tombol */
        color: black;               /* Warna teks hitam */
        border: none;
        padding: 15px 25px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 10px 0;
        cursor: pointer;
        border-radius: 12px;
        z-index: 10; /* Memastikan tombol berada di atas latar belakang */
        width: 100%; /* Membuat tombol penuh lebar kolom */
        box-sizing: border-box;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #f4b9a7;  /* Warna beige lebih gelap saat hover */
        transform: scale(1.05); /* Efek zoom saat hover */
    }
    .stSelectbox, .stNumberInput, .stTextInput, .stTextArea {
        background: #f9dcc4; /* Background beige */
        color: black;
        border-radius: 10px;
        border: 2px solid #f4b9a7; /* Border beige lebih gelap */
        padding: 12px;
        margin: 10px 0;
        box-sizing: border-box;
        transition: background-color 0.3s ease;
    }
    .stSelectbox>div, .stNumberInput>div, .stTextInput>div, .stTextArea>div {
        background: #f9dcc4;
        color: black;
    }
    .stColumns {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }
    .stColumn {
        flex: 1;
        max-width: calc(50% - 10px);
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.8); /* Background putih semi-transparan untuk kolom input */
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .prediction-result {
        background-color: #f9dcc4; /* Background beige untuk hasil prediksi */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-top: 20px;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        color: black;
        border: 2px solid #f4b9a7;
    }
    .input-label {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    .input-label i {
        margin-right: 10px;
        font-size: 20px;
        color: #f4b9a7;
    }
    </style>
""", unsafe_allow_html=True)

# Mengatur elemen utama di dalam div dengan kelas 'main'
st.markdown('<div class="main">', unsafe_allow_html=True)

# Antarmuka pengguna Streamlit
st.title("Weather Prediction")
st.write("Masukkan data cuaca untuk memprediksi jenis cuaca.")

# Membagi input form menjadi dua kolom dengan 5 input di masing-masing kolom
st.markdown('<div class="stColumns">', unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="input-label"><i class="fas fa-temperature-high"></i> Temperature (°C)</div>', unsafe_allow_html=True)
        temperature = st.number_input('', format="%.1f", key="temperature")
        
        st.markdown('<div class="input-label"><i class="fas fa-tachometer-alt"></i> Humidity (%)</div>', unsafe_allow_html=True)
        humidity = st.number_input('', format="%.1f", key="humidity")
        
        st.markdown('<div class="input-label"><i class="fas fa-wind"></i> Wind Speed (km/h)</div>', unsafe_allow_html=True)
        wind_speed = st.number_input('', format="%.1f", key="wind_speed")
        
        st.markdown('<div class="input-label"><i class="fas fa-cloud-showers-heavy"></i> Precipitation (%)</div>', unsafe_allow_html=True)
        precipitation = st.number_input('', format="%.1f", key="precipitation")
        
        st.markdown('<div class="input-label"><i class="fas fa-cloud"></i> Atmospheric Pressure (hPa)</div>', unsafe_allow_html=True)
        atmospheric_pressure = st.number_input('', format="%.1f", key="atmospheric_pressure")
    
    with col2:
        st.markdown('<div class="input-label"><i class="fas fa-cloud-sun"></i> Cloud Cover</div>', unsafe_allow_html=True)
        cloud_cover_options = {'Clear': 0, 'Cloudy': 1, 'Overcast': 2, 'Partly Cloudy': 3}
        cloud_cover = st.selectbox('', options=list(cloud_cover_options.keys()), key="cloud_cover")
        
        st.markdown('<div class="input-label"><i class="fas fa-calendar-season"></i> Season</div>', unsafe_allow_html=True)
        season_options = {'Autumn': 0, 'Spring': 1, 'Summer': 2, 'Winter': 3}
        season = st.selectbox('', options=list(season_options.keys()), key="season")
        
        st.markdown('<div class="input-label"><i class="fas fa-map-marker-alt"></i> Location</div>', unsafe_allow_html=True)
        location_options = {'Coastal': 0, 'Inland': 1, 'Mountain': 2}
        location = st.selectbox('', options=list(location_options.keys()), key="location")
        
        st.markdown('<div class="input-label"><i class="fas fa-sun"></i> UV Index</div>', unsafe_allow_html=True)
        uv_index = st.number_input('', format="%.1f", key="uv_index")
        
        st.markdown('<div class="input-label"><i class="fas fa-eye"></i> Visibility (km)</div>', unsafe_allow_html=True)
        visibility = st.number_input('', format="%.1f", key="visibility")

st.markdown('</div>', unsafe_allow_html=True)

# Tombol prediksi
if st.button('Predict'):
    to_predict_list = [
        temperature, humidity, wind_speed, precipitation,
        cloud_cover_options[cloud_cover], atmospheric_pressure, uv_index,
        season_options[season], visibility, location_options[location]
    ]
    
    try:
        result = value_predictor(to_predict_list)
        st.markdown(f'<div class="prediction-result">Predicted Weather Type: {result}</div>', unsafe_allow_html=True)
    except RuntimeError as e:
        st.error(f"An error occurred: {str(e)}")

# Menutup div dengan kelas 'main'
st.markdown('</div>', unsafe_allow_html=True)
