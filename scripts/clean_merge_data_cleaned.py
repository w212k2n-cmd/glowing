
# clean_merge_data.py - Merge OWID Energy and Climate Temperature Data

import pandas as pd

# ------------------ Load Datasets ------------------
energy_df = pd.read_csv("owid-energy-data.csv")
temp_df = pd.read_csv("temperature_data.csv")

# ------------------ Preprocess Energy Data ------------------
energy_cols = ["country", "year", "energy_per_capita"]
energy_df = energy_df[energy_cols]
energy_df = energy_df.dropna(subset=["energy_per_capita"])

# ------------------ Preprocess Temperature Data ------------------
temp_cols = ["country", "year", "temp_anomaly"]
temp_df = temp_df[temp_cols]
temp_df = temp_df.dropna(subset=["temp_anomaly"])

# ------------------ Merge Datasets ------------------
merged_df = pd.merge(energy_df, temp_df, on=["country", "year"], how="inner")

# ------------------ Export Cleaned Data ------------------
output_path = "data/merged_energy_temp.csv"
merged_df.to_csv(output_path, index=False)

print(f"✅ Merged dataset saved to: {output_path}")
