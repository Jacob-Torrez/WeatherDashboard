import scheduler
import visualization

class Interface:
    def __init__ (self):
        self.job_scheduler = scheduler.Scheduler()

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
                print("Exiting")
                break

            else:
                print("Invalid input. Please input again")
                continue

    def onDemandMenu(self):
        while True:
            print("Options: [1] Minutely [2] Hourly [3] Daily [4] Exit")
            choice = input()

            if choice == '4':
                print("Exiting")
                break

            elif choice != '1' and choice != '2' and choice != '3':
                print("Invalid input. Please input again")
                continue

            print("Please enter the location:")
            city = input()

            if choice == '1':
                print("Retrieving minutely forecast")

            elif choice == '2':
                print("Retrieving hourly forecast")

            elif choice == '3':
                print("Retrieving daily forecast")

    def schedulerMenu(self):
        while True:
            print("Options: [1] View Jobs [2] View Data [3] Add Job [4] Remove Job [5] Exit")
            choice = input()

            if choice == '1':
                self.viewJobMenu()

            elif choice == '2':
                pass
            
            elif choice == '3':
                self.addJobMenu()

            elif choice == '4':
                self.removeJobMenu()

            elif choice == '5':
                print("Exiting")
                break

            else:
                print("Invalid input. Please input again")
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
        

