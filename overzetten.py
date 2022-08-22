import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Tam",
  password="U.]C_rAAxLq_f5AZ"
)

cursor = mydb.cursor()

db_create = "CREATE DATABASE IF NOT EXISTS python_novice"
db_select = "USE python_novice"
tbl_create = "CREATE TABLE IF NOT EXISTS users, name VARCHAR(255), gender VARCHAR(255), age INT(10), fav_color VARCHAR(255)"
tbl_insert = "INSERT INTO users (name, gender, age, fav_color) VALUES(%5, %5, %5, %5)"

cursor.execute(db_create)
cursor.execute(db_select)
cursor.execute(tbl_create)

with open("gebruikers.json") as json_file:
    gebruikers = json.load(json_file)

    for item in gebruikers:
        name = item["name"]
        gender = item["gender"]
        age = item["age"]
        fav_color = item["fav_color"]

cursor.execute(tbl_insert.format(name,gender, age, fav_color))
