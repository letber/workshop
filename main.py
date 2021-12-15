"""goaltracker"""


import csv
import os


if __name__ == "__main__":
    file1 = open('goals.csv', 'w', newline='')
    writer = csv.writer(file1)
    writer.writerow(["Days", "Number of times", "Success", "Failure"])
        
    inp = input()
    if inp.startswith('create'):
        strings = inp.split(' ')
        num = int(strings[-1])
        task = " ".join(strings[1:-1])
        writer.writerow([f'{task} {num} times', 
                        0, 
                        "*" if 0 >= num else "", 
                        "*" if 0 < num else ""])
    