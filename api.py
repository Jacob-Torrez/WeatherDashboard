import requests
import config

class APICaller:
    def __init__(self):
        self.OWM_key = config.OWM_KEY
        self.OWM_URL = config.OWM_URL
        self.OSM_URL = config.OSM_URL
        self.timeout = 20
        
    def requestWeather(self, lon : float, lat : float, excludes : str):
        try:
            payload = {
                'lat': lat, 
                'lon': lon, 
                'appid': self.OWM_key, 
                'exclude': excludes, 
                'units': 'imperial'
            }

            response = requests.get(
                self.OWM_URL,
                params=payload,
                timeout=self.timeout
            )
            response.raise_for_status()

            return response.json()
        
        except:
            return False
        
    def requestCoordinates(self, location : str):
        try:
            payload = {
                'q': location, 
                'format': 'json', 
                'limit': 1, 
                'addressdetails': 1
            }

            headers = {
                'User-Agent': config.USER_AGENT
            }

            response = requests.get(
                self.OSM_URL, 
                params=payload, 
                headers=headers
            )
            response.raise_for_status()

            return response.json()[0]

        except:
            return False