import sqlite3

def calculate_daily_summary(city, weather_data):
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    dt = weather_data['dt']
    
    avg_temp = temp  # Replace with actual calculation logic
    max_temp = temp  # Replace with actual logic
    min_temp = temp  # Replace with actual logic
    dominant_condition = weather_data['weather'][0]['main']
    
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO daily_weather_summary (date, city, avg_temp, max_temp, min_temp, humidity, wind_speed, dominant_condition)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (dt, city, avg_temp, max_temp, min_temp, humidity, wind_speed, dominant_condition))
    
    conn.commit()
    conn.close()

def process_forecast_data(city, forecast_data):
    daily_summaries = {}
    
    for entry in forecast_data['list']:
        dt = entry['dt']
        temp = entry['main']['temp']
        humidity = entry['main']['humidity']
        wind_speed = entry['wind']['speed']
        condition = entry['weather'][0]['main']

        date = dt.split(' ')[0]
        
        if date not in daily_summaries:
            daily_summaries[date] = {
                'temps': [],
                'humidity': [],
                'wind_speed': [],
                'conditions': []
            }

        daily_summaries[date]['temps'].append(temp)
        daily_summaries[date]['humidity'].append(humidity)
        daily_summaries[date]['wind_speed'].append(wind_speed)
        daily_summaries[date]['conditions'].append(condition)
    
    for date, data in daily_summaries.items():
        avg_temp = sum(data['temps']) / len(data['temps'])
        max_temp = max(data['temps'])
        min_temp = min(data['temps'])
        dominant_condition = max(set(data['conditions']), key=data['conditions'].count)

        store_forecast_summary(date, city, avg_temp, max_temp, min_temp, data['humidity'], data['wind_speed'], dominant_condition)

def store_forecast_summary(date, city, avg_temp, max_temp, min_temp, humidity, wind_speed, dominant_condition):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO forecast_weather_summary (date, city, avg_temp, max_temp, min_temp, humidity, wind_speed, dominant_condition)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (date, city, avg_temp, max_temp, min_temp, sum(humidity)/len(humidity), sum(wind_speed)/len(wind_speed), dominant_condition))

    conn.commit()
    conn.close()
