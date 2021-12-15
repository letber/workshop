import sys
import datetime

def read_csv(file):
    """
    reads csv


    
    """
    date = datetime.date.today().strftime("%d/%m/%Y").replace("/",".")
    with open(file, 'r') as file_contents:
        file_contents.readline()
        data = file_contents.read().splitlines()

        for line in data:
            line_list = line.split(",")
            if line_list[0] == date:
                task = line_list[1]
                times = line_list[2]
 
                
            pass
x = 'a,b,c'
print(x.split(","))   
