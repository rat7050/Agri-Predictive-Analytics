# 🌱 Agri Predictive Analytics Model

### Crop Yield Prediction Using Machine Learning

## 📌 About the Project

Agri Predictive Analytics is a machine learning project that predicts crop yield based on historical agricultural data and current season conditions.

The main aim of this project is to understand how different factors like rainfall, temperature, soil nitrogen, irrigation and previous crop yield affect agricultural production.

This project focuses on the Vidarbha region of Maharashtra, India. It provides a crop yield forecast approximately 6 weeks before harvest.

I built this project as part of my learning and internship work to understand how machine learning can be used to solve real-world agricultural problems.

## 🎯 Project Objectives

- Predict upcoming crop yield using Machine Learning.
- Analyze historical crop yield patterns.
- Understand the impact of weather and soil conditions.
- Identify potential crop yield shortfall risks.
- Present prediction results through an interactive dashboard.

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| Streamlit | Interactive dashboard |
| Plotly | Data visualization |
| Joblib | Saving and loading the trained model |
| Jupyter Notebook | Data analysis and experimentation |

## 📊 Project Features

**1. Crop Yield Prediction**

Predicts crop yield using historical yield records and current agricultural conditions.

**2. Multiple Crop & District Selection**

Users can select available crops and districts from the dashboard.

**3. Weather Analysis**

Considers rainfall, dry spells and high-temperature conditions.

**4. Soil & Irrigation Factors**

Uses soil nitrogen levels and irrigated area as prediction inputs.

**5. Shortfall Risk Detection**

Provides a shortfall warning when the model identifies a potential yield risk.

**6. Interactive Dashboard**

Built using Streamlit with different sections for overview, crop forecasting and model information.

**7. Forecast Visualization**

Compares historical crop yield with predicted yield using interactive charts.

**8. Download Forecast Report**

Allows users to download prediction results in CSV format.

## 🔍 Input Features

The model uses the following information:

- Crop Name
- District
- Previous Three Seasons' Yield
- Rainfall Compared to Normal
- Longest Dry Spell
- Weeks Above 36°C
- Irrigated Area Share
- Soil Nitrogen Level
- Mandi Price Change

## 📈 Prediction Output

The dashboard provides:

- Predicted Crop Yield (Quintals per Hectare)
- Historical Average Yield
- Yield Difference
- Potential Shortfall Risk
- Historical vs Predicted Yield Chart

## 📁 Project Structure

```text
Agri-Predictive-Analytics/
│
├── dataset/
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

## 🚀 How to Run the Project

Follow these steps to run the project on your local machine.

**Step 1: Clone the Repository**

```bash
git clone https://github.com/rat7050/Agri-Predictive-Analytics.git
```

**Step 2: Open the Project Folder**

```bash
cd Agri-Predictive-Analytics
```

**Step 3: Create a Virtual Environment (Recommended)**

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

**Step 4: Install Required Libraries**

```bash
pip install -r requirements.txt
```

**Step 5: Run the Streamlit Application**

```bash
streamlit run app.py
```

The application will open in your browser.

## ⚠️ Important Note

This project currently uses synthetic Vidarbha-style agricultural data for model development and experimentation.

The predictions are intended for learning and demonstration purposes. They should not be treated as actual agricultural forecasts without validation using real-world agricultural data.

## 🎓 What I Learned

While working on this project, I got practical experience with:

- Understanding agricultural data and its features.
- Data preprocessing and feature engineering.
- Working with Machine Learning models.
- Saving and loading trained models using Joblib.
- Connecting a trained ML model with Streamlit.
- Creating interactive dashboards and visualizations.
- Presenting prediction results in a user-friendly way.

## 👨‍💻 Developed By

**Ratnesh Kumar**

B.Tech – Artificial Intelligence & Data Science

Interested in Machine Learning, Data Science and solving real-world problems using data.

- GitHub: [@rat7050](https://github.com/rat7050)

---

⭐ If you find this project useful, feel free to explore the repository.

**Thanks for visiting!** 🌱
