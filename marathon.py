import mysql.connector
import pandas as pd


# Import het CSV bestand
df = pd.read_csv('marathon_results.csv')
df.head(3)

# Verbinding met de SQL Server
conn = mysql.connector.connect(
    host = "bit_academy",
    user = "bit-academy",
    password = "bit-academy")

# maak cursor aan zodat SQL query kan worden uitgevoerd na het schrijven ervan
cursor = conn.cursor()
print("CSV-bestand in de MySQL-database aan het laden...")

# Maak de tabel
cursor.execute("""DROP DATABASE IF EXISTS marathon;""")
cursor.execute("""CREATE DATABASE marathon;""")
cursor.execute("""USE marathon;""")
cursor.execute("""CREATE TABLE IF NOT EXISTS marathon (
    id          INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    year        INT(10),
    winner      VARCHAR(255),
    gender      VARCHAR(255),
    country     VARCHAR(255),
    time        TIME,
    marathon    VARCHAR(255)
);""")

# Data aan de tabel toevoegen
for index, row in df.iterrows():
    print(row)
    year = df['year']
    winner = df['winner']
    gender = df['gender']
    country = df['country']
    time = df['time']
    marathon = df['marathon']
    query = ("INSERT INTO marathon.marathon (year, winner, gender, country, time, marathon) VALUES (?,?,?,?,?,?)")
    values = [year, winner, gender, country, time, marathon]
cursor.execute(query, values)

# Commit veranderingen aan de database
conn.commit()

# check om te zien of het gelukt is
# Een nieuwe query maken die de gehele database 'marathon' selecteert
sql = "SELECT * FROM `marathon`"
cursor.execute(sql)

# de gegevens uit de database halen met een loop en printen
result = cursor.fetchall()
for i in result:
    print(i)

# Verbinding afsluiten
conn.close()
print("Bestand succesvol geladen!")
