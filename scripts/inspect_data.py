import pandas as pd

# Load Excel file
df = pd.read_excel(
    "data/raw/PET_PNP_REFP2_DC_NUS_MBBL_M.xls",
    sheet_name="Data 1",
    header=2
)

print(df.head())

print(df.info())

print(df.describe())