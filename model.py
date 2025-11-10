import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib

df = pd.read_csv("battery_data.csv")

X = df[['temperature', 'voltage', 'charge_cycles']]
y = df['battery_health']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=120, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Model Accuracy (R²):", r2_score(y_test, y_pred))

joblib.dump(model, "battery_health_model.pkl")
print("✅ Model saved as battery_health_model.pkl")
