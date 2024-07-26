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
        color: #333;
    }
    .main {
        background: linear-gradient(135deg, #a2c2e1, #f0f4f7);
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        min-height: 100vh;
        padding: 20px;
    }
    .stButton>button {
        background-color: #1e90ff;  /* Warna biru cerah untuk tombol */
        color: white;
        border: none;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 8px 4px;
        cursor: pointer;
        border-radius: 20px;
        transition: background-color 0.3s ease, transform 0.3s ease;
        width: 100%;
        box-sizing: border-box;
    }
    .stButton>button:hover {
        background-color: #1c86ee;  /* Warna biru lebih gelap saat hover */
        transform: scale(1.05);
    }
    .stSelectbox, .stNumberInput, .stTextInput, .stTextArea {
        background: #ffffff; /* Background putih untuk input */
        color: #333;
        border-radius: 15px;
        border: 2px solid #cccccc; /* Border abu-abu terang */
        padding: 12px;
        margin: 12px 0;
        box-sizing: border-box;
        transition: border-color 0.3s ease;
    }
    .stSelectbox>div, .stNumberInput>div, .stTextInput>div, .stTextArea>div {
        background: #ffffff;
        color: #333;
    }
    .stSelectbox:hover, .stNumberInput:hover, .stTextInput:hover, .stTextArea:hover {
        border-color: #1e90ff; /* Border biru cerah saat hover */
    }
    .stColumns {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: space-between;
    }
    .stColumn {
        flex: 1;
        max-width: calc(50% - 20px);
    }
    .stTitle {
        font-size: 28px;
        font-weight: bold;
        color: #1e90ff;
        text-align: center;
    }
    .stWrite {
        font-size: 16px;
        color: #555;
        text-align: center;
    }
    .input-label {
        font-size: 16px;
        color: #1e90ff;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .input-label i {
        color: #1e90ff;
        font-size: 20px;
    }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)

# Mengatur elemen utama di dalam div dengan kelas 'main'
st.markdown('<div class="main">', unsafe_allow_html=True)

# Antarmuka pengguna Streamlit
st.markdown('<p class="stTitle">Weather Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="stWrite">Masukkan data cuaca untuk memprediksi jenis cuaca.</p>', unsafe_allow_html=True)

# Membagi input form menjadi dua kolom dengan 5 input di masing-masing kolom
st.markdown('<div class="stColumns">', unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="input-label"><i class="fas fa-thermometer-half"></i> Temperature (°C)</div>', unsafe_allow_html=True)
        temperature = st.number_input('')
        st.markdown('<div class="input-label"><i class="fas fa-tint"></i> Humidity (%)</div>', unsafe_allow_html=True)
        humidity = st.number_input('')
        st.markdown('<div class="input-label"><i class="fas fa-wind"></i> Wind Speed (km/h)</div>', unsafe_allow_html=True)
        wind_speed = st.number_input('')
        st.markdown('<div class="input-label"><i class="fas fa-cloud-showers-heavy"></i> Precipitation (%)</div>', unsafe_allow_html=True)
        precipitation = st.number_input('')
        st.markdown('<div class="input-label"><i class="fas fa-sun"></i> Atmospheric Pressure (hPa)</div>', unsafe_allow_html=True)
        atmospheric_pressure = st.number_input('')
    
    with col2:
        st.markdown('<div class="input-label"><i class="fas fa-cloud"></i> Cloud Cover</div>', unsafe_allow_html=True)
        cloud_cover_options = {'Clear': 0, 'Cloudy': 1, 'Overcast': 2, 'Partly Cloudy': 3}
        cloud_cover = st.selectbox('', options=list(cloud_cover_options.keys()))
        st.markdown('<div class="input-label"><i class="fas fa-calendar"></i> Season</div>', unsafe_allow_html=True)
        season_options = {'Autumn': 0, 'Spring': 1, 'Summer': 2, 'Winter': 3}
        season = st.selectbox('', options=list(season_options.keys()))
        st.markdown('<div class="input-label"><i class="fas fa-map-marker-alt"></i> Location</div>', unsafe_allow_html=True)
        location_options = {'Coastal': 0, 'Inland': 1, 'Mountain': 2}
        location = st.selectbox('', options=list(location_options.keys()))
        st.markdown('<div class="input-label"><i class="fas fa-sun"></i> UV Index</div>', unsafe_allow_html=True)
        uv_index = st.number_input('')
        st.markdown('<div class="input-label"><i class="fas fa-eye"></i> Visibility (km)</div>', unsafe_allow_html=True)
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
        st.success(f"Predicted Weather Type: {result}")
    except RuntimeError as e:
        st.error(f"An error occurred: {str(e)}")

# Menutup div dengan kelas 'main'
st.markdown('</div>', unsafe_allow_html=True)
