import scheduler
import api
import visualization

class Interface:
    def __init__ (self):
        self.job_scheduler = scheduler.Scheduler()
        self.api = api.APICaller()
        self.visualizer = visualization.Visualizer()

    def run(self):
        print("Welcome to The Weather Dashboard!")

        while True:
            print("Options: [1] On-Demand [2] Scheduler [3] Exit")
            choice = input()

            if choice == '1':
                print("Entering On-Demand")
                self.onDemandMenu()

            elif choice == '2':
                print("Entering Scheduler")
                self.schedulerMenu()

            elif choice == '3':
                break

            else:
                print("Invalid input. Please input again")
                continue

    def onDemandMenu(self):
        while True:
            print("Please enter location: (q to quit)")
            location = input()

            if location == 'q':
                break

            locationData = self.api.requestCoordinates(location)

            if not locationData:
                "Invalid location. Please try again"
                continue

            weatherData = self.api.requestWeather(locationData['lon'], locationData['lat'], 'alerts,current')

            while True:
                print("Options: [1] Minutely [2] Hourly [3] Daily [4] Exit")
                choice = input()

                if choice == '4':
                    break

                elif choice != '1' and choice != '2' and choice != '3':
                    print("Invalid input. Please input again")
                    continue

                if choice == '1':
                    data = [(d['dt'], d['precipitation']) for d in weatherData['minutely']]
                    self.visualizer.plotData(data, "Precipitation (mm/h)", '%H:%M')

                elif choice == '2':
                    fields = {
                        '1': ("Temperature (F)", 'temp'),
                        '2': ("Pressure (hPa)", 'pressure'),
                        '3': ("Humidity (%)", 'humidity'),
                        '4': ("UV Index", 'uvi'),
                        '5': ("Wind speed (mi/h)", 'wind_speed'),
                        '6': ("Proabibility of Precipitation (%)", 'pop')
                    }
                    print("Plot options:")
                    print("[1] Temperature")
                    print("[2] Pressure")
                    print("[3] Humidity")
                    print("[4] UV Index")
                    print("[5] Wind Speed")
                    print("[6] Probability of Precipitation")     
                    print("[7] Exit")         
                    choice = input()

                    if choice == '7':
                        continue

                    if choice not in ['1', '2', '3', '4', '5', '6']:
                        print("Invald choice. Try again")
                        continue

                    data = [(d['dt'], d[fields[choice][1]]) for d in weatherData['hourly']]
                    self.visualizer.plotData(data, fields[choice][0], '%m/%m/%y %H:%M')

                elif choice == '3':
                    fields = {
                        '1': ("Max Temperature (F)", ('temp', 'max')),
                        '2': ("Min Temperature (F)", ('temp', 'min')),
                        '3': ("Pressure (hPa)", 'pressure'),
                        '4': ("Humidity (%)", 'humidity'),
                        '5': ("Wind speed (mi/h)", 'wind_speed'),
                        '6': ("Proabibility of Precipitation (%)", 'pop'),
                        '7': ("Max UV Index", 'uvi')
                    }
                    print("Plot options:")
                    print("[1] Max Temp")
                    print("[2] Min Temp")
                    print("[3] Pressure")
                    print("[4] Humidity")
                    print("[5] Wind Speed")
                    print("[6] Probability of Precipitation")    
                    print("[7] Max UV Index") 
                    print("[8] Exit")
                    choice = input()

                    if choice == '8':
                        continue

                    if choice not in ['1', '2', '3', '4', '5', '6', '7']:
                        print("Invalid choice. Try again")
                        continue

                    data = [(d['dt'], d[fields[choice][1][0]][fields[choice][1][1]] 
                            if isinstance(fields[choice][1], tuple) else d[fields[choice][1]]) 
                            for d in weatherData['daily']]
                    self.visualizer.plotData(data, fields[choice][0], '%m/%d/%y')

    def schedulerMenu(self):
        while True:
            print("Options: [1] View Jobs [2] View Data [3] Add Job [4] Remove Job [5] Exit")
            choice = input()

            if choice == '1':
                self.viewJobMenu()

            elif choice == '2':
                self.viewDataMenu()
            
            elif choice == '3':
                self.addJobMenu()

            elif choice == '4':
                self.removeJobMenu()

            elif choice == '5':
                break

            else:
                print("Invalid input. Please input again")
                continue

    def viewJobMenu(self):
        jobs = self.job_scheduler.getJobsMetadata()

        columnNames = ["locationID", "City", "Country"]
        columnWidths = [len(col) for col in columnNames]

        for job in jobs:
            for i, value in enumerate(job):
                columnWidths[i] = max(columnWidths[i], len(str(value)))

        header = " | ".join([col.ljust(columnWidths[i]) for i, col in enumerate(columnNames)])
        print(header)
        print("-" * len(header))

        for job in jobs:
            print(" | ".join(str(value).ljust(columnWidths[i]) for i, value in enumerate(job)))

        print("-" * len(header))

    def viewDataMenu(self):
        while True:
            print("Enter locationID of data to view: (q to quit)")
            locationID = input()

            if (locationID.lower() == 'q'):
                break

            weatherData = self.job_scheduler.getJobData(locationID)

            if (not weatherData):
                print("Invalid ID or no data available. Please try again")
                continue

            fields = {
                '1': ("Max Temperature (F)", 2),
                '2': ("Min Temperature (F)", 3),
                '3': ("Probability of Precipitation (%)", 4),
                '4': ("Humidity (%)", 5),
                '5': ("Pressure (hPa)", 6),
                '6': ("UV Index Max", 7)
            }

            while True:
                print("Plot options:")
                print("[1] Max Temp")
                print("[2] Min Temp")
                print("[3] Probability of Precipitation")
                print("[4] Humidity")
                print("[5] Pressure")
                print("[6] UV Index Max")
                print("[7] Exit")                
                choice = input()

                if (choice in fields):
                    yLabel, dataIndex = fields[choice]
                    
                    data = [(d[1], d[dataIndex]) for d in weatherData]
                    self.visualizer.plotData(data, yLabel, '%m/%d/%y')

                elif (choice == '7'):
                    break

                else:
                    print("Invalid input. Please try again")
                    continue

    def addJobMenu(self):
        while True:
            print("Please enter the location of the job: (q to quit)")
            location = input()

            if (location.lower() == 'q'):
                break

            elif (self.job_scheduler.addJob(location)):
                print("Job added successfully!")
                break

            else:
                print("Job already added or unknown location. Please try again")
                continue

    def removeJobMenu(self):
        while True:
            print("Enter locationID of job to remove: (q to quit)")
            locationID = input()

            if (locationID.lower() == 'q'):
                break

            elif (self.job_scheduler.removeJob(locationID)):
                print("Job removed successfully!")
                break

            else:
                print("Job not found or could not be removed. Please try again")
                continue

