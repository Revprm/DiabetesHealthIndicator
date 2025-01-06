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

### Field Details

| Field                      | Type                   | Description                                                      | Valid Range                                                                                                                                     | Example |
| -------------------------- | ---------------------- | ---------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| BMI                        | Float                  | The Body Mass Index of the individual.                           | 0 to 100                                                                                                                                        | 28.7    |
| Age                        | Integer                | The age of the individual in years.                              | 18 to 120                                                                                                                                       | 45      |
| HighBP                     | Integer (Boolean-like) | Indicates high blood pressure diagnosis.                         | 1 = Yes, 0 = No                                                                                                                                 | 1       |
| HighChol                   | Integer (Boolean-like) | Indicates high cholesterol.                                      | 1 = Yes, 0 = No                                                                                                                                 | 1       |
| Stroke                     | Integer (Boolean-like) | Indicates if the individual has experienced a stroke.            | 1 = Yes, 0 = No                                                                                                                                 | 0       |
| HeartDiseaseorAttack       | Integer (Boolean-like) | Indicates heart disease or attack history.                       | 1 = Yes, 0 = No                                                                                                                                 | 0       |
| PhysActivity               | Integer (Boolean-like) | Indicates regular physical activity.                             | 1 = Yes, 0 = No                                                                                                                                 | 1       |
| DiffWalk                   | Integer (Boolean-like) | Indicates difficulty in walking or climbing stairs.              | 1 = Yes, 0 = No                                                                                                                                 | 0       |
| GenHlth (General Health)   | Integer                | Self-assessment of general health.                               | 1 = Poor, 2 = Fair, 3 = Good, 4 = Very Good, 5 = Excellent                                                                                      | 3       |
| PhysHlth (Physical Health) | Integer                | Number of days physical health was not good in the past 30 days. | 0 to 30                                                                                                                                         | 5       |
| Education                  | Integer                | Highest level of education attained.                             | 1 = No formal education, 2 = Some High School, 3 = High School Graduate, 4 = Some College, 5 = Bachelor’s Degree, 6 = Master’s Degree or Higher | 4       |
| Income                     | Integer                | Annual household income level.                                   | 1 = < $10k, 2 = $10k-$19,999, 3 = $20k-$29,999, 4 = $30k-$39,999, 5 = $40k-$49,999, 6 = $50k-$59,999, 7 = $60k-$69,999, 8 = ≥ $70k              | 5       |

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
