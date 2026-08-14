import pickle
import pandas as pd
from flask import render_template, request, Flask

app = Flask(__name__)

with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route("/", methods = ["GET", "POST"])
def home():
    prediction = None
    error = None

    values = {
        'day' : 1,
        'month' : 1,
        'forecast_wind_production' : 0.0,
        'system_load_ea' : 0.0,
        'ork_temperature' : 10.0,
        'ork_windspeed' : 0.0,
        'co2_intensity' : 0.0,
        'actual_wind_production' : 0.0,
        'system_load_ep2' : 0.0,
        'smpep2' : 0.0
    }

    if request.method == "POST":
        try:
            values['day'] = int(request.form['day'])
            values['month'] = int(request.form['month'])
            values['forecast_wind_production'] = float(request.form['forecast_wind_production'])
            values['system_load_ea'] = float(request.form['system_load_ea'])
            values['ork_temperature'] = float(request.form['ork_temperature'])
            values['ork_windspeed'] = float(request.form['ork_windspeed'])
            values['co2_intensity'] = float(request.form['co2_intensity'])
            values['actual_wind_production'] = float(request.form['actual_wind_production'])
            values['system_load_ep2'] = float(request.form['system_load_ep2'])
            values['smpep2'] = float(request.form['smpep2'])

            input_data = pd.DataFrame({
                "Day": [values["day"]],
                "Month": [values["month"]],
                "ForecastWindProduction": [values["forecast_wind_production"]],
                "SystemLoadEA": [values["system_load_ea"]],
                "ORKTemperature": [values["ork_temperature"]],
                "ORKWindspeed": [values["ork_windspeed"]],
                "CO2Intensity": [values["co2_intensity"]],
                "ActualWindProduction": [values["actual_wind_production"]],
                "SystemLoadEP2": [values["system_load_ep2"]],
                "SMPEP2": [values["smpep2"]]
            })

            result = model.predict(input_data)
            prediction = f"{result[0]:.2f}"

        except Exception as e:
            error = f"Prediction failed: {str(e)}"

    return render_template(
        "index.html",
        prediction = prediction,
        error = error,
        values = values
    )

if __name__ == '__main__':
    app.run(debug = True)