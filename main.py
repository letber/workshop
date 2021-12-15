"""goaltracker"""


import csv
import os


if __name__ == "__main__":
    with open('goals.csv', 'w', newline='') as file1:
        writer = csv.writer(file1)
        writer.writerow(["Days", "Number of times", "Success", "Failure"])
    