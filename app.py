import pickle
import pandas as pd
import streamlit as st

with open("model/model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title = "Electricity Price Prediction", page_icon = "⚡", layout = "centered"
)

st.title("⚡ Electricity Price Prediction")
st.write("Enter the required weather and electricity-system information to predict the electricity price.")

day = st.number_input("Day", min_value = 1, max_value = 31, value = 1, step = 1)

month = st.number_input("Month", min_value = 1, max_value = 12, value = 1, step = 1) 

forecast_wind_production = st.number_input("Forecast Wind Production", min_value = 0.0, value = 0.0)

system_load_ea = st.number_input("System Load EA",min_value = 0.0, value = 0.0)

ork_temperature = st.number_input("ORK Temperature", value = 10.0)

ork_windspeed = st.number_input("ORK Windspeed", min_value = 0.0, value = 0.0)

co2_intensity = st.number_input("CO2 Intensity",min_value = 0.0, value = 0.0)

actual_wind_production = st.number_input("Actual Wind Production", min_value = 0.0, value = 0.0)

system_load_ep2 = st.number_input("System Load EP2", min_value = 0.0, value = 0.0)

smpep2 = st.number_input("SMPEP2", value = 0.0)

input_data = pd.DataFrame({
    "Day": [day],
    "Month": [month],
    "ForecastWindProduction": [forecast_wind_production],
    "SystemLoadEA": [system_load_ea],
    "ORKTemperature": [ork_temperature],
    "ORKWindspeed": [ork_windspeed],
    "CO2Intensity": [co2_intensity],
    "ActualWindProduction": [actual_wind_production],
    "SystemLoadEP2": [system_load_ep2],
    "SMPEP2": [smpep2]
})

if st.button("Predict Electricity Price"):
    try:
        prediction = model.predict(input_data)

        st.success("Prediction completed successfully!")

        st.metric(
            label="Predicted Electricity Price",
            value=f"{prediction[0]:.2f}"
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")