
# MULTIMEDIA UNIVERSITY OF KENYA
## FACULTY OF ENGINEERING AND TECHNOLOGY

**UNIT:** Fundamentals of Computers (CIT 2118)  
**LAB:** Lab 3 - Data Logging and Plotting  
**STUDENT:** KEVIN KIPKOECH KEMBOI  
**REG NO:** ENG-219-044/2025  
**LECTURER:** LEC MARTIN  
**DATE:** 30th January 2026

---

## 1. Overview

The goal of this program is to log simulated environmental data (Temperature and Humidity) to external files and visualize the trends using Matplotlib.

## 2. Lab Tasks Completed

- Logged both Temperature and Humidity values
- Implemented dual-format logging:
    - `sensor_data.csv` (For spreadsheet analysis)
    - `sensor_log.txt` (For human-readable logging)
- Added Error Handling (Try-Except) to manage file operation failures
- Generated a multi-variable plot showing both metrics over time

## 3. How to Run

1. Ensure 'matplotlib' is installed: `pip install matplotlib`
2. Run the script: `python Lab3_Data_Logging.py`
3. Check the local directory for `sensor_data.csv` and `sensor_log.txt` to see the recorded data

## 4. Reflection

- Data logging is critical for monitoring long-term system stability and performance in engineering
- Visualizations convert raw numeric logs into actionable insights, allowing for rapid detection of anomalies
