# Check win rate of the bot

import csv
import os

for i in range(1000):
    os.system("python test.py")

total = 0
win = 0
loose = 0

with open('out.csv', newline='') as f: 
    reader = csv.reader(f)
    for row in reader:
        total += 1
        if row[0] == '1':
            win += 1
        else:
            loose += 1

print("Total: ", total)
print("Win: ", win)
print("Loose: ", loose)
print("Win Rate: ", win/total*100, "%")
print("Loose Rate: ", loose/total*100, "%")