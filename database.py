import sqlite3
import config

class DatabaseManager:
    def __init__(self):
        self.con = sqlite3.connect(config.DATABASE_FILE)
        self.cur = self.con.cursor()

    def addLocation(self, country : str, city : str, long : float, lat : float):
        if (self.cur.execute("SELECT COUNT(LocationID) FROM Location WHERE City = ? AND Country = ?", (city, country)).fetchone()[0]):
            return False
        
        else:
            self.cur.execute("INSERT INTO Location (Country, City, Longitude, Latitude) VALUES (?, ?, ?, ?)", (country, city, long, lat))
            self.con.commit()
            return True
    
    def removeLocation(self, locationID : int):
        if (self.cur.execute("SELECT COUNT(LocationID) FROM Location WHERE LocationID = ?", (locationID,)).fetchone()[0]):
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

    def addWeather(self, locationID : int, timestamp : int, tempMax : float, tempMin : float, PoP : float, humidity : float, pressure : float, UV : float, moonPhase : float):
        self.cur.execute("INSERT INTO Weather (LocationID, Timestamp, TemperatureMax, TemperatureMin, PrecipProbability, Humidity, Pressure, UVIndexMax, MoonPhase) "
        + "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (locationID, timestamp, tempMax, tempMin, PoP, humidity, pressure, UV, moonPhase))
        self.con.commit()
        return self.cur.lastrowid