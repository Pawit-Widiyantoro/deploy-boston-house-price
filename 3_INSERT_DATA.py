import mysql.connector
import pandas as pd

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="boston_house_price",
    port=3307
)

myCursor = db.cursor()

# Define the column names for the dataset
column_names = [
    'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 
    'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'
]

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('housing.csv', header=None, delimiter=r"\s+", names=column_names)

# Insert data into the table
for index, row in df.iterrows():
    query = """
    INSERT INTO boston_house_prices (
        CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT, MEDV
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        float(row['CRIM']), float(row['ZN']), float(row['INDUS']), int(row['CHAS']), 
        float(row['NOX']), float(row['RM']), float(row['AGE']), float(row['DIS']), 
        int(row['RAD']), float(row['TAX']), float(row['PTRATIO']), float(row['B']), 
        float(row['LSTAT']), float(row['MEDV'])
    )
    myCursor.execute(query, values)

# Commit the transaction
db.commit()

# Close the cursor and connection
myCursor.close()
db.close()

print("Data inserted successfully")
