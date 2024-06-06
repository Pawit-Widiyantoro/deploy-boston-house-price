import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'boston_house_price',
    port = 3307
)

myCursor = db.cursor()

query = """
CREATE TABLE IF NOT EXISTS boston_house_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    CRIM FLOAT(20) NOT NULL,
    ZN FLOAT(20) NOT NULL,
    INDUS FLOAT(20) NOT NULL,
    CHAS TINYINT NOT NULL,
    NOX FLOAT(20) NOT NULL,
    RM FLOAT(20) NOT NULL,
    AGE FLOAT(20) NOT NULL,
    DIS FLOAT(20) NOT NULL,
    RAD INT NOT NULL,
    TAX FLOAT(20) NOT NULL,
    PTRATIO FLOAT(20) NOT NULL,
    B FLOAT(20) NOT NULL,
    LSTAT FLOAT(20) NOT NULL,
    MEDV FLOAT(20) NOT NULL
)
"""

myCursor.execute(query)

print("Table created!!!")

db.commit()
myCursor.close()
db.close()