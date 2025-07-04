import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("trained_model.pkl")

# App Title
st.set_page_config(page_title="Blast-Furnace Failure Predictor", page_icon="🔥", layout="centered")
st.title("Predictive Maintenance for Blast-Furnace Stoves")
st.markdown("AI model to **predict failure risk within the next 24 hours** based on sensor readings.")

# Sidebar Information
with st.sidebar:
    st.header("📌 Sensor Input Guide")
    st.markdown("""
    - **Temperature (°C):** 800–1200  
    - **Pressure (bar):** 4.0–10.0  
    - **Vibration (mm/s):** 0.0–10.0  
    - **Flow Rate (m³/h):** 500–1500  
    - **Runtime (hrs):** 0–2000  
    - **Sensor Drift:** 0.0–1.0  
    """)

st.subheader("📥 Enter Sensor Values")

# Input layout
col1, col2 = st.columns(2)
with col1:
    temperature = st.number_input("🔥 Temperature (°C)", min_value=800.0, max_value=1200.0, step=0.1)
    vibration = st.number_input("📉 Vibration (mm/s)", min_value=0.0, max_value=10.0, step=0.1)
    runtime = st.number_input("⏱ Runtime Since Maintenance (hrs)", min_value=0, max_value=2000)

with col2:
    pressure = st.number_input("💨 Pressure (bar)", min_value=4.0, max_value=10.0, step=0.1)
    flow_rate = st.number_input("🌬 Flow Rate (m³/h)", min_value=500.0, max_value=1500.0, step=1.0)
    drift = st.slider("🎯 Sensor Drift Index", 0.0, 1.0, 0.2)

# Predict button
if st.button("🔍 Predict Failure Risk"):
    input_data = np.array([[temperature, pressure, vibration, flow_rate, runtime, drift]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.markdown("---")
    if prediction == 1:
        st.error("⚠️ **Warning**: High Risk of Failure in Next 24 Hours!")
    else:
        st.success("✅ System is Operating Normally. No Failure Predicted.")
    

