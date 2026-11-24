
import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
from datetime import datetime

# PAGE CONFIGURATION

st.set_page_config(
    page_title="Agri Predict | Crop Intelligence",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. LOAD ML MODEL

@st.cache_resource
def load_model():
    return joblib.load("models/best_model.pkl")


BUNDLE = load_model()
FEATS = BUNDLE["features"]

# 3. SESSION STATE & NAVIGATION


if "page" not in st.session_state:
    st.session_state["page"] = "Overview"


def go_to_forecast():
    st.session_state["page"] = "Crop Forecast"


def go_to_overview():
    st.session_state["page"] = "Overview"


# 4. CUSTOM CSS

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f5f8f5;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: #102b20;
}

[data-testid="stSidebar"] * {
    color: #ffffff;
}

/* Main Heading */

.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #173d2c;
    margin-bottom: 5px;
}

.subtitle {
    color: #829087;
    font-size: 14px;
    margin-bottom: 28px;
}

/* Section Heading */

.section-title {
    color: #173d2c;
    font-size: 22px;
    font-weight: 700;
    margin-top: 15px;
    margin-bottom: 15px;
}

/* Metric Cards */

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e4eee5;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
}

div[data-testid="stMetricLabel"] {
    color: #738078;
}

div[data-testid="stMetricValue"] {
    color: #173d2c;
    font-weight: 800;
}

/* Buttons */

div.stButton > button {
    background: #198754;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 25px;
    font-weight: 700;
    transition: 0.2s;
}

div.stButton > button:hover {
    background: #126c40;
    color: white;
    border: none;
    transform: translateY(-2px);
}

/* Form */

div[data-testid="stForm"] {
    background: white;
    padding: 22px;
    border: 1px solid #e4eee5;
    border-radius: 15px;
}

/* Footer */

.footer {
    text-align: center;
    color: #89958d;
    padding: 25px;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)

# 5. FORECAST FUNCTION

def forecast(crop, district, lag1, lag2, lag3, **inputs):

    row = dict(BUNDLE["defaults"])
    row.update(inputs)

    lags = [lag1, lag2, lag3]

    baseline = sum(lags) / 3

    row["yield_lag1"] = lag1
    row["yield_lag2"] = lag2
    row["yield_lag3"] = lag3

    row["yield_roll3_mean"] = baseline
    row["yield_roll3_std"] = pd.Series(lags).std()
    row["yield_trend"] = lag1 / baseline

    row["crop_code"] = BUNDLE["crops"].index(crop)
    row["district_code"] = BUNDLE["districts"].index(district)

    x = pd.DataFrame([row])[FEATS]

    ratio_raw = float(BUNDLE["model"].predict(x)[0])

    ratio = (
        ratio_raw
        + BUNDLE["district_offsets"].get(district, 0.0)
    )

    alert = ratio_raw <= BUNDLE["shortfall_threshold"]

    return ratio * baseline, baseline, alert

# 6. SIDEBAR NAVIGATION


with st.sidebar:

    st.markdown("## 🌱 AGRI PREDICT")
    st.caption("Crop Intelligence Platform")

    st.markdown("---")

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Crop Forecast",
            "About Model"
        ],
        key="page"
    )

    st.markdown("---")

    st.markdown("### 📍 Coverage")

    st.write("Vidarbha Region")
    st.write("Maharashtra, India")

    st.markdown("---")

    st.caption("Machine Learning Powered")
    st.caption("Agri Predict v1.0")

# 7. OVERVIEW PAGE


if page == "Overview":

    st.markdown(
        '<div class="main-title">Crop Intelligence Dashboard 🌱</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Monitor agricultural conditions and forecast crop yield using machine learning.</div>',
        unsafe_allow_html=True
    )

    # Dashboard Statistics

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Available Crops",
        len(BUNDLE["crops"])
    )

    c2.metric(
        "District Coverage",
        len(BUNDLE["districts"])
    )

    c3.metric(
        "Forecast Period",
        "6 Weeks"
    )

    st.markdown("---")

    st.markdown(
        '<div class="section-title">Explore Crop Forecasting</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([1.2, 1])

    with left:

        st.markdown("### 🌾 Crop Yield Prediction")

        st.write(
            "Estimate crop yield using historical production, "
            "rainfall, temperature, irrigation and soil nitrogen."
        )

        st.button(
            "Start Forecast →",
            on_click=go_to_forecast,
            use_container_width=False
        )

    with right:

        st.markdown("### 📊 Agricultural Analytics")

        st.write(
            "Understand historical yield trends, forecast "
            "performance and potential shortfall risks."
        )

    st.markdown("---")

    st.markdown("### Available Crops")

    crop_icons = ["🌱", "🌾", "🌿", "🪴", "🌱"]

    crop_cols = st.columns(min(len(BUNDLE["crops"]), 4))

    for i, crop in enumerate(BUNDLE["crops"]):

        with crop_cols[i % len(crop_cols)]:

            st.markdown(
                f"### {crop_icons[i % len(crop_icons)]} {crop.title()}"
            )


# 8. CROP FORECAST PAGE


elif page == "Crop Forecast":

    st.markdown(
        '<div class="main-title">Crop Yield Forecast 🌱</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Enter agricultural conditions to estimate upcoming crop yield.</div>',
        unsafe_allow_html=True
    )

    with st.form("forecast_form"):

        st.markdown("### 🌾 Crop Information")

        col1, col2 = st.columns(2)

        with col1:

            crop = st.selectbox(
                "Select Crop",
                BUNDLE["crops"]
            )

        with col2:

            district = st.selectbox(
                "Select District",
                BUNDLE["districts"]
            )

        st.markdown("---")

        st.markdown("### 📈 Historical Yield Data")

        st.caption("Previous three seasons (quintals per hectare)")

        a, b, c = st.columns(3)

        with a:

            lag1 = st.number_input(
                "Last Season",
                min_value=1.0,
                max_value=80.0,
                value=10.0
            )

        with b:

            lag2 = st.number_input(
                "Two Seasons Ago",
                min_value=1.0,
                max_value=80.0,
                value=10.0
            )

        with c:

            lag3 = st.number_input(
                "Three Seasons Ago",
                min_value=1.0,
                max_value=80.0,
                value=10.0
            )

        st.markdown("---")

        st.markdown("### 🌦️ Current Season Conditions")

        col1, col2 = st.columns(2)

        with col1:

            rain = st.slider(
                "Rainfall Compared to Normal",
                0.3, 2.0, 1.0, 0.05
            )

            dry = st.slider(
                "Longest Dry Spell (Weeks)",
                0, 20, 5
            )

            heat = st.slider(
                "Weeks Above 36°C",
                0, 15, 2
            )

        with col2:

            irrigation = st.slider(
                "Irrigated Share of Area",
                0.0, 0.8, 0.25, 0.05
            )

            nitrogen = st.number_input(
                "Soil Nitrogen (kg/ha)",
                100.0, 400.0, 250.0
            )

            price = st.slider(
                "Mandi Price Change (%)",
                -30, 30, 0
            )

        st.markdown("---")

        submitted = st.form_submit_button(
            "🌱 Generate Yield Forecast",
            use_container_width=True
        )

    # ======================================
    # GENERATE PREDICTION
    # ======================================

    if submitted:

        try:

            with st.spinner("Analyzing agricultural data..."):

                pred, baseline, alert = forecast(
                    crop,
                    district,
                    lag1,
                    lag2,
                    lag3,
                    weeks_to_harvest=6,
                    cum_rain_ratio=rain,
                    dry_run_max=dry,
                    cum_heat=heat,
                    irrigated_share=irrigation,
                    soil_N=nitrogen,
                    price_yoy=price / 100
                )

                st.session_state["forecast_result"] = {
                    "crop": crop,
                    "district": district,
                    "pred": pred,
                    "baseline": baseline,
                    "alert": alert,
                    "lags": [lag3, lag2, lag1]
                }

        except Exception as e:

            st.error(f"Forecast failed: {e}")

    # DISPLAY PREDICTION RESULT

    if "forecast_result" in st.session_state:

        result = st.session_state["forecast_result"]

        st.markdown("---")

        st.markdown("## 📊 Forecast Results")

        st.caption(
            f'{result["crop"].title()} • '
            f'{result["district"]} • '
            '6 weeks before harvest'
        )

        pred = result["pred"]
        baseline = result["baseline"]
        alert = result["alert"]

        change = pred - baseline

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Predicted Yield",
            f"{pred:.2f} q/ha",
            f"{change:+.2f} q/ha"
        )

        col2.metric(
            "Historical Average",
            f"{baseline:.2f} q/ha"
        )

        col3.metric(
            "Yield Difference",
            f"{(change / baseline) * 100:+.1f}%"
        )

        if alert:

            st.error(
                "⚠️ Shortfall Risk Detected! "
                "Forecast indicates a potential yield shortfall. "
                "Consider reviewing supply requirements."
            )

        else:

            st.success(
                "✓ No shortfall alert detected by the model."
            )

        # Yield Chart

        st.markdown("### 📈 Historical vs Predicted Yield")

        chart_data = pd.DataFrame({

            "Season": [
                "3 Seasons Ago",
                "2 Seasons Ago",
                "Last Season",
                "This Season (Forecast)"
            ],

            "Yield": result["lags"] + [pred]

        })

        fig = px.bar(
            chart_data,
            x="Season",
            y="Yield",
            color="Season",
            text_auto=".2f",
            color_discrete_sequence=[
                "#A8C8AD",
                "#75A981",
                "#43865A",
                "#176B3A"
            ]
        )

        fig.update_layout(
            showlegend=False,
            plot_bgcolor="white",
            paper_bgcolor="white",
            font_color="#173D2C",
            yaxis_title="Yield (q/ha)",
            xaxis_title="",
            margin=dict(t=25, b=20)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Download Report

        report = pd.DataFrame([{

            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),

            "Crop": result["crop"],

            "District": result["district"],

            "Predicted Yield (q/ha)": round(pred, 2),

            "Historical Average (q/ha)": round(baseline, 2),

            "Yield Difference": round(change, 2),

            "Shortfall Risk": "Yes" if alert else "No"

        }])

        st.download_button(
            "⬇️ Download Forecast Report",
            data=report.to_csv(index=False),
            file_name="crop_yield_forecast.csv",
            mime="text/csv"
        )

        if st.button("← Back to Overview"):
            go_to_overview()
            st.rerun()


