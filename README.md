# 🌱 Household Carbon Emission Prediction using Machine Learning

## 📌 Project Overview
This project predicts the **monthly household carbon emission (kg CO₂)** based on lifestyle and energy-related factors using **Machine Learning**.  
The goal of this project is to promote **environmental awareness and sustainable living** by helping households understand their carbon footprint.

A **Random Forest Regressor** model is trained and deployed using a **Streamlit web application** that provides real-time predictions based on user inputs.

---

## 🎯 Problem Statement
To develop a machine learning model that accurately predicts **monthly household carbon emissions** using the following parameters:
- Electricity consumption
- Renewable energy usage
- Water consumption
- Waste generation
- Recycling habits
- Usage of green appliances

---

## 📊 Dataset Description
- **Total Records:** 400  
- **Learning Type:** Supervised Learning (Regression)

### 🔢 Input Features
| Feature | Description |
|-------|------------|
| household_size | Number of people in the household |
| monthly_energy_kwh | Monthly electricity usage (kWh) |
| renewable_usage_pct | Percentage of renewable energy used |
| water_usage_liters | Monthly water consumption (liters) |
| waste_generated_kg | Monthly waste generated (kg) |
| recycling_pct | Recycling percentage |
| green_appliances | Number of energy-efficient appliances |

### 🎯 Target Variable
- **carbon_emission_kg** – Monthly carbon emission in kg CO₂

---

## 🤖 Machine Learning Algorithm Used
**Random Forest Regressor**

### ✔ Why Random Forest?
- Provides high prediction accuracy
- Handles non-linear relationships well
- Reduces overfitting
- Suitable for real-world environmental data

---

## 📈 Model Performance
- **Mean Absolute Error (MAE):** 4.07  
- **R² Score:** 0.98  

This indicates that the model predicts household carbon emissions with **very high accuracy**.

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 🖥️ Web Application
A **Streamlit-based web application** allows users to:
1. Enter household and energy usage details
2. Click on **Predict Carbon Emission**
3. Instantly view predicted monthly carbon emissions

---

## 🚀 How to Run the Project Locally

### Step 1: Install Required Libraries
```bash
pip install pandas scikit-learn streamlit joblib numpy
```
### Step 2: Train the Model
```bash
python train_model.py
```
### Step 3: Run the Streamlit App
```bash
python -m streamlit run app.py
```
