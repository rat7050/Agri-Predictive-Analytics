# 🌾 Agri Predictive Analytics

A Machine Learning project that predicts crop yield using agricultural and weather-related data.

The main idea of this project is to understand how factors like rainfall, temperature, soil nutrients, irrigation, and previous crop yield can affect agricultural production.

## 🚀 Live Preview

Try the project here:

**[🌐 Open Agri Predict – Live Application](https://agri-predictive-analytics-m9efdzulyamnkeew7tzdwn.streamlit.app/)**

## 📌 Project Overview

Agri Predictive Analytics is a crop yield prediction project developed using Python and Machine Learning.

The application predicts crop yield around 6 weeks before harvest. Users can select a crop and district, enter agricultural conditions, and get an estimated yield prediction.

The project focuses on the Vidarbha region of Maharashtra.

## 🎯 Project Objectives

- Predict crop yield using Machine Learning.
- Understand the impact of weather conditions on crop production.
- Analyze historical crop yield.
- Identify possible crop yield shortfall risks.
- Present prediction results through an interactive Streamlit application.

## ✨ Features

- Crop and district selection.
- Crop yield prediction.
- Historical yield comparison.
- Rainfall and temperature-based analysis.
- Irrigation and soil condition inputs.
- Crop yield shortfall risk alert.
- Interactive charts for better understanding.
- Download prediction results as a CSV file.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data handling and analysis |
| NumPy | Numerical calculations |
| Scikit-learn | Machine Learning |
| Joblib | Model loading |
| Matplotlib | Data visualization |
| Streamlit | Web application |
| Jupyter Notebook | Model development and experimentation |

## 📊 Input Features

The application uses the following inputs for prediction:

- Crop
- District
- Previous three seasons' crop yield
- Rainfall compared to normal rainfall
- Maximum dry spell duration
- Number of weeks with temperature above 36°C
- Irrigated area share
- Soil nitrogen level
- Mandi price change

## 📈 Prediction Results

After entering the required details, the application displays:

- Predicted crop yield.
- Historical average yield.
- Difference between predicted and average yield.
- Crop shortfall risk alert.
- Historical vs predicted yield chart.
- CSV download option.

## 📁 Project Structure

```text
Agri-Predictive-Analytics/
│
├── dataset/
│   └── Dataset files
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│   └── Jupyter notebooks
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ How to Run the Project Locally

**Step 1: Clone the repository**

```bash
git clone https://github.com/rat7050/Agri-Predictive-Analytics.git
```

**Step 2: Open the project folder**

```bash
cd Agri-Predictive-Analytics
```

**Step 3: Create a virtual environment**

```bash
python -m venv venv
```

**Step 4: Activate the environment**

For Windows:

```bash
venv\Scripts\activate
```

**Step 5: Install required libraries**

```bash
pip install -r requirements.txt
```

**Step 6: Run the Streamlit application**

```bash
streamlit run app.py
```

The application will open in your browser.

## ⚠️ Important Note

This project currently uses synthetic, Vidarbha-style agricultural data for learning and demonstration purposes.

The predictions are experimental and should not be used for actual farming or financial decisions without validation using reliable real-world agricultural data.

## 📚 What I Learned

While working on this project, I learned:

- Data preprocessing and analysis.
- Working with agricultural datasets.
- Understanding Machine Learning models.
- Feature engineering.
- Model prediction and evaluation.
- Building interactive applications using Streamlit.
- Presenting Machine Learning results through visualizations.

## 👨‍💻 Developed By

**Ratnesh Kumar**

B.Tech – Artificial Intelligence & Data Science

Sagar Institute of Research & Technology - Excellence, Bhopal

- **GitHub:** [rat7050](https://github.com/rat7050)
- **LinkedIn:** [Ratnesh Kumar](https://www.linkedin.com/in/ratnesh-kumar-692376338/)

---

If you find this project interesting, feel free to explore the repository and try the live application.

⭐ Don't forget to give the repository a star!
