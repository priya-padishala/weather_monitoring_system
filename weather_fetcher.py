import requests

API_KEY = 'd0690c864c7ed549898eb9cc5207e193'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'http://api.openweathermap.org/data/2.5/forecast'

def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

def fetch_weather_forecast(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    response = requests.get(FORECAST_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching forecast data: {response.status_code}")
