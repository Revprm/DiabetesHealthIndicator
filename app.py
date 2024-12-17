from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('models/XGBmodel.pkl')
scaler = joblib.load('models/scaler.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    prediction = model.predict([list(data.values())])

    output = prediction[0]
    return jsonify(output)