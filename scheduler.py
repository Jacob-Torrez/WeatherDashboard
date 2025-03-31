import api
import schedule
import database
import time

class Scheduler:
    def __init__(self):
        self.api = api.APICaller()
        self.db_manager = database.DatabaseManager()

    def addJob(self, location: str):
        locationData = self.api.requestCoordinates(location)

        if (locationData):
            return self.db_manager.addLocation(
                locationData['address']['country'],
                locationData['address']['city'],
                locationData['lon'],
                locationData['lat']
            )
        
        else:
            return False
        
    def removeJob(self, locationID : int):
        return self.db_manager.removeLocation(locationID)
    
    def getJobsMetadata(self):
        return self.db_manager.getLocationsMetadata()
    
    def getJobsCoordinates(self):
        return self.db_manager.getLocationsCoordinates()

    def fetchDailyWeather(self):
        locations = self.getJobsCoordinates()

        if not locations:
            return False

        else:
            for location in locations:
                response = self.api.requestWeather(location[1], location[2], 'alerts,minutely,hourly,current')['daily'][0]
                self.db_manager.addWeather(location[0], response['dt'], response['temp']['max'], response['temp']['min'], response['pop'], response['humidity'], response['pressure'], response['uvi'])

            return True
        
    def getJobData(self, locationID : int):
        return self.db_manager.getWeatherData(locationID)
        

def main():
    scheduler = Scheduler()
    schedule.every(24).hours.do(scheduler.fetchDailyWeather)

    while True:
        schedule.run_pending()
        time.sleep(3600)

if __name__ == "__main__":
    main()