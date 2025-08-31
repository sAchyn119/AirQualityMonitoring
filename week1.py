# Week 1 Project - Environmental Monitoring & Pollution Control
# Theme: Air Quality Monitoring using AI/ML
# Step 1: Import necessary libraries

import pandas as pd
import numpy as np

# Step 2: Load the dataset
# (Make sure city_day.csv is in the same folder as this notebook)
df = pd.read_csv("city_day.csv")

# Step 3: Explore the dataset
print("------ Dataset Info ------")
print(df.info())

print("\n------ Summary Statistics ------")
print(df.describe())

print("\n------ Missing Values ------")
print(df.isnull().sum())

# Optional: Show first 5 rows
print("\n------ Sample Data ------")
print(df.head())
