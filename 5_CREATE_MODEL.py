import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report

from joblib import dump

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port=3307,
  database="boston_house_price"
)

def fetch_data():
    try:
        # Query to select data
        query = "SELECT * FROM boston_house_prices"
        # Use pandas to read data into a DataFrame
        df = pd.read_sql(query, mydb)
    finally:
        mydb.close()
    
    return df

# Fetch the data
data = fetch_data()
print("Data fetched from the database:")
print(data.head())

# Separate features and target variable
X = data[['LSTAT', 'RM', 'PTRATIO', 'INDUS', 'TAX']]
y = data['MEDV']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a model
model_rf = RandomForestRegressor()

model_rf.fit(X_train, y_train)

# Make predictions on the test set
y_pred_rf = model_rf.predict(X_test)

# Evaluate the model using score method
r2_score = model_rf.score(X_test, y_test)

print(f"R^2 Score: {r2_score:.2f}")

# Save the model to a file
model_filename_rf = 'trained_model_rf.pkl'
dump(model_rf, model_filename_rf)
print(f"Model saved to {model_filename_rf}")