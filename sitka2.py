import csv
import matplotlib.pyplot as plt
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []

# testing the datetime strip function
mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(mydate)
print(type(mydate))

for rec in csv_file:
    highs.append(int(rec[5]))
    date = datetime.strptime(rec[2], "%Y-%m-%d")
    dates.append(date)

print(highs)
print(dates)

fig = plt.figure()

plt.title("Daily High Temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)
# autoformat x-axis that had dates
fig.autofmt_xdate()
plt.plot(dates, highs, c="red")

plt.show()
