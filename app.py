from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import logging

app = Flask(__name__, template_folder='templates')
CORS(app)
logging.basicConfig(level=logging.DEBUG)

model = joblib.load('models/XGBmodel.pkl')
scaler = joblib.load('models/scaler.pkl')

required_features = [
    "HighBP", "HighChol", "BMI", "Stroke", "HeartDiseaseorAttack",
    "PhysActivity", "GenHlth", "PhysHlth", "DiffWalk", "Age",
    "Education", "Income"
]

features_to_scale = ['BMI', 'GenHlth', 'PhysHlth', 'Age', 'Education', 'Income']

def validate_input_data(input_data):
    missing_features = [feature for feature in required_features if feature not in input_data]
    if missing_features:
        return jsonify({"error": f"Missing required features: {', '.join(missing_features)}"}), 400
    return None

def scale_input_features(input_data_values):
    features_to_scale_values = [input_data_values[required_features.index(feature)] for feature in features_to_scale]
    scaled_features = scaler.transform([features_to_scale_values])[0]
    
    for idx, feature in enumerate(features_to_scale):
        input_data_values[required_features.index(feature)] = scaled_features[idx]
    
    return input_data_values

def generate_prediction(input_data_values):
    prediction_result = model.predict([input_data_values])
    return int(prediction_result[0]) 

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the ML Prediction API!"}), 200

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return "Use POST to send data for prediction."

    try:
        input_data = request.get_json(force=True)

        validation_error = validate_input_data(input_data)
        if validation_error:
            return validation_error
        
        input_data_values = [input_data[feature] for feature in required_features]
        
        scaled_input_data = scale_input_features(input_data_values)
        
        prediction_value = generate_prediction(scaled_input_data)

        return jsonify({"prediction": prediction_value})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
