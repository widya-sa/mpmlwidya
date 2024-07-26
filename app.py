import streamlit as st
import joblib
import numpy as np

# Fungsi untuk memuat model dan melakukan prediksi
def value_predictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, -1)  # Membentuk array 2D dengan 1 baris dan 10 kolom
    with open('model.pkl', 'rb') as file:
        loaded_model = joblib.load(file)
    result = loaded_model.predict(to_predict)[0]  # Ambil hasil prediksi
    weather_mapping = {
        0: 'Cloudy',
        1: 'Rainy',
        2: 'Snowy',
        3: 'Sunny'
    }
    return weather_mapping.get(result, 'Unknown')  # Mengembalikan kategori cuaca

# Antarmuka pengguna Streamlit
st.title("Weather Prediction")
st.write("Masukkan data cuaca untuk memprediksi jenis cuaca.")

# Membagi form menjadi dua kolom
col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Cuaca")
    temperature = st.number_input('Temperature (°C)')
    humidity = st.number_input('Humidity (%)')
    wind_speed = st.number_input('Wind Speed (km/h)')
    precipitation = st.number_input('Precipitation (%)')
    atmospheric_pressure = st.number_input('Atmospheric Pressure (hPa)')

with col2:
    st.subheader("Kondisi Cuaca")
    cloud_cover = st.selectbox('Cloud Cover', options={
        'Clear': 0,
        'Cloudy': 1,
        'Overcast': 2,
        'Partly Cloudy': 3
    })
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
st.markdown("---")
if st.button('Predict'):
    to_predict_list = [
        temperature, humidity, wind_speed, precipitation,
        cloud_cover, atmospheric_pressure, uv_index, season,
        visibility, location
    ]
    
    try:
        result = value_predictor(to_predict_list)
        st.success(f"Predicted Weather Type: {result}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
