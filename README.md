# 🌍 Air Quality Monitoring using AI/ML

This project is developed under the **AICTE Edunet Internship** with the theme:  
**Environmental Monitoring & Pollution Control**.  

The aim is to analyze **air quality data**, detect pollution trends, and build a simple machine learning model to predict the **Air Quality Index (AQI)** from various pollutants.

---

## 📊 Dataset
- **Source:** Kaggle (Air Quality Data in India, 2015–2020)  
- **File Used:** `city_day.csv`  
- Columns include:  
  - `City`, `Date`  
  - Pollutants: `PM2.5`, `PM10`, `NO2`, `SO2`, `CO`, `O3`  
  - `AQI` (Air Quality Index)

---

## ✅ Progress

### Week 1 (30%)
- Imported dataset into Jupyter Notebook (`.ipynb`).  
- Explored structure of dataset using `.info()`, `.describe()`.  
- Checked for missing values.  
- Displayed first few rows with `head()`.

### Week 2 (60%)
- Handled missing values by filling with mean.  
- Converted `Date` column to datetime format.  
- **EDA (Exploratory Data Analysis):**
  - AQI trends over time.  
  - Correlation heatmap between pollutants and AQI.  
- **ML Model:**
  - Built a Linear Regression model to predict AQI from pollutants.  
  - Evaluated with **RMSE** and **R² score**.  
  - Example prediction using sample pollutant values.  

---

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/sAchyn119/AirQualityMonitoring.git
   cd AirQualityMonitoring
2. Install dependencies:

    pip install -r requirements.txt


    (or manually install: pandas, numpy, matplotlib, seaborn, scikit-learn)

3. Run the Jupyter Notebook:

    jupyter notebook Week2_AQI_Project.ipynb