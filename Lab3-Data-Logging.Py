# =========================================================
# NAME: KEVIN KIPKOECH KEMBOI
# REG NO: ENG-219-044/2025
# UNIT: FUNDAMENTALS OF COMPUTERS (CIT 2118)
# LAB: Lab 3 - Data Logging and Plotting
# =========================================================

import random
import time
import matplotlib.pyplot as plt

# Lists to store data for plotting
temps = []
humidity = []
timestamps = []

print("Starting Data Logging Simulation...")

try:
    # Task: Loop to log 10 data points
    for t in range(10):
        # Simulating data with random variations
        temp = 25 + random.uniform(-1, 1)
        hum = 50 + random.uniform(-5, 5)
        
        temps.append(temp)
        humidity.append(hum)
        timestamps.append(t)
        
        # Task: Use different file formats (CSV and TXT)
        # Logging to CSV
        with open("sensor_data.csv", "a") as csv_file:
            csv_file.write(f"{t},{temp:.2f},{hum:.2f}\n")
            
        # Logging to TXT
        with open("sensor_log.txt", "a") as txt_file:
            txt_file.write(f"Time: {t}s | Temp: {temp:.2f}C | Humidity: {hum:.2f}%\n")
            
        print(f"Logged: Time {t}s - Temp {temp:.2f}C, Hum {hum:.2f}%")
        
        # Interval between logs
        time.sleep(0.5)

# Task: Add error handling for file operations
except IOError as e:
    print(f"File System Error: Could not write to file. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Task: Plot the data
plt.figure(figsize=(10, 5))
plt.plot(timestamps, temps, label="Temperature (C)", marker='o', color='tab:red')
plt.plot(timestamps, humidity, label="Humidity (%)", marker='s', color='tab:blue')

plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.title("Environmental Data Log (Temp & Humidity)")
plt.legend()
plt.grid(True)
plt.show()