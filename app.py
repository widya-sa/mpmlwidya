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

# Fungsi untuk mengonversi input string ke nilai numerik
def map_input_to_value(value, mapping):
    return mapping.get(value, -1)

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
        margin: 0; /* Menghilangkan margin untuk tampilan penuh */
    }
    .stButton>button {
        background-color: #f9dcc4;  /* Warna beige untuk tombol */
        color: black;
        border: none;
        padding: 15px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 10px 0;
        cursor: pointer;
        border-radius: 12px;
        width: 100%; /* Lebar penuh tombol */
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
    .stNumberInput input, .stSelectbox select, .stTextInput input, .stTextArea textarea {
        background: #f9dcc4;
        color: black;
        border: none;
        width: 100%; /* Lebar penuh input di dalam container */
    }
    .st-container {
        width: 100%; /* Lebar penuh untuk konten */
        max-width: 100%; /* Menghindari pembatasan lebar */
    }
    .stColumns {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }
    .stColumn {
        flex: 1;
        min-width: 0;
        max-width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Mengatur elemen utama di dalam div dengan kelas 'main'
st.markdown('<div class="main">', unsafe_allow_html=True)

# Antarmuka pengguna Streamlit
st.title("Weather Prediction")
st.write("Masukkan data cuaca untuk memprediksi jenis cuaca.")

# Definisi mapping untuk input
cloud_cover_mapping = {'Clear': 0, 'Cloudy': 1, 'Overcast': 2, 'Partly Cloudy': 3}
season_mapping = {'Autumn': 0, 'Spring': 1, 'Summer': 2, 'Winter': 3}
location_mapping = {'Coastal': 0, 'Inland': 1, 'Mountain': 2}

# Membagi input form menjadi dua kolom per baris
def create_input_row(inputs):
    cols = st.columns(len(inputs))
    for i, input_item in enumerate(inputs):
        with cols[i]:
            st.markdown(f'<div class="input-container"><i class="fas {input_item[1]}"></i><span class="input-label">{input_item[0]}</span>', unsafe_allow_html=True)
            if input_item[0] == 'Cloud Cover':
                value = st.selectbox('', options=list(input_item[2].keys()), key=input_item[3])
                st.session_state[input_item[3]] = map_input_to_value(value, input_item[2])
            elif input_item[0] == 'Season':
                value = st.selectbox('', options=list(input_item[2].keys()), key=input_item[3])
                st.session_state[input_item[3]] = map_input_to_value(value, input_item[2])
            elif input_item[0] == 'Location':
                value = st.selectbox('', options=list(input_item[2].keys()), key=input_item[3])
                st.session_state[input_item[3]] = map_input_to_value(value, input_item[2])
            else:
                st.session_state[input_item[3]] = st.number_input('', key=input_item[3])
            st.markdown('</div>', unsafe_allow_html=True)

# Definisi input untuk baris pertama dan kedua
inputs_row1 = [
    ('Temperature (°C)', 'fa-thermometer-half', None, 'temp'),
    ('Humidity (%)', 'fa-tint', None, 'humidity')
]
inputs_row2 = [
    ('Wind Speed (km/h)', 'fa-wind', None, 'wind_speed'),
    ('Precipitation (%)', 'fa-cloud-showers-heavy', None, 'precipitation')
]
inputs_row3 = [
    ('Atmospheric Pressure (hPa)', 'fa-gauge', None, 'pressure'),
    ('Cloud Cover', 'fa-cloud', cloud_cover_mapping, 'cloud_cover')
]
inputs_row4 = [
    ('Season', 'fa-calendar-season', season_mapping, 'season'),
    ('Location', 'fa-map-marker-alt', location_mapping, 'location')
]
inputs_row5 = [
    ('UV Index', 'fa-sun', None, 'uv_index'),
    ('Visibility (km)', 'fa-eye', None, 'visibility')
]

# Menampilkan input dalam baris
create_input_row(inputs_row1)
create_input_row(inputs_row2)
create_input_row(inputs_row3)
create_input_row(inputs_row4)
create_input_row(inputs_row5)

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
