from flask import Flask, render_template
from weather_fetcher import fetch_weather_data, fetch_weather_forecast
from data_processor import calculate_daily_summary, process_forecast_data
from database import init_db

app = Flask(__name__)
init_db()  # Initialize the database

@app.route('/')
def index():
    # Fetch current weather data for a city
    city = 'Delhi'  # Change to desired city
    weather_data = fetch_weather_data(city)
    calculate_daily_summary(city, weather_data)

    # Fetch and process forecast data
    forecast_data = fetch_weather_forecast(city)
    process_forecast_data(city, forecast_data)

    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
