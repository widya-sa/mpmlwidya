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
        position: relative;
        padding: 20px; /* Menambahkan padding untuk ruang di sekeliling konten */
    }
    .sidebar .sidebar-content {
        background-color: rgba(255, 255, 255, 0.8);
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
        position: relative;
    }
    .stSelectbox>div, .stNumberInput>div, .stTextInput>div, .stTextArea>div {
        background: #f9dcc4;
        color: black;
    }
    .input-container {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
        background: #f9dcc4;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #f4b9a7;
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
    .stNumberInput input, .stSelectbox select, .stTextInput input, .stTextArea textarea {
        background: #f9dcc4;
        color: black;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Mengatur elemen utama di dalam div dengan kelas 'main'
st.markdown('<div class="main">', unsafe_allow_html=True)

# Antarmuka pengguna Streamlit
st.title("Weather Prediction")
st.write("Masukkan data cuaca untuk memprediksi jenis cuaca.")

# Membagi input form menjadi baris dengan 3 input di setiap baris
def create_input_row(inputs):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="input-container"><i class="fas {inputs[0][1]}"></i><span class="input-label">{inputs[0][0]}</span>', unsafe_allow_html=True)
        st.number_input('', key=inputs[0][2])
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="input-container"><i class="fas {inputs[1][1]}"></i><span class="input-label">{inputs[1][0]}</span>', unsafe_allow_html=True)
        st.number_input('', key=inputs[1][2])
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="input-container"><i class="fas {inputs[2][1]}"></i><span class="input-label">{inputs[2][0]}</span>', unsafe_allow_html=True)
        st.number_input('', key=inputs[2][2])
        st.markdown('</div>', unsafe_allow_html=True)

# Definisi input
inputs_row1 = [
    ('Temperature (°C)', 'fa-thermometer-half', 'temp'),
    ('Humidity (%)', 'fa-tint', 'humidity'),
    ('Wind Speed (km/h)', 'fa-wind', 'wind_speed')
]
inputs_row2 = [
    ('Precipitation (%)', 'fa-cloud-showers-heavy', 'precipitation'),
    ('Atmospheric Pressure (hPa)', 'fa-gauge', 'pressure'),
    ('UV Index', 'fa-sun', 'uv_index')
]
inputs_row3 = [
    ('Cloud Cover', 'fa-cloud', 'cloud_cover'),
    ('Season', 'fa-calendar-season', 'season'),
    ('Location', 'fa-map-marker-alt', 'location')
]
inputs_row4 = [
    ('Visibility (km)', 'fa-eye', 'visibility')
]

# Menampilkan input dalam baris
create_input_row(inputs_row1)
create_input_row(inputs_row2)
create_input_row(inputs_row3)
create_input_row(inputs_row4)

# Tombol prediksi
if st.button('Predict'):
    to_predict_list = [
        st.session_state.temp, st.session_state.humidity, st.session_state.wind_speed,
        st.session_state.precipitation, st.session_state.pressure, st.session_state.uv_index,
        st.session_state.cloud_cover, st.session_state.season, st.session_state.visibility,
        st.session_state.location
    ]
    
    try:
        result = value_predictor(to_predict_list)
        st.success(f"Predicted Weather Type: {result}")
    except RuntimeError as e:
        st.error(f"An error occurred: {str(e)}")

# Menutup div dengan kelas 'main'
st.markdown('</div>', unsafe_allow_html=True)
