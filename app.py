import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("carbon_emission_model.pkl")

st.title("🌱 Household Carbon Emission Predictor")
st.write("Enter household details to predict monthly CO₂ emissions")

# User inputs
household_size = st.number_input("Household Size", 1, 10, 3)
monthly_energy_kwh = st.number_input("Monthly Energy Usage (kWh)", 50, 1000, 250)
renewable_usage_pct = st.slider("Renewable Energy Usage (%)", 0, 100, 40)
water_usage_liters = st.number_input("Water Usage (liters/month)", 1000, 30000, 12000)
waste_generated_kg = st.number_input("Waste Generated (kg/month)", 1, 60, 20)
recycling_pct = st.slider("Recycling Percentage (%)", 0, 100, 50)
green_appliances = st.number_input("Number of Green Appliances", 0, 10, 3)

# Predict button
if st.button("Predict Carbon Emission"):
    input_data = np.array([[
        household_size,
        monthly_energy_kwh,
        renewable_usage_pct,
        water_usage_liters,
        waste_generated_kg,
        recycling_pct,
        green_appliances
    ]])

    prediction = model.predict(input_data)[0]
    st.success(f"🌍 Estimated Carbon Emission: {prediction:.2f} kg CO₂/month")
