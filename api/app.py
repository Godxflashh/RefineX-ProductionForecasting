from flask import Flask, jsonify
import joblib

app = Flask(__name__)

# ------------------------------------------------
# Load Model
# ------------------------------------------------

model = joblib.load("models/prophet_model.pkl")

print("✅ Prophet model loaded.")

# ------------------------------------------------
# Generate Forecast ONCE
# ------------------------------------------------

future = model.make_future_dataframe(
    periods=12,
    freq="MS"
)

forecast = model.predict(future)

# Prevent negative production values
forecast["yhat"] = forecast["yhat"].clip(lower=1)
forecast["yhat_lower"] = forecast["yhat_lower"].clip(lower=1)
forecast["yhat_upper"] = forecast["yhat_upper"].clip(lower=1)

print("✅ Forecast cache created.")

# ------------------------------------------------
# API
# ------------------------------------------------

@app.route("/")
def home():

    return jsonify({

        "project": "RefineX",

        "module": "Production Forecasting",

        "status": "Running"

    })


@app.route("/health")
def health():

    return jsonify({

        "status": "Healthy"

    })


@app.route("/predict")
def predict():

    prediction = forecast.tail(12)

    return jsonify({

        "next_month_prediction":

            round(float(prediction.iloc[0]["yhat"]),2),

        "next_3_month_average":

            round(float(prediction.head(3)["yhat"].mean()),2),

        "next_12_month_average":

            round(float(prediction["yhat"].mean()),2)

    })


if __name__ == "__main__":

    app.run(

        debug=True,

        port=5000

    )