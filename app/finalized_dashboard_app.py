
# app.py - Finalized Climate Impact Dashboard with Full Visual Integration
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Climate Impact Dashboard", layout="wide")

st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: #00f0ff;
        }
        h1, h2, h3, h4 {
            color: #00f0ff;
            text-shadow: 0 0 10px #00f0ff;
        }
        .stSlider > div[data-baseweb="slider"] > div {
            background: linear-gradient(90deg, #00f0ff, #ff00f0, #00ffcc);
            box-shadow: 0 0 12px #00f0ff;
            border-radius: 10px;
        }
        .stSlider label, .stMultiSelect label {
            color: #00f0ff !important;
            font-weight: bold;
        }
        .electric-flicker-box {
            padding: 12px;
            border-radius: 15px;
            animation: flickerGlow 1.8s infinite;
            border: 3px solid transparent;
            background: linear-gradient(#000, #000) padding-box,
                        linear-gradient(270deg, #a020f0, #00f0ff, #a020f0) border-box;
            background-size: 600% 600%;
            transition: box-shadow 0.3s ease-in-out;
        }
        .electric-flicker-box:hover {
            box-shadow: 0 0 28px #00f0ff, 0 0 48px #ff00ff;
        }
        @keyframes flickerGlow {
            0% { box-shadow: 0 0 10px #a020f0; }
            20% { box-shadow: 0 0 20px #00f0ff; }
            40% { box-shadow: 0 0 14px #a020f0; }
            60% { box-shadow: 0 0 24px #00f0ff; }
            80% { box-shadow: 0 0 12px #a020f0; }
            100% { box-shadow: 0 0 20px #00f0ff; }
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 Climate Impact Dashboard")

@st.cache_data
def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    df['temp_anomaly_f'] = df['temp_anomaly'] * 1.8
    return df

DATA_PATH = "data/merged_energy_temp.csv"

try:
    df = load_data(DATA_PATH)
except FileNotFoundError:
    st.error("❌ Merged data not found. Please run: `python scripts/clean_merge_data_cleaned.py`.")
    st.stop()

st.write("### 📋 Sample Data Preview")
st.dataframe(df.head())

st.subheader("⚡ Energy Use vs Temperature Anomaly (°F)")

year = st.slider("Select Year", int(df['year'].min()), int(df['year'].max()), 2020)
df_year = df[(df['year'] == year) & df['energy_per_capita'].notna() & df['temp_anomaly_f'].notna()]

if df_year.empty:
    st.warning("⚠️ No data available for the selected year.")
else:
    fig1 = px.scatter(
        df_year,
        x="energy_per_capita",
        y="temp_anomaly_f",
        color="country",
        hover_name="country",
        size_max=60,
        log_x=True,
        title=f"Energy per Capita vs Temperature Anomaly (°F) in {year}",
        labels={
            "energy_per_capita": "Energy per Capita (log scale)",
            "temp_anomaly_f": "Temperature Anomaly (°F)",
        },
    )
    fig1.update_traces(marker=dict(size=10, line=dict(width=1.5, color='white')))
    fig1.update_layout(
        margin=dict(l=40, r=40, t=60, b=40),
        plot_bgcolor='#0a0a0a',
        paper_bgcolor='#0a0a0a',
        font_color='#00f0ff',
        title_font_color='#00f0ff',
        hovermode='closest'
    )
    st.markdown('<div class="electric-flicker-box">', unsafe_allow_html=True)
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.subheader("📈 Temperature Anomaly Over Time")
st.markdown('<div class="electric-flicker-box">', unsafe_allow_html=True)

countries = st.multiselect(
    "Select Countries",
    sorted(df['country'].unique()),
    default=["United States", "China"]
)
df_line = df[df['country'].isin(countries)]

if df_line.empty:
    st.warning("⚠️ No data available for selected countries.")
else:
    fig2 = px.line(
        df_line,
        x="year",
        y="temp_anomaly_f",
        color="country",
        markers=True,
        title="Temperature Anomaly (°F) Over Time",
        labels={
            "year": "Year",
            "temp_anomaly_f": "Temperature Anomaly (°F)",
        },
    )
    fig2.update_layout(
        xaxis=dict(rangeslider=dict(visible=True)),
        yaxis_title="Anomaly (°F)",
        margin=dict(l=40, r=40, t=60, b=40),
        legend_title="Country",
        plot_bgcolor='#0a0a0a',
        paper_bgcolor='#0a0a0a',
        font_color='#00f0ff',
        title_font_color='#00f0ff',
        hovermode='x unified'
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
