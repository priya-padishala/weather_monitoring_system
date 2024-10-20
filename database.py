import sqlite3

def init_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    # Create daily weather summary table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_weather_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            city TEXT NOT NULL,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            humidity REAL,
            wind_speed REAL,
            dominant_condition TEXT
        )
    ''')

    # Create forecast weather summary table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS forecast_weather_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            city TEXT NOT NULL,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            humidity REAL,
            wind_speed REAL,
            dominant_condition TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
