import sqlite3
import config

class DatabaseManager:
    def __init__(self):
        self.con = sqlite3.connect(config.DATABASE_FILE)
        self.cur = self.con.cursor()

    def addLocation(self, country : str, city : str, long : float, lat : float):
        if (self.cur.execute("SELECT LocationID FROM Location WHERE City = ? AND Country = ?", (city, country)).fetchone() is None):
            self.cur.execute("INSERT INTO Location (Country, City, Longitude, Latitude) VALUES (?, ?, ?, ?)", (country, city, long, lat))
            self.con.commit()
            return True
        
        else:
            return False
    
    def removeLocation(self, locationID : int):
        if (self.cur.execute("SELECT LocationID FROM Location WHERE LocationID = ?", (locationID,)).fetchone()):
            self.cur.execute("DELETE FROM Location WHERE LocationID = ?", (locationID,))
            self.cur.execute("DELETE FROM Weather WHERE LocationID = ?", (locationID,))
            self.con.commit()
            return True
        
        else:
            return False
        
    def getLocationsMetadata(self):
        return self.cur.execute("SELECT LocationID, City, Country FROM Location").fetchall()
    
    def getLocationsCoordinates(self):
        return self.cur.execute("SELECT LocationID, Longitude, Latitude FROM Location").fetchall()
    
    def getWeatherData(self, locationID : int):
        if (self.cur.execute("SELECT LocationID FROM Weather WHERE LocationID = ?", (locationID,)).fetchone()):
            return (self.cur.execute("SELECT * FROM Weather WHERE LocationID = ?", (locationID,)).fetchall())
        
        else:
            return False

    def addWeather(self, locationID : int, timestamp : int, tempMax : float, tempMin : float, PoP : float, humidity : float, pressure : float, UV : float):
        self.cur.execute("INSERT INTO Weather (LocationID, Timestamp, TemperatureMax, TemperatureMin, PrecipProbability, Humidity, Pressure, UVIndexMax) "
        + "VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (locationID, timestamp, tempMax, tempMin, PoP, humidity, pressure, UV))
        self.con.commit()
        return self.cur.lastrowid