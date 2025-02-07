# CS506_Final_Project_Proposal

# 🚗 Uber & Lyft Ride Price Prediction - Boston, MA  

## 📌 Project Description  
Ride-sharing services like **Uber and Lyft** have become integral to urban transportation. This project aims to analyze ride-sharing data from **Boston, MA** to identify key factors influencing ride prices and demand.  

Using a dataset containing ride details such as **time, location, temperature, and service type**, we will develop a **predictive model** that estimates ride fares based on these features. Additionally, this project seeks to uncover insights into pricing strategies and demand patterns, providing a deeper understanding of how external variables impact ride-sharing services.  

---

## 🎯 Goals  

### 🔹 Primary Goal  
- Successfully **predict ride prices** for Uber and Lyft in Boston based on **time of day, location, distance, temperature, and service type**.  

### 🔹 Secondary Goals  
- Identify patterns in **pricing strategies and demand fluctuations**.  
- Provide valuable insights for **users and ride-sharing companies** to optimize pricing and travel decisions.  

---

## 📊 Data Collection  

### 📌 Dataset Source  
- **Uber and Lyft Dataset - Boston, MA** ([Kaggle](https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma))  

### 📌 Dataset Overview  
This dataset contains **6.9 million rows** of ride-sharing data collected from Uber and Lyft in **Boston, MA**, with **57 features** capturing key aspects of ride pricing, demand, and external influences:  

- **📅 Temporal Patterns:** `timestamp`, `datetime`, `timezone` (effect of time on ride demand and pricing)  
- **📍 Location-Based Demand:** `source`, `destination` (popular pickup/drop-off locations)  
- **💰 Pricing & Surge Effects:** `price`, `distance`, `surge_multiplier` (fare variations and surge pricing)  
- **🚖 Ride Type Comparison:** `cab_type` (Uber vs. Lyft fare and demand comparison)  
- **🌦 Weather Influence:** `windSpeed`, `temperature` (impact of weather on pricing and ride frequency)  
- **📌 Additional Attributes:** Various ride-specific details.  

---

## ⚙️ Modeling Approach  

1️⃣ **Separate Uber & Lyft Data** → Analyze pricing structures independently.  
2️⃣ **Conduct Exploratory Data Analysis (EDA)** → Identify trends, correlations, and outliers.  
3️⃣ **Feature Engineering** → Extract meaningful features for improved prediction accuracy.  
4️⃣ **Train & Evaluate Multiple Models** → Compare different machine learning models:  

### 🚀 Models to be Tested  
- **Random Forest** 🌲  
- **XGBoost** ⚡  
- **Neural Networks (NN)** 🤖  
- **Logistic Regression** 📊  
- **k-Nearest Neighbors (KNN)** 🔍  

Each model will be evaluated using **train accuracy and test accuracy** to ensure a balance between **underfitting and overfitting**.  

---

## 📈 Data Visualization Plan  

### 🔹 **Exploratory Data Analysis (EDA)**  
📌 **Heatmaps:** Identify popular pickup/drop-off locations.  
📌 **Time-Series Analysis:** Observe fare variations across different times and days.  
📌 **Bar Charts:** Compare **average prices between Uber and Lyft**.  

### 🔹 **Model Evaluation**  
📌 **Feature Importance Plot:** Identify key variables affecting ride pricing.  
📌 **Actual vs. Predicted Plot:** Measure model performance.  

---

## ✅ Test Plan  

To ensure **robust evaluation** and prevent overfitting, we will implement the following testing strategies:  

### 📌 **Train-Test Split**  
- The dataset will be split into **80% training data** and **20% testing data** to evaluate model performance on unseen data.  

### 📌 **Cross-Validation**  
- **k-fold cross-validation (e.g., k=5)** will be used to assess model consistency and avoid dependency on a single train-test split.  

### 📌 **Performance Metrics**  
- **Train Accuracy & Test Accuracy** → Measure model fit and generalization ability.  
- **Mean Absolute Error (MAE) & Root Mean Square Error (RMSE)** → Evaluate regression models' prediction errors.  
- **F1-score, Precision, Recall** → Assess classification performance (if applicable).  

### 📌 **Hyperparameter Tuning**  
- Optimize model performance using **Grid Search** or **Random Search**.  

### 📌 **Uber vs. Lyft Comparison**  
- After selecting the **best model**, we will analyze Uber and Lyft pricing strategies separately.  

By following this **test plan**, we aim to ensure our final model is both **accurate and generalizable** for predicting ride prices and demand patterns. 🚀  

---

## 📢 Contributors  
🚀 **Joshua Nahm** - [GitHub Profile](https://github.com/JoshuaNahm)  
🚀 **Seokhoon Shin** - [GitHub Profile](https://github.com/seokhoonshin)  

---


