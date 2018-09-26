import csv
import sqlite3
with open('Public_Computer_Access_Locations.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)


#conn.execute('''CREATE TABLE Locations
conn = sqlite3.\
    connect('Dataimporter.db')
#print ("Opened database successfully");


conn.execute('''CREATE TABLE Locations
         (
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
('INSERT INTO LOCATIONS (Lab_name,Phone,Accessible,Hours,Tech_Support_Assisted,Organization,Location, Web_address) \
VALUES (Lab_name,Phone,Accessible,Hours,Tech_Support_Assisted,Organization,Location, Web_address)')



