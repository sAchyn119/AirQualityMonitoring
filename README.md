# 🌍 Air Quality Monitoring using AI/ML

## ✅ Project Overview  
Environmental pollution is a major global issue affecting public health and ecosystems. This project leverages **Artificial Intelligence (AI)** and **Machine Learning (ML)** to monitor air pollution data, analyze trends, and predict the **Air Quality Index (AQI)** in real time based on pollutant values.  
An interactive web app built with **Streamlit** allows easy and fast AQI prediction for different pollutant inputs.

## 🎯 Objective  
- Preprocess and clean real-world air pollution dataset  
- Perform Exploratory Data Analysis (EDA) to understand pollutant patterns  
- Build and compare multiple ML models  
- Deploy the best model in an interactive web app for real-time predictions  
- Enable easy use without coding knowledge

## ✅ Key Features & Deliverables  

### 🧹 Data Preprocessing  
- Handle missing values by filling with column means  
- Convert the Date column to proper datetime format  
- Drop rows with remaining NaN values as necessary

### 📊 Exploratory Data Analysis (EDA)  
- Line plot showing AQI trends over time per city  
- Correlation heatmap to visualize relationships between pollutants and AQI  

### 🤖 Machine Learning Models  
- Baseline model: Linear Regression  
- Final selected model: Random Forest Regressor (based on performance metrics)  

### 💾 Model Persistence  
- Best model saved as: `models/best_model.pkl` using **Joblib**  
- Enables fast loading without retraining
- 📥 Model Download Link:  
  https://drive.google.com/file/d/14R8VnfZA8aPdHW9m19TDQ_RFWXsAFzYB/view?usp=sharing 

### 🌐 Interactive Web Application  
- Built using **Streamlit**  
- Simple and clean UI to input pollutant values  
- Predicts AQI instantly and displays results

## 🚀 How to Run

### 1️⃣ Install Dependencies  
pip install -r requirements.txt
### 2️⃣ Run the Streamlit Application
streamlit run app.py
### 3️⃣ Open the Web Interface
Open your browser and visit:
http://localhost:8501

## ✅ Example Input (Streamlit App)
Parameter  	Value
PM2.5	      120
PM10	      150
NO2        	40
SO2	        20
CO	        1.2
O3        	30

# 👉 The app will display the predicted AQI immediately.

## ✅ Project Folder Structure
AirQualityMonitoring/
│
├── app.py                           # Streamlit Web App for AQI prediction  
├── models/  
│   └── best_model.pkl               # Saved trained Random Forest model  
├── data/  
│   └── city_day.csv                 # Air Quality dataset (2015-2020)  
├── requirements.txt                 # Required Python dependencies  
├── README.md                        # Project description & instructions  
├── Week3_Final_AQI_Project.ipynb    # Complete project notebook (EDA + Model Training)  

## 📚 Technologies & Libraries Used

Python

Pandas, NumPy → Data manipulation

Scikit-learn → Machine learning models (Linear Regression, Random Forest)

Matplotlib, Seaborn → Visualization

Joblib → Model persistence

Streamlit → Interactive Web App

## ✅ Key Improvements & Innovations

Robust data preprocessing with handling of missing values

Interactive and clean visualizations

Comparison of ML models to select the best one

Deployed a user-friendly Streamlit web app for real-time predictions

Example input for easy demonstration of predictions

Well-structured project ready for production

# 👨‍💻 Author
Sachin Yadav
# AICTE Edunet Internship – 2025
📅 Year: 2025
