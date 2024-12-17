# Diabetes Health Indicator

## Overview
This project aims to predict the likelihood of diabetes in patients based on various health indicators. It uses machine learning algorithms to analyze patient data and provide a health indicator score.

## Documentation

[API Documentation](https://documenter.getpostman.com/view/39901805/2sAYJ1jh1c)

## How to Run
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/DiabetesHealthIndicator.git
    ```

2. Navigate to the project directory:
    ```sh
    cd DiabetesHealthIndicator
    ```

3. Create a Python environment:
   ```sh
   python -m venv venv
   ./venv/Scripts/activate
   ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Run the application:
    ```sh
    python main.py
    ```

## JSON Request and Response

### Request
The application expects a JSON request with the following format:
```json
{
    "HighBP": 1,
    "HighChol": 1,
    "BMI": 28.7,
    "Stroke": 0,
    "HeartDiseaseorAttack": 0,
    "PhysActivity": 1,
    "GenHlth": 3,
    "PhysHlth": 5,
    "DiffWalk": 0,
    "Age": 45,
    "Education": 4,
    "Income": 5
}
```

### Response
The application will respond with a JSON object containing the prediction result:
```json
{
    "prediction": 1
}
```
The prediction values are:
- 0: Low risk
- 1: Medium risk
- 2: High risk

