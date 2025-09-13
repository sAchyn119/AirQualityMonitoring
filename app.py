import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('models/best_model.pkl')

# App Title
st.set_page_config(page_title="🌍 AQI Prediction App", layout="wide")

st.title("🌿 Air Quality Index (AQI) Prediction")
st.markdown("""
Welcome to the **Air Quality Monitoring System** powered by Machine Learning!  
Enter the values of different pollutants to predict the **Air Quality Index (AQI)** in real time.
""")

# Create input fields in columns
with st.form(key='aqi_form'):
    col1, col2, col3 = st.columns(3)

    with col1:
        pm25 = st.number_input('PM2.5 (µg/m³)', min_value=0.0, max_value=500.0, step=0.1)
        no2 = st.number_input('NO2 (µg/m³)', min_value=0.0, max_value=500.0, step=0.1)
    
    with col2:
        pm10 = st.number_input('PM10 (µg/m³)', min_value=0.0, max_value=500.0, step=0.1)
        so2 = st.number_input('SO2 (µg/m³)', min_value=0.0, max_value=500.0, step=0.1)
    
    with col3:
        co = st.number_input('CO (mg/m³)', min_value=0.0, max_value=50.0, step=0.1)
        o3 = st.number_input('O3 (µg/m³)', min_value=0.0, max_value=500.0, step=0.1)

    submit_button = st.form_submit_button(label='Predict AQI 🌟')

# Prediction Logic
if submit_button:
    input_data = pd.DataFrame([[pm25, pm10, no2, so2, co, o3]],
                              columns=['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3'])
    
    predicted_aqi = model.predict(input_data)[0]

    # Display Result
    st.success(f"✅ Predicted Air Quality Index (AQI): **{predicted_aqi:.2f}**")

    # Informative Interpretation
    if predicted_aqi <= 50:
        st.info("🌱 AQI Level: Good – Air quality is satisfactory.")
    elif predicted_aqi <= 100:
        st.info("🌼 AQI Level: Moderate – Acceptable air quality.")
    elif predicted_aqi <= 150:
        st.warning("⚠️ AQI Level: Unhealthy for sensitive groups.")
    elif predicted_aqi <= 200:
        st.warning("⚠️ AQI Level: Unhealthy – General public may be affected.")
    elif predicted_aqi <= 300:
        st.error("🚨 AQI Level: Very Unhealthy – Health warnings of emergency conditions.")
    else:
        st.error("🚨 AQI Level: Hazardous – Entire population likely affected.")

# Footer
st.markdown("""
---
Made with ❤️ by **Sachin Yadav**  
📅 AICTE Edunet Internship – 2025
""")
