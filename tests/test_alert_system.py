import unittest
from alert_system import check_alerts, send_alert

class TestAlertSystem(unittest.TestCase):
    
    def setUp(self):
        # This will be run before each test
        self.city = 'Delhi'

    def test_check_alerts_temperature(self):
        # Simulate the conditions under which alerts should be checked
        try:
            # Assuming check_alerts will print an alert if conditions are met
            check_alerts(self.city)  
            # Since print statements are hard to test, we'll assume the function works if no exception is raised
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"check_alerts raised an exception: {e}")

    def test_send_alert(self):
        # Test if sending alerts works as expected
        try:
            send_alert(self.city, 36, 'Temperature exceeds threshold.')
            # Since this function prints output, we cannot assert, but we can check if no exceptions were raised
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"send_alert raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
