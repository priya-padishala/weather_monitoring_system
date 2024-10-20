import sqlite3

def check_alerts(city):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT temp, humidity, wind_speed FROM current_weather WHERE city = ?', (city,))
    data = cursor.fetchone()

    if data:
        temp, humidity, wind_speed = data
        if temp > 35:  # Temperature alert threshold
            send_alert(city, temp, 'Temperature exceeds threshold.')
        
        if humidity > 80:  # Humidity alert threshold
            send_alert(city, humidity, 'Humidity exceeds threshold.')
        
        if wind_speed > 20:  # Wind speed alert threshold
            send_alert(city, wind_speed, 'Wind speed exceeds threshold.')

    conn.close()

def send_alert(city, value, message):
    print(f"ALERT: {message} in {city}: {value}")
