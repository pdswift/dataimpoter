import sqlite3

conn = sqlite3.connect('Dataimporter.db')
print ("Opened database successfully");

conn.execute(Dataimporter
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
                                )
print ("Table created successfully");

conn.close()
