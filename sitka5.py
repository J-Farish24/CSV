import csv
from os import name
import matplotlib.pyplot as plt
from datetime import datetime

#Extract information for the first graph
open_file = open("sitka_weather_2018_simple.csv", "r")
csv_file_1 = csv.reader(open_file, delimiter=",")

header_row = next(csv_file_1)
#Get indexes for values
for index, column_header in enumerate(header_row):
    if column_header == "TMAX":
        high_index_1 = index
    elif column_header == "TMIN":
        low_index_1 = index
    elif column_header == "DATE":
        date_index_1 = index
    elif column_header == "NAME":
        name_index_1 = index

highs_1 = []
lows_1 = []
dates_1 = []



for rec in csv_file_1:
    try:
        date = datetime.strptime(rec[date_index_1], "%Y-%m-%d")
        high = int(rec[high_index_1])
        low = int(rec[low_index_1])
        graph_title_1 = rec[name_index_1]
    except ValueError:
        print(f"Missing data for {date}")
    else:
        highs_1.append(high)
        lows_1.append(low)
        dates_1.append(date)
open_file.close()

#Extract information for the second graph
open_file = open("death_valley_2018_simple.csv", "r")
csv_file_2 = csv.reader(open_file, delimiter=",")

header_row = next(csv_file_2)
#Get indexes for values
for index, column_header in enumerate(header_row):
    if column_header == "TMAX":
        high_index_2 = index
    elif column_header == "TMIN":
        low_index_2 = index
    elif column_header == "DATE":
        date_index_2 = index
    elif column_header == "NAME":
        name_index_2 = index

highs_2 = []
lows_2 = []
dates_2 = []



for rec in csv_file_2:
    try:
        date = datetime.strptime(rec[date_index_2], "%Y-%m-%d")
        high = int(rec[high_index_2])
        low = int(rec[low_index_2])
        graph_title_2 = rec[name_index_2]
    except ValueError:
        print(f"Missing data for {date}")
    else:
        highs_2.append(high)
        lows_2.append(low)
        dates_2.append(date)
open_file.close()



plt.subplot(2, 1, 1)
plt.plot(dates_1, highs_1, c="red")
plt.plot(dates_1, lows_1, c = "blue")
plt.fill_between(dates_1, highs_1, lows_1, facecolor = 'blue', alpha = 0.1)
plt.title(graph_title_1)

plt.subplot(2, 1, 2)
plt.plot(dates_2, highs_2, c= "red")
plt.plot(dates_2, lows_2, c="blue")
plt.fill_between(dates_2, highs_2, lows_2, facecolor = "blue", alpha = 0.1)
plt.title(graph_title_2)

plt.suptitle(f"Temperature comparison between {graph_title_1} and {graph_title_2}")

plt.show()
