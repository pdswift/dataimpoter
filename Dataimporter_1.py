import csv

with open('Public_Computer_Access_Locations.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)

import sqlite3
#conn.execute('''CREATE TABLE Locations
conn = sqlite3.\
    connect('Dataimporter.db')
#print ("Opened database successfully");


conn.execute('''CREATE TABLE Locations
         (ID INT PRIMARY KEY     NOT NULL,
         Lab_name                TEXT,
         Phone                   TEXT,
         Accessible              TEXT,
         Hours                   TEXT,
         Tech_Support_Assisted   TEXT,
         Organization            TEXT,
         Location                TEXT,
         Web_address             TEXT,
         ADDRESS        CHAR(50),
         SALARY         REAL);
''')
print ("Table created successfully");

#conn.close()


with open('Public_Computer_Access_Locations.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    Lab_name = []
    Phone = []
    for row in readCSV:
       Lab_name =row[2]
       Phone = row[3]

       Lab_name.append(Lab_name)
       Phone.append(Phone)

    print(Lab_name)
    print(Phone)
