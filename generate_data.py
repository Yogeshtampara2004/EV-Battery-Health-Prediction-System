import pandas as pd
import numpy as np

np.random.seed(42)
n = 300

temperature = np.random.normal(35, 8, n).clip(15, 60)
voltage = np.random.normal(3.8, 0.15, n).clip(3.5, 4.2)
charge_cycles = np.random.randint(50, 800, n)

# Simulate health decreasing with temperature and cycles
health = 100 - (0.04 * charge_cycles) - (0.6 * (temperature - 25)) + np.random.normal(0, 2, n)
health = np.clip(health, 50, 100)

df = pd.DataFrame({
    "temperature": temperature,
    "voltage": voltage,
    "charge_cycles": charge_cycles,
    "battery_health": health
})

df.to_csv("battery_data.csv", index=False)
print("✅ battery_data.csv generated successfully!")
