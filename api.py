import requests
from dotenv import load_dotenv
import os

class APICaller:
    def __init__(self):
        load_dotenv()

        self.OWM_KEY = os.getenv("OWM_KEY")
        self.OWM_URL = os.getenv("OWM_URL")
        self.OSM_URL = os.getenv("OSM_URL")
        self.USER_AGENT = os.getenv("USER_AGENT")
        self.timeout = 20
        
    def requestWeather(self, lon : float, lat : float, excludes : str):
        try:
            payload = {
                'lat': lat, 
                'lon': lon, 
                'appid': self.OWM_KEY, 
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
                'User-Agent': self.USER_AGENT
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