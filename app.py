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

# Menambahkan CSS untuk background, styling, dan ikon
st.markdown("""
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');
    
    .main {
        background-image: url('https://wallpapercave.com/wp/wp12086198.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
        height: 100vh; /* Memastikan tinggi sesuai dengan viewport */
        overflow: auto;
        padding: 20px; /* Menambahkan padding agar konten tidak menempel pada tepi */
    }
    .stButton>button {
        background-color: #4CAF50;  /* Warna hijau untuk tombol */
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        z-index: 10; /* Memastikan tombol berada di atas latar belakang */
        width: 100%; /* Lebar penuh tombol */
    }
    .stButton>button:hover {
        background-color: #45a049;  /* Warna hijau lebih gelap saat hover */
    }
    .stSelectbox, .stNumberInput, .stTextInput, .stTextArea {
        background: #f9dcc4; /* Background beige */
        color: black;
        border-radius: 10px;
        border: 2px solid #f4b9a7; /* Border beige lebih gelap */
        padding: 10px;
        margin: 10px 0;
        box-sizing: border-box;
        width: 100%; /* Lebar penuh input */
    }
    .input-container {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
        background: #f9dcc4;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #f4b9a7;
        width: 100%; /* Lebar penuh input container */
    }
    .input-container i {
        font-size: 20px;
        color: black; /* Warna ikon */
        margin-right: 10px;
    }
    .input-label {
        font-weight: bold;
        color: black; /* Warna label */
        margin-right: 10px;
    }
    .input-row {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        margin-bottom: 20px;
    }
    .input-col {
        flex: 1;
        max-width: calc(50% - 10px); /* Lebar kolom 50% dari container */
    }
    </style>
""", unsafe_allow_html=True)

# Mengatur elemen utama di dalam div dengan kelas 'main'
st.markdown('<div class="main">', unsafe_allow_html=True)

# Antarmuka pengguna Streamlit
st.title("Weather Prediction")
st.write("Masukkan data cuaca untuk memprediksi jenis cuaca.")

# Membagi input form menjadi dua kolom dengan 5 input di masing-masing kolom
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="input-row">', unsafe_allow_html=True)
    temperature = st.number_input('Temperature (°C)')
    humidity = st.number_input('Humidity (%)')
    wind_speed = st.number_input('Wind Speed (km/h)')
    precipitation = st.number_input('Precipitation (%)')
    atmospheric_pressure = st.number_input('Atmospheric Pressure (hPa)')
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="input-row">', unsafe_allow_html=True)
    cloud_cover_options = {'Clear': 0, 'Cloudy': 1, 'Overcast': 2, 'Partly Cloudy': 3}
    cloud_cover = st.selectbox('Cloud Cover', options=list(cloud_cover_options.keys()))
    season_options = {'Autumn': 0, 'Spring': 1, 'Summer': 2, 'Winter': 3}
    season = st.selectbox('Season', options=list(season_options.keys()))
    location_options = {'Coastal': 0, 'Inland': 1, 'Mountain': 2}
    location = st.selectbox('Location', options=list(location_options.keys()))
    uv_index = st.number_input('UV Index')
    visibility = st.number_input('Visibility (km)')
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
        st.success(f"Predicted Weather Type: {result}")
    except RuntimeError as e:
        st.error(f"An error occurred: {str(e)}")

# Menutup div dengan kelas 'main'
st.markdown('</div>', unsafe_allow_html=True)
