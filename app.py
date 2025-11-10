import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EV Battery Health Prediction", page_icon="🔋", layout="wide")

st.title("🔋 EV Battery Health Prediction System")
st.write("Estimate remaining battery health based on sensor data using Machine Learning.")

model = joblib.load("battery_health_model.pkl")
data = pd.read_csv("battery_data.csv")

# Sidebar input
st.sidebar.header("Input Parameters")
temp = st.sidebar.slider("Temperature (°C)", 10, 60, 30)
volt = st.sidebar.slider("Voltage (V)", 3.5, 4.2, 3.8)
cycles = st.sidebar.slider("Charge Cycles", 0, 1000, 250)

# Prediction
input_df = pd.DataFrame([[temp, volt, cycles]], columns=["temperature", "voltage", "charge_cycles"])
prediction = model.predict(input_df)[0]

st.metric(label="Predicted Battery Health (%)", value=f"{prediction:.2f}")

# Visualization: Relationship between features and health
st.subheader("📈 Battery Data Insights")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x="temperature", y="battery_health", ax=ax, color="tomato")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x="charge_cycles", y="battery_health", ax=ax, color="royalblue")
    st.pyplot(fig)
