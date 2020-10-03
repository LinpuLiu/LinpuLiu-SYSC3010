import sqlite3
dbconnect = sqlite3.connect("sensors.db");
cursor = dbconnect.cursor();
cursor.execute('''CREATE TABLE sensors(sensorID NUMERIC, type TEXT, zone TEXT)''');
cursor.execute('''INSERT INTO sensors values(1, "door", "kitchen")''')
dbconnect.commit()
cursor.execute('''INSERT INTO sensors values(2, "temperature", "kitchen")''');
dbconnect.commit()
cursor.execute('''INSERT INTO sensors values(3, "door", "garage")''');
dbconnect.commit()
cursor.execute('''INSERT INTO sensors values(4, "motion", "garage")''');
dbconnect.commit()
cursor.execute('''INSERT INTO sensors values(5, "temperature", "garage")''');
dbconnect.commit()
cursor.execute('SELECT type FROM sensors WHERE zone = "kitchen"');
records = cursor.fetchall()
for row in records:
    print("display all the sensors in the kitchen:   " + row[0])
cursor.execute('SELECT zone FROM sensors WHERE type = "door"');
records = cursor.fetchall()
for row in records:
    print("display all the door sensors:       " + row[0])

dbconnect.commit;
dbconnect.close();


