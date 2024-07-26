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
    .main {
        background-image: url('https://wallpapercave.com/wp/wp12086198.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stButton>button {
        background-color: #f9dcc4;  /* Warna beige untuk tombol */
        color: black;               /* Warna teks hitam */
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
        width: 100%; /* Membuat tombol penuh lebar kolom */
        box-sizing: border-box;
    }
    .stButton>button:hover {
        background-color: #f4b9a7;  /* Warna beige lebih gelap saat hover */
    }
    .stSelectbox, .stNumberInput, .stTextInput, .stTextArea {
        background: #f9dcc4; /* Background beige */
        color: black;
        border-radius: 10px;
        border: 2px solid #f4b9a7; /* Border beige lebih gelap */
        padding: 10px;
        margin: 10px 0;
        box-sizing: border-box;
        display: flex;
        align-items: center;
    }
    .stSelectbox img, .stNumberInput img, .stTextInput img, .stTextArea img {
        margin-right: 10px; /* Jarak antara ikon dan teks input */
        height: 24px; /* Ukuran ikon */
        width: 24px;
    }
    .stSelectbox>div, .stNumberInput>div, .stTextInput>div, .stTextArea>div {
        background: #f9dcc4;
        color: black;
        display: flex;
        align-items: center;
    }
    .stColumns {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }
    .stColumn {
        flex: 1;
        max-width: calc(50% - 10px);
    }
    .prediction-result {
        background-color: #f9dcc4; /* Background beige untuk hasil prediksi */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-top: 20px;
        font-size: 18px;
        text-align: center;
        color: black;
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
        st.markdown('<div><img src="https://example.com/temperature-icon.png" alt="Temp Icon">Temperature (°C)</div>', unsafe_allow_html=True)
        temperature = st.number_input('')
        st.markdown('<div><img src="https://example.com/humidity-icon.png" alt="Humidity Icon">Humidity (%)</div>', unsafe_allow_html=True)
        humidity = st.number_input('')
        st.markdown('<div><img src="https://example.com/wind-speed-icon.png" alt="Wind Speed Icon">Wind Speed (km/h)</div>', unsafe_allow_html=True)
        wind_speed = st.number_input('')
        st.markdown('<div><img src="https://example.com/precipitation-icon.png" alt="Precipitation Icon">Precipitation (%)</div>', unsafe_allow_html=True)
        precipitation = st.number_input('')
        st.markdown('<div><img src="https://example.com/atmospheric-pressure-icon.png" alt="Pressure Icon">Atmospheric Pressure (hPa)</div>', unsafe_allow_html=True)
        atmospheric_pressure = st.number_input('')
    
    with col2:
        st.markdown('<div><img src="https://example.com/cloud-cover-icon.png" alt="Cloud Cover Icon">Cloud Cover</div>', unsafe_allow_html=True)
        cloud_cover_options = {'Clear': 0, 'Cloudy': 1, 'Overcast': 2, 'Partly Cloudy': 3}
        cloud_cover = st.selectbox('', options=list(cloud_cover_options.keys()))
        st.markdown('<div><img src="https://example.com/season-icon.png" alt="Season Icon">Season</div>', unsafe_allow_html=True)
        season_options = {'Autumn': 0, 'Spring': 1, 'Summer': 2, 'Winter': 3}
        season = st.selectbox('', options=list(season_options.keys()))
        st.markdown('<div><img src="https://example.com/location-icon.png" alt="Location Icon">Location</div>', unsafe_allow_html=True)
        location_options = {'Coastal': 0, 'Inland': 1, 'Mountain': 2}
        location = st.selectbox('', options=list(location_options.keys()))
        st.markdown('<div><img src="https://example.com/uv-index-icon.png" alt="UV Index Icon">UV Index</div>', unsafe_allow_html=True)
        uv_index = st.number_input('')
        st.markdown('<div><img src="https://example.com/visibility-icon.png" alt="Visibility Icon">Visibility (km)</div>', unsafe_allow_html=True)
        visibility = st.number_input('')

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
