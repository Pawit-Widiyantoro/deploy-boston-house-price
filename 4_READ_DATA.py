import mysql.connector
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="boston_house_price",
    port = 3307
)

myCursor = db.cursor()

query = "SELECT * FROM boston_house_prices"

myCursor.execute(query)

results = myCursor.fetchall()
for row in results:
    print(row)

db.commit()

myCursor.close()

db.close()