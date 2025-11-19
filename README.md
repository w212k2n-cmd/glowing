# ⚡ Glow Climate Dashboard
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/launch?repository=https://github.com/w212k2n-cmd/glowing&main=app/finalized_dashboard_app.py)


A futuristic Streamlit app that visualizes energy consumption and climate anomaly data with glowing neon UI effects.

## 🔹 Features
- Animated borders and hover glows
- Log-scaled energy vs anomaly scatter plot
- Interactive temperature anomaly line chart
- Dark theme with particle-style ambiance

## 📦 Install Requirements

```bash
pip install -r requirements.txt
```

## 🛠️ Generate Merged Data

```bash
python scripts/clean_merge_data_cleaned.py
```

## 🚀 Run the App

```bash
streamlit run app/finalized_dashboard_app.py
```

## 📁 Data Sources
- [OWID Energy Data](https://ourworldindata.org/energy)
- [NOAA Temperature Data](https://www.ncei.noaa.gov/)
