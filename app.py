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
        temperature = st.number_input('Temperature (°C)', format="%.1f")
        humidity = st.number_input('Humidity (%)', format="%.1f")
        wind_speed = st.number_input('Wind Speed (km/h)', format="%.1f")
        precipitation = st.number_input('Precipitation (%)', format="%.1f")
        atmospheric_pressure = st.number_input('Atmospheric Pressure (hPa)', format="%.1f")
    
    with col2:
        cloud_cover_options = {'Clear': 0, 'Cloudy': 1, 'Overcast': 2, 'Partly Cloudy': 3}
        cloud_cover = st.selectbox('Cloud Cover', options=list(cloud_cover_options.keys()))
        season_options = {'Autumn': 0, 'Spring': 1, 'Summer': 2, 'Winter': 3}
        season = st.selectbox('Season', options=list(season_options.keys()))
        location_options = {'Coastal': 0, 'Inland': 1, 'Mountain': 2}
        location = st.selectbox('Location', options=list(location_options.keys()))
        uv_index = st.number_input('UV Index', format="%.1f")
        visibility = st.number_input('Visibility (km)', format="%.1f")

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
