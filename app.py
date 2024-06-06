import numpy as np
from flask import Flask, request, render_template, jsonify
import joblib

# Create Flask app
flask_app = Flask(__name__)
model = joblib.load(open("trained_model_rf.pkl", "rb"))

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
