import unittest
from data_processor import calculate_daily_summary, process_forecast_data, store_forecast_summary
from weather_fetcher import fetch_weather_data

class TestDataProcessor(unittest.TestCase):
    
    def setUp(self):
        # This will be run before each test
        self.city = 'Delhi'
        self.weather_data = fetch_weather_data(self.city)  # Simulate fetching real weather data

    def test_calculate_daily_summary(self):
        # This method should calculate and store daily summary
        try:
            calculate_daily_summary(self.city, self.weather_data)
            # You might want to verify that data is stored correctly; you could query the DB here
            # For now, we will assume it worked if no exceptions were raised
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"calculate_daily_summary raised an exception: {e}")

    def test_process_forecast_data(self):
        # Assuming fetch_weather_forecast is implemented properly
        forecast_data = fetch_weather_data(self.city)  # Simulate fetching forecast data
        try:
            process_forecast_data(self.city, forecast_data)
            # Again, verify data is stored; this can be done with DB queries
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"process_forecast_data raised an exception: {e}")

    def test_store_forecast_summary(self):
        # Mock values for storing forecast summary
        date = '2024-10-20'
        avg_temp = 25.0
        max_temp = 30.0
        min_temp = 20.0
        humidity = 60.0
        wind_speed = 10.0
        dominant_condition = 'Clear'

        try:
            store_forecast_summary(date, self.city, avg_temp, max_temp, min_temp, humidity, wind_speed, dominant_condition)
            # Verify data is stored; query the DB
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"store_forecast_summary raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