# 9. ABOUT MODEL PAGE

elif page == "About Model":

    st.markdown(
        '<div class="main-title">About the ML Model 🤖</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Understand how Agri Predict generates crop yield forecasts.</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Prediction Process")

    steps = [

        ("01", "Historical Yield",
         "Previous three seasons of crop yield data."),

        ("02", "Weather Conditions",
         "Rainfall, dry spells and high temperatures."),

        ("03", "Soil & Irrigation",
         "Nitrogen availability and irrigated area."),

        ("04", "Machine Learning",
         "The trained model estimates yield relative to historical baseline."),

        ("05", "Forecast Output",
         "Predicted yield and shortfall risk.")

    ]

    for number, title, description in steps:

        with st.container(border=True):

            col1, col2 = st.columns([0.15, 0.85])

            with col1:
                st.markdown(f"### {number}")

            with col2:
                st.markdown(f"**{title}**")
                st.caption(description)

    st.markdown("---")

    st.markdown("### 📌 Model Information")

    st.write("**Forecast Timing:** Approximately 6 weeks before harvest")

    st.write("**Geographical Style:** Vidarbha, Maharashtra")

    st.write("**Model Input:** Historical yield, weather and soil conditions")

    st.write("**Training Data:** Synthetic Vidarbha-style data")

    st.info(
        "This is an experimental predictive analytics project. "
        "Forecasts should be validated against real agricultural "
        "observations before actual farming decisions."
    )

# 10. FOOTER

st.markdown("---")

st.markdown(
    '<div class="footer">'
    '🌱 AGRI PREDICT | Crop Intelligence Platform '
    '| Built By Ratnesh Kumar'
    '</div>',
    unsafe_allow_html=True
)
