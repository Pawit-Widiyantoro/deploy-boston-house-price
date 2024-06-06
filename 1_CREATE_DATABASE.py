import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    port = 3307
)

myCursor = db.cursor()

query = "CREATE DATABASE boston_house_price"

myCursor.execute(query)

print("Database created!!!")

db.commit()
myCursor.close()
db.close()