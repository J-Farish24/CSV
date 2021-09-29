import csv
import matplotlib.pyplot as plt
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)
    if column_header == "TMAX":
        high_index = index
    elif column_header == "TMIN":
        low_index = index
    elif column_header == "DATE":
        date_index = index

highs = []
lows = []
dates = []

# testing the datetime strip function
# mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(mydate)
# print(type(mydate))

for rec in csv_file:
    try:
        date = datetime.strptime(rec[date_index], "%Y-%m-%d")
        high = int(rec[high_index])
        low = int(rec[low_index])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(date)

# print(highs)
# print(dates)

fig = plt.figure()

plt.title("Daily Highs amd Lows Temperature - 2018\nDeath Valley", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)
# autoformat x-axis that had dates
fig.autofmt_xdate()
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.show()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.title("Highs")

plt.subplot(2, 1, 2)
plt.plot(dates, lows, c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Death Valley, Arizona")

plt.show()
