from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict
import joblib
import uvicorn
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize FastAPI app
app = FastAPI(title="ML Prediction API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models
model = joblib.load('models/final_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# Define constants
REQUIRED_FEATURES = [
    "HighBP", "HighChol", "BMI", "Stroke", "HeartDiseaseorAttack",
    "PhysActivity", "GenHlth", "PhysHlth", "DiffWalk", "Age",
    "Education", "Income"
]

FEATURES_TO_SCALE = ['BMI', 'GenHlth', 'PhysHlth', 'Age', 'Education', 'Income']

# Define request model
class PredictionInput(BaseModel):
    HighBP: int = Field(..., description="High Blood Pressure")
    HighChol: int = Field(..., description="High Cholesterol")
    BMI: float = Field(..., description="Body Mass Index")
    Stroke: int = Field(..., description="Stroke History")
    HeartDiseaseorAttack: int = Field(..., description="Heart Disease or Attack History")
    PhysActivity: int = Field(..., description="Physical Activity")
    GenHlth: int = Field(..., description="General Health")
    PhysHlth: float = Field(..., description="Physical Health")
    DiffWalk: int = Field(..., description="Difficulty Walking")
    Age: int = Field(..., description="Age")
    Education: int = Field(..., description="Education Level")
    Income: int = Field(..., description="Income Level")

# Define response model
class PredictionResponse(BaseModel):
    prediction: int
    confidence: float

def scale_input_features(input_data: List[float]) -> List[float]:
    """Scale the input features using the pre-trained scaler."""
    features_to_scale_values = [input_data[REQUIRED_FEATURES.index(feature)] 
                              for feature in FEATURES_TO_SCALE]
    scaled_features = scaler.transform([features_to_scale_values])[0]
    
    for idx, feature in enumerate(FEATURES_TO_SCALE):
        input_data[REQUIRED_FEATURES.index(feature)] = scaled_features[idx]
    
    return input_data

def generate_prediction(input_data: List[float]) -> tuple[int, float]:
    """Generate prediction and confidence score."""
    prediction = int(model.predict([input_data])[0])
    confidence = float(model.predict_proba([input_data])[0][prediction])
    return prediction, confidence

@app.get("/")
async def home():
    """Root endpoint."""
    return {"message": "Welcome to the ML Prediction API!"}

@app.post("/predict", response_model=PredictionResponse)
async def predict(input_data: PredictionInput):
    """
    Make a prediction based on the input features.
    Returns prediction and confidence score.
    """
    try:
        # Convert input data to list in correct order
        input_values = [getattr(input_data, feature) for feature in REQUIRED_FEATURES]
        
        # Scale features
        scaled_input = scale_input_features(input_values)
        
        # Generate prediction
        prediction_value, confidence_value = generate_prediction(scaled_input)
        
        return PredictionResponse(
            prediction=prediction_value,
            confidence=confidence_value
        )
        
    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)