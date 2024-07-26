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
        padding: 20px; /* Menambahkan padding untuk ruang di sekeliling konten */
    }
    .stButton>button {
        background-color: #f9dcc4;  /* Warna beige untuk tombol */
        color: black;
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
        background-color: #f4b9a7;  /* Warna beige lebih gelap saat hover */
    }
    .input-container {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
        background: #f9dcc4; /* Background beige */
        border-radius: 10px;
        border: 2px solid #f4b9a7; /* Border beige lebih gelap */
        padding: 10px;
        width: 100%; /* Lebar penuh container input */
        box-sizing: border-box;
    }
    .input-container i {
        font-size: 20px;
        color: black; /* Warna ikon */
        margin-right: 10px;
    }
    .input-container label {
        flex: 1;
        margin-right: 10px;
        color: black; /* Warna teks label */
        font-weight: bold;
    }
    .input-container input, .input-container select {
        background: #f9dcc4;
        color: black;
        border: none;
        border-radius: 5px;
        padding: 10px;
        width: 100%; /* Lebar penuh input */
        box-sizing: border-box;
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
    
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('<label for="temperature"><i class="fas fa-temperature-high"></i> Temperature (°C)</label>', unsafe_allow_html=True)
    temperature = st.number_input('', key='temperature')
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('<label for="humidity"><i class="fas fa-tint"></i> Humidity (%)</label>', unsafe_allow_html=True)
    humidity = st.number_input('', key='humidity')
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('<label for="wind_speed"><i class="fas fa-wind"></i> Wind Speed (km/h)</label>', unsafe_allow_html=True)
    wind_speed = st.number_input('', key='wind_speed')
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('<label for="precipitation"><i class="fas fa-cloud-showers-heavy"></i> Precipitation (%)</label>', unsafe_allow_html=True)
    precipitation = st.number_input('', key='precipitation')
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('<label for="atmospheric_pressure"><i class="fas fa-cloud"></i> Atmospheric Pressure (hPa)</label>', unsafe_allow_html=True)
    atmospheric_pressure = st.number_input('', key='atmospheric_pressure')
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="input-row">', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('<label for="cloud_cover"><i class="fas fa-cloud"></i> Cloud Cover</label>', unsafe_allow_html=True)
    cloud_cover_options = {'Clear': 0, 'Cloudy': 1, 'Overcast': 2, 'Partly Cloudy': 3}
    cloud_cover = st.selectbox('', options=list(cloud_cover_options.keys()), key='cloud_cover')
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('<label for="season"><i class="fas fa-calendar-season"></i> Season</label>', unsafe_allow_html=True)
    season_options = {'Autumn': 0, 'Spring': 1, 'Summer': 2, 'Winter': 3}
    season = st.selectbox('', options=list(season_options.keys()), key='season')
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('<label for="location"><i class="fas fa-map-marker-alt"></i> Location</label>', unsafe_allow_html=True)
    location_options = {'Coastal': 0, 'Inland': 1, 'Mountain': 2}
    location = st.selectbox('', options=list(location_options.keys()), key='location')
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('<label for="uv_index"><i class="fas fa-sun"></i> UV Index</label>', unsafe_allow_html=True)
    uv_index = st.number_input('', key='uv_index')
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('<label for="visibility"><i class="fas fa-eye"></i> Visibility (km)</label>', unsafe_allow_html=True)
    visibility = st.number_input('', key='visibility')
    st.markdown('</div>', unsafe_allow_html=True)

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
