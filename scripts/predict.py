from pathlib import Path
import joblib
import pandas as pd

# ------------------------------------------------
# Project Root
# ------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models" / "prophet_model.pkl"
REPORT_PATH = PROJECT_ROOT / "reports" / "production_forecast.csv"

print("Loading model...")

model = joblib.load(MODEL_PATH)

print("Model loaded successfully!")

future = model.make_future_dataframe(
    periods=12,
    freq="MS"
)

forecast = model.predict(future)

forecast["yhat"] = forecast["yhat"].clip(lower=1)
forecast["yhat_lower"] = forecast["yhat_lower"].clip(lower=1)
forecast["yhat_upper"] = forecast["yhat_upper"].clip(lower=1)

forecast = forecast[
    ["ds", "yhat", "yhat_lower", "yhat_upper"]
].tail(12)

forecast.columns = [
    "Date",
    "Predicted Production",
    "Lower Bound",
    "Upper Bound"
]

print("\n========== NEXT 12 MONTH FORECAST ==========\n")

print(forecast)

forecast.to_csv(
    REPORT_PATH,
    index=False
)

print(f"\nForecast saved to:\n{REPORT_PATH}")