# 🔋 EV Battery Health Prediction System

A machine learning-based Streamlit web app that predicts the **remaining health of an Electric Vehicle (EV) battery** based on real-time sensor data such as temperature, voltage, and charge cycles.

---

## 📊 Overview
This project simulates an **EV battery monitoring system** where IoT sensors send temperature, voltage, and charge cycle data.  
The system predicts **battery health percentage** using a regression model and visualizes feature relationships through interactive charts.

---

## 🧠 Features
- Predict battery health using trained ML regression model  
- Interactive Streamlit dashboard with live prediction sliders  
- Real-time data visualizations using Seaborn and Matplotlib  
- Automatically generated synthetic dataset for experimentation  

---

## 🧩 Tech Stack
- **Python 3.9+**
- **Libraries:** Pandas, NumPy, Scikit-learn, Streamlit, Seaborn, Matplotlib, Joblib
- **Model:** Random Forest Regressor
- **Frontend:** Streamlit web interface

---


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/ev-battery-health.git
cd ev-battery-health
pip install -r requirements.txt
python generate_data.py
python model.py
streamlit run app.py
```


## 📁 Folder Structure
