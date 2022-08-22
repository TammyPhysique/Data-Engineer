import csv
import mysql.connector
import sys

mydb = mysql.connector.connct(
    host="127.0.0.1",
    user="bit-academy",
    password="",
    database="marathon"
    )

mycursor = mydb.cursor()

arg = sys,argv[1]

openbestand = open(arg)
leesbestand = csv.reader(openbestand)

if len (sys.argv)>1:
    print("CSV-bestand in MySQL-database aan het laden...")
    for row in leesbestand:
        mycursor.execute("INSERT INTO marathondata(year, winner, gender, country,         time, marathon)" \
        "VALUES(%s,%s,%s,%s,%s,%s)",
        row)
    print("Bestand succesvol geladen!")
else:
    print("ERROR: Geen bestandnaam geleverd!")

mydb.commit()
mydb.close()