import requests
import config

class WeatherAPI:
    def __init__(self):
        self.api_key = config.API_KEY
        self.base_url = config.OWM_URL
        self.timeout = 20
        
    def requestWeather(self, lon : float, lat : float, excludes : str):
        try:
            payload = {
                'lat': lat, 
                'lon': lon, 
                'appid': self.api_key, 
                'exclude': excludes, 
                'units': 'imperial'
            }

            response = requests.get(
                self.base_url,
                params=payload,
                timeout=self.timeout
            )
            response.raise_for_status()

            return response.json()
        
        except:
            return False