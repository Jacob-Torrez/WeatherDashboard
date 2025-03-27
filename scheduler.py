import api, schedule, database, requests, config

class Scheduler:
    def __init__ (self):
        self.wapi = api.WeatherAPI()
        self.dbManager = database.DatabaseManager()
        self.OSMURL = config.OSM_URL

    def addJob(self, location: str):
        payload = {"q": location, "format": "json", "limit": 1, "addressdetails": 1}
        headers = {"User-Agent": config.USER_AGENT}

        request = requests.get(self.OSMURL, params=payload, headers=headers)

        if (request.status_code != 200):
            return False
        else:
            response = request.json()
            return self.dbManager.addLocation(response[0]['address']['country'], response[0]['address']['city'], response[0]['lon'], response[0]['lat'])
        
    def removeJob(self, locationID : int): # check if location exists
        return self.dbManager.removeLocation(locationID)
    
    def getJobs(self):
        pass

    def fetchDailyWeather(self):
        pass

scheduler = Scheduler()
print(scheduler.removeJob(1))
