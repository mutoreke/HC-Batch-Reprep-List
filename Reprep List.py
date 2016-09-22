#!Python 3
# Parses CSV file and stores it in the background
__author__ = 'KTM'
import csv, collections

AccessionID = []
TubeNo = []

exampleCSV = open('1.csv')
exampleReader = csv.reader(exampleCSV)
exampleData = list(exampleReader)


for row in exampleData[0:]:
    if row[2].isdecimal():
        AccessionID.append(row[2])

for i in range(1,len(AccessionID)+1):
    TubeNo.append(i)

Combined = {k: v for (k, v) in zip(AccessionID,TubeNo)}
print(Combined.get('195414',0))