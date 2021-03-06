import os
import pandas as pd
import csv
from numpy import *

dirOfNetwork = os.path.dirname(__file__)

columnInQuestion = 21
dataMax = 0
dataMin = 0

print(columnInQuestion)

with open(dirOfNetwork + "/Datasets/mainData_Normalized.csv", "r") as sourceCSV:
    csvReaderHere = csv.reader(sourceCSV)
    dataMax = max(int(column[columnInQuestion].replace(',', '')) for column in csvReaderHere)
    print(dataMax)


with open(dirOfNetwork + "/Datasets/mainData_Normalized.csv", "r") as sourceCSV:
    csvReaderHere = csv.reader(sourceCSV)
    dataMin = min(int(column[columnInQuestion].replace(',', '')) for column in csvReaderHere)
    print(dataMin)

with open(dirOfNetwork + "/Datasets/mainData_Normalized.csv", "r") as sourceCSV:
    csvReaderHere = csv.reader(sourceCSV)
    with open(dirOfNetwork + "/Datasets/mainData_Normalized2.csv", "w") as resultCSV:
        csvWriterHere = csv.writer(resultCSV, lineterminator='\n')
        for row in csvReaderHere:
            row[columnInQuestion] = (int(row[columnInQuestion]) - dataMin)/(dataMax-dataMin)
            row[columnInQuestion] = "%.3f" % row[columnInQuestion]
            csvWriterHere.writerow(row)
# Max for column 2: 20
# Min for column 2: 15




