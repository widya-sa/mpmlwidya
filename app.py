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
    .main {
        background-image: url('https://wallpapercave.com/wp/wp12086198.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        padding: 20px;
        color: white;
        min-height: 100vh;
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
    .stSelectbox>div, .stNumberInput>div, .stTextInput>div, .stTextArea>div {
        background: #f9dcc4;
        color: black;
        display: flex;
        align-items: center;
    }
    .icon {
        margin-right: 10px;
        font-size: 20px; /* Ukuran ikon */
        color: black; /* Warna ikon */
    }
    .title {
        display: flex;
        align-items: center;
        gap: 10px; /* Spasi antara ikon dan teks */
    }
    .fa-sun {
        color: black; /* Warna ikon matahari hitam */
        font-size: 24px; /* Ukuran ikon */
    }
    </style>
""", unsafe_allow_html=True)

# Mengatur elemen utama di dalam div dengan kelas 'main'
st.markdown('<div class="main">', unsafe_allow_html=True)

# Antarmuka pengguna Streamlit
st.markdown('<div class="title"><i class="fa fa-sun"></i><h1>Weather Prediction</h1></div>', unsafe_allow_html=True)
st.write("Masukkan data cuaca untuk memprediksi jenis cuaca.")

# Membagi input form menjadi dua kolom dengan 5 input di masing-masing kolom
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="stSelectbox"><i class="fa fa-thermometer-half icon"></i>' +
                '<input type="number" placeholder="Temperature (°C)" /></div>', unsafe_allow_html=True)
    temperature = st.number_input('', format='%d')
    
    st.markdown('<div class="stSelectbox"><i class="fa fa-tint icon"></i>' +
                '<input type="number" placeholder="Humidity (%)" /></div>', unsafe_allow_html=True)
    humidity = st.number_input('', format='%d')
    
    st.markdown('<div class="stSelectbox"><i class="fa fa-wind icon"></i>' +
                '<input type="number" placeholder="Wind Speed (km/h)" /></div>', unsafe_allow_html=True)
    wind_speed = st.number_input('', format='%d')
    
    st.markdown('<div class="stSelectbox"><i class="fa fa-cloud-rain icon"></i>' +
                '<input type="number" placeholder="Precipitation (%)" /></div>', unsafe_allow_html=True)
    precipitation = st.number_input('', format='%d')
    
    st.markdown('<div class="stSelectbox"><i class="fa fa-cloud icon"></i>' +
                '<input type="number" placeholder="Atmospheric Pressure (hPa)" /></div>', unsafe_allow_html=True)
    atmospheric_pressure = st.number_input('', format='%d')

with col2:
    st.markdown('<div class="stSelectbox"><i class="fa fa-cloud icon"></i>' +
                '<select><option value="0">Clear</option><option value="1">Cloudy</option><option value="2">Overcast</option><option value="3">Partly Cloudy</option></select></div>', unsafe_allow_html=True)
    cloud_cover_options = {'Clear': 0, 'Cloudy': 1, 'Overcast': 2, 'Partly Cloudy': 3}
    cloud_cover = st.selectbox('', options=list(cloud_cover_options.keys()))
    
    st.markdown('<div class="stSelectbox"><i class="fa fa-calendar icon"></i>' +
                '<select><option value="0">Autumn</option><option value="1">Spring</option><option value="2">Summer</option><option value="3">Winter</option></select></div>', unsafe_allow_html=True)
    season_options = {'Autumn': 0, 'Spring': 1, 'Summer': 2, 'Winter': 3}
    season = st.selectbox('', options=list(season_options.keys()))
    
    st.markdown('<div class="stSelectbox"><i class="fa fa-map-marker-alt icon"></i>' +
                '<select><option value="0">Coastal</option><option value="1">Inland</option><option value="2">Mountain</option></select></div>', unsafe_allow_html=True)
    location_options = {'Coastal': 0, 'Inland': 1, 'Mountain': 2}
    location = st.selectbox('', options=list(location_options.keys()))
    
    st.markdown('<div class="stSelectbox"><i class="fa fa-sun icon"></i>' +
                '<input type="number" placeholder="UV Index" /></div>', unsafe_allow_html=True)
    uv_index = st.number_input('', format='%d')
    
    st.markdown('<div class="stSelectbox"><i class="fa fa-eye icon"></i>' +
                '<input type="number" placeholder="Visibility (km)" /></div>', unsafe_allow_html=True)
    visibility = st.number_input('', format='%d')

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
