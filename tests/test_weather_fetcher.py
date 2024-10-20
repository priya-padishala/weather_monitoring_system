import unittest
from weather_fetcher import fetch_weather_data

class TestWeatherFetcher(unittest.TestCase):
    def test_fetch_weather_data(self):
        city = 'Delhi'
        data = fetch_weather_data(city)
        self.assertIn('main', data)
        self.assertIn('temp', data['main'])

if __name__ == '__main__':
    unittest.main()
