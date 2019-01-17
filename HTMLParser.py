from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen
from collections import Counter
import re
import csv

PAGENUMBER = 1
ARAWDATA = []
BRAWDATA = []
OFFICIALDATA = {}
NUMBERS = []
TIMES = []
CHANCE = []
zc = 0

while PAGENUMBER <= 83:  
    COUNTER = 0  
    RAW = url.read()  
    url.close()  
    PARSED = Soup(RAW, 'html.parser')  

    for line in PARSED.findAll('td', {'align': 'right'}):  
        if 'mega-millions-drawing.asp?d=' in str(line):  
            pRAW = re.findall('d=(.*?)\">', str(line))  
            for pline in pRAW:
                ARAWDATA.append(pline)  

    for line in PARSED.findAll('td', {'align': 'center'}):
        if '<strong>' in str(line) and 'nowrap' in str(line):  
            pRAW = re.findall('<b>(.*?)</b>', str(line))
            for pline in pRAW:
                BRAWDATA.append(pline.replace(" · ", " "))

    for date in ARAWDATA:
        OFFICIALDATA[date] = BRAWDATA[COUNTER]  
        COUNTER += 1
    PAGENUMBER += 1

with open('lotto.csv', 'w') as data:
    file = csv.writer(data)
    file.writerows(OFFICIALDATA.items())


def frequency(list):
    global zc
    BUFFED = [] 
    for line in list:
        buffer = line.split()
        for bbuffer in buffer:
            BUFFED.append(bbuffer)
    STORED = Counter(BUFFED)  
    zc = len(STORED)  

    with open('occurrence.csv', 'w') as data:
        file = csv.writer(data)
        file.writerows(STORED.items())


def solution():
    with open('occurrence.csv', 'r') as data:
        fileReader = csv.reader(data)
        for row in fileReader:
            NUMBERS.append(row[0])  
            TIMES.append(row[1]) 
            a = str((int(row[1]) / len(BRAWDATA)))  
            CHANCE.append(a[2:4]) 


REPORT = {  
    'Numbers': NUMBERS,
    'Times': TIMES,
    'Chance': CHANCE,
}

frequency(BRAWDATA)
solution()

with open('report.csv', 'w') as data:
    dataWriter = csv.writer(data)
    z = 0
    while z < zc:  
        dataWriter.writerow([
            str(REPORT['Numbers'][z]),
            str(REPORT['Times'][z]),
            str(REPORT['Chance'][z]),
        ])
        z += 1

