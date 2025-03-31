import requests
from dotenv import load_dotenv
import os

class APIClient:
    def __init__(self):
        load_dotenv()

        self.owm_key = os.getenv("OWM_KEY")
        self.owm_url = os.getenv("OWM_URL")
        self.osm_url = os.getenv("OSM_URL")
        self.user_agent = os.getenv("USER_AGENT")
        self.timeout = 20
        
    def requestWeather(self, lon : float, lat : float, excludes : str):
        try:
            payload = {
                'lat': lat, 
                'lon': lon, 
                'appid': self.owm_key, 
                'exclude': excludes, 
                'units': 'imperial'
            }

            response = requests.get(
                self.owm_url,
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
                'User-Agent': self.user_agent
            }

            response = requests.get(
                self.osm_url, 
                params=payload, 
                headers=headers
            )
            response.raise_for_status()

            return response.json()[0]

        except:
            return False