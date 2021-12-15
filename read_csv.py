"""current date reader"""
import datetime
from typing import List

def read_csv(file:str)->List(tuple):
    """
    reads csv
    """
    date = datetime.date.today().strftime("%d/%m/%Y")
    date = date.replace("/",".")
    current_day = []
    with open(file, 'r', encoding="utf-8") as file_contents:
        file_contents.readline()
        data = file_contents.read().splitlines()
        for line in data:
            line_list = line.split(",")
            if line_list[0] == date:
                task = line_list[1]
                times = line_list[2]
                if line_list[3] != "*":
                    success = False
                elif line_list[3] == "*":
                    success = True
                current_day.append((date, task, times, success))
    return current_day
