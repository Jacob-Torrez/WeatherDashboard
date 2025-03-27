import requests, config

class WeatherAPI:
    def __init__ (self):
        self.apiKey = config.API_KEY
        self.OWMURL = config.OWM_URL
        
    def requestWeather(self, location, excludes): #"exclude": "alerts,minutely"
        payload = {"lat": location.latitude, "lon": location.longitude, "appid": self.apiKey, "exclude": excludes, "units": "imperial"}

        request = requests.get(self.OWMURL, params=payload)

        if (request.status_code == 200):
            return request.json
        else:
            print("request failed")
        