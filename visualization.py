import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

class Visualizer:
    def __init__(self):
        pass

    def plotData(self, data, yLabel : str, dateFormat : str):
        fig, ax = plt.subplots()

        timestamps, values = zip(*data)

        dates = [datetime.datetime.fromtimestamp(ts) for ts in timestamps]

        ax.plot(dates, values, marker='o', linestyle='-')

        ax.xaxis.set_major_formatter(mdates.DateFormatter(dateFormat))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.xticks(rotation=45)

        ax.set_xlabel("Date")
        ax.set_ylabel(yLabel)
        ax.set_title(f"{yLabel} Over Time")

        plt.tight_layout()
        plt.show()
