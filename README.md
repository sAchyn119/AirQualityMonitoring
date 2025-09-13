# 🌍 Air Quality Monitoring using AI/ML - Final Project

## ✅ Objective  
Build an intelligent system to analyze air pollution data, detect trends, and predict Air Quality Index (AQI) based on pollutant values using machine learning. The system provides an interactive web application for live AQI prediction.

## ✅ Final Deliverables  
- ✅ Data Preprocessing  
  - Handled missing values by filling with column means  
  - Converted Date column into datetime format  
- ✅ Exploratory Data Analysis (EDA)  
  - AQI trend over time  
  - Correlation heatmap between pollutants and AQI  
- ✅ Machine Learning Models  
  - Linear Regression (baseline)  
  - Random Forest Regressor (final model selected based on performance)  
- ✅ Model Saving  
  - Saved best trained model as: `models/best_model.pkl`  
- ✅ Interactive Web App  
  - Built with **Streamlit**  
  - Allows live input of pollutant values to predict AQI  

## 🚀 How to Run the Project
pip install -r requirements.txt
### 2️⃣ Run the Streamlit App
streamlit run app.py

### 3️⃣ Open in Browser

Visit the displayed URL (usually http://localhost:8501) to use the AQI prediction app.

## ✅ Improvisations Done

Advanced data preprocessing (missing value handling, datetime parsing)

Clean and interactive visualizations (trend line + correlation heatmap)

Trained multiple ML models and selected the best-performing one

Example prediction functionality added

Simple and user-friendly web interface using Streamlit

## ✅ Project Folder Structure
AirQualityMonitoring/
│
├── app.py                 # Streamlit Web App  
├── models/  
│   └── best_model.pkl     # Saved trained Random Forest model  
├── data/  
│   └── city_day.csv       # Dataset file  
├── requirements.txt       # Required dependencies  
├── README.md              # Project description file  
├── Week3_Final_AQI_Project.ipynb  # Full project notebook  

# 👨‍💻 Author

Sachin Yadav
# Internship: AICTE Edunet 2025

# 📅 Year: 2025

## ✅ Sample requirements.txt Content
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
streamlit
