# RefineX – AI-Based Production Forecasting

RefineX is an AI-powered production forecasting module developed as part of a larger refinery intelligence platform. The objective of this module is to forecast future refinery production using historical production trends through time-series forecasting.

Unlike traditional regression models, this project focuses on temporal patterns such as long-term trends and seasonality using Facebook Prophet, making it suitable for industrial production forecasting where historical behavior plays a significant role.

---

## Overview

This module is responsible for forecasting refinery production based on publicly available historical refinery production data provided by the U.S. Energy Information Administration (EIA).

The complete refinery intelligence platform consists of multiple independent modules including:

- Production Forecasting (This Module)
- Predictive Maintenance
- Incident Severity Prediction
- AI Recommendation Engine
- Flask Backend
- Frontend Dashboard

Each module is developed independently and later integrated through REST APIs.

---

## Features

- Historical refinery production forecasting
- Time-series forecasting using Facebook Prophet
- Automated model training
- Future production prediction
- Forecast export as CSV
- REST API using Flask
- Modular project architecture
- Ready for frontend integration

---

## Tech Stack

### Machine Learning

- Facebook Prophet
- Scikit-learn
- Pandas
- NumPy

### Backend

- Flask
- Joblib

### Visualization

- Matplotlib

### Development

- Python
- Jupyter Notebook
- Git
- GitHub

---

## Dataset

Since real refinery production datasets are confidential, this project uses publicly available production data from the **U.S. Energy Information Administration (EIA)**.

Dataset used:

**Refinery Net Production**

Characteristics:

- Monthly observations
- 1993 – 2026
- ~399 records
- Multiple refinery production products
- Historical industrial production data

Target Variable:

**U.S. Refinery Net Production of Finished Motor Gasoline (Thousand Barrels)**

---

## Project Structure

```text
RefineX-ProductionForecasting/

│── api/
│     app.py

│── data/
│     raw/
│     processed/

│── models/
│     prophet_model.pkl

│── notebooks/
│     01_EDA.ipynb
│     02_Model_Training.ipynb

│── reports/
│     production_forecast.csv

│── scripts/
│     inspect_data.py
│     train.py
│     predict.py

│── utils/

│── README.md
│── requirements.txt
│── .gitignore
```

---

## Workflow

```
Historical Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Preparation
        │
        ▼
Prophet Model Training
        │
        ▼
Model Serialization
        │
        ▼
Prediction Engine
        │
        ▼
Flask REST API
        │
        ▼
Frontend Dashboard
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Training

Train the forecasting model

```bash
python scripts/train.py
```

The trained model will be stored in

```
models/prophet_model.pkl
```

---

## Generate Forecast

Generate future production forecasts

```bash
python scripts/predict.py
```

Forecasts are exported to

```
reports/production_forecast.csv
```

---

## Run API

Start the Flask server

```bash
python api/app.py
```

Default server

```
http://127.0.0.1:5000
```

---

## API Endpoints

### GET /

Returns API status.

---

### GET /health

Health check endpoint.

---

### GET /predict

Returns production forecast in JSON format.

Example response

```json
{
    "next_month_prediction": 34820.96,
    "next_3_month_average": 41796.96,
    "next_12_month_average": 39413.49
}
```

---

## Model Performance

Evaluation was performed using a train-test split on historical production data.

Metrics evaluated:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

The trained Prophet model achieved approximately **5.27% MAPE** on the selected forecasting target.

---

## Current Status

- Completed project architecture
- Dataset exploration
- Data preprocessing
- Prophet model training
- Forecast generation
- Model serialization
- Flask REST API
- CSV forecast generation

---

## Future Improvements

- Daily production forecasting
- Weekly production forecasting
- Multiple refinery product forecasting
- Automated model retraining
- Interactive dashboard
- Docker deployment
- Cloud deployment
- Integration with real refinery datasets

---

## License

This project was developed for academic and internship purposes.
