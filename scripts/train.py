import pandas as pd
import joblib
from prophet import Prophet


# -----------------------------
# Load Dataset
# -----------------------------
file_path = "data/raw/PET_PNP_REFP2_DC_NUS_MBBL_M.xls"

df = pd.read_excel(
    file_path,
    sheet_name="Data 1"
)

# -----------------------------
# Clean Dataset
# -----------------------------
df.columns = df.iloc[1]
df = df.iloc[2:].reset_index(drop=True)

target = (
    "U.S. Refinery Net Production of Finished Motor Gasoline "
    "(Thousand Barrels)"
)

prophet_df = df[["Date", target]].copy()

prophet_df.columns = ["ds", "y"]

prophet_df = prophet_df.dropna()

prophet_df["ds"] = pd.to_datetime(prophet_df["ds"])
prophet_df["y"] = pd.to_numeric(prophet_df["y"])

# -----------------------------
# Train Prophet
# -----------------------------
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False,
    interval_width=0.95
)

model.fit(prophet_df)

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(
    model,
    "models/prophet_model.pkl"
)

print("====================================")
print("RefineX Training Completed")
print("Model saved successfully!")
print("====================================")