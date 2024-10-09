import numpy as np
from flask import Flask, request, render_template, jsonify
import joblib
import os

# Create Flask app
# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # One level up to project root

# Create Flask app and set the template folder explicitly
flask_app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))

# Load the trained model using the absolute path
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trained_model_rf.pkl')
model = joblib.load(open(model_path, "rb"))

# Define feature names
feature_names = ['LSTAT', 'RM', 'PTRATIO', 'INDUS', 'TAX']

@flask_app.route("/")
def Home():
    return render_template("index.html", prediction_text="")

@flask_app.route("/predict/api", methods=["POST"])
def predict_api():
    # Create a dictionary with feature names as keys and their corresponding values
    input_data = {feature: float(request.form[feature]) for feature in feature_names}
    
    # Create numpy array with the input data
    arr = np.array([[input_data[feature] for feature in feature_names]])

    print("Input Data:", input_data)
    print("Array:", arr)

    pred = model.predict(arr)
    print("Prediction:", pred)

    return jsonify({'prediction': pred.tolist()})


@flask_app.route("/predict", methods=["POST"])
def predict():
    # instantiate predict_api()
    response = predict_api()

    # convert predicted values from float to string
    prediction = ', '.join(map(str, response.get_json()['prediction']))
    
    return render_template("index.html", prediction_text="Harga Rumah = {} USD".format(prediction))


if __name__ == "__main__":
    flask_app.run(debug=True)
