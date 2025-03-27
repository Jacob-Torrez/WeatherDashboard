import scheduler, visualization

class Interface:
    def __init__ (self):
        pass

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
            print("Options: [1] View Jobs [2] Add Job [3] Remove Job [4] Exit")
            choice = input()

            if choice == '1':
                pass
            
            elif choice == '2':
                pass

            elif choice == '3':
                pass

            elif choice == '4':
                print("Exiting")
                break

            else:
                print("Invalid input. Please input again")
                continue
