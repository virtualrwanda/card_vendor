from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the saved ARIMA model
model = joblib.load('arima_model.pkl')

# Route to test the API
@app.route('/')
def home():
    return "Welcome to the ARIMA Model API!"

# Route to predict transport cost based on inputs
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        distance = float(request.form['distance'])
        fuel_price = float(request.form['fuel_price'])
        trips_per_day = int(request.form['trips_per_day'])
        peak_off_peak = int(request.form['peak_off_peak'])

        # Prepare input data
        inputs = {
            'Distance': [distance],
            'Fuel_Price': [fuel_price],
            'Trips_Per_Day': [trips_per_day],
            'Peak/Off-Peak': [peak_off_peak]
        }
        inputs_df = pd.DataFrame(inputs)

        # Forecast the next month's cost
        forecast_steps = 1
        forecast = model.forecast(steps=forecast_steps)

        # Render the result on the same page
        return render_template('index.html', forecasted_cost=round(forecast[0], 2))

    except Exception as e:
        return render_template('index.html', error=str(e))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
