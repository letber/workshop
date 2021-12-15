"""goaltracker"""


import csv
from genericpath import isfile
import os


if __name__ == "__main__":
    if isfile('goals.csv'):
        file1 = open('goals.csv', 'r', newline='')
        reader = csv.reader(file1)
        lines = []
        for row in reader:
            lines.append(row)
        lines = lines[1:]
        file1 = open('goals.csv', 'w', newline='')
    else:
        file1 = open('goals.csv', 'w', newline='')
        writer = csv.writer(file1)
        writer.writerow(["Days", "Number of times", "Success", "Failure"])
    print(lines)
    inp = input()
    while inp != 'Exit':
        if inp.startswith('create'):
            strings = inp.split(' ')
            num = int(strings[-1])
            task = " ".join(strings[1:-1])
            writer.writerow([f'{task} {num} times', 
                            0, 
                            "*" if 0 >= num else "", 
                            "*" if 0 < num else ""])

        inp = input()
    
    