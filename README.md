# Engineering Test Data Analyzer

## Overview
The Engineering Test Data Analyzer is a Python-based project that reads and analyzes engineering-style sensor data from a CSV file. The program processes raw machine and robotic-system test data, detects abnormal sensor readings, and generates a summary report of system performance.

This project was created to practice working with engineering and robotics-related data systems, including concepts used in manufacturing automation, machine monitoring, and robotic diagnostics.

---

## Features
- Reads sensor data from a CSV file
- Processes:
  - Temperature
  - Pressure
  - Vibration
  - Joint angle
  - Motor speed
- Detects abnormal sensor values
- Calculates:
  - Average values
  - Maximum values
  - Minimum values
- Prints a formatted engineering test report

---

## Technologies Used
- Python
- CSV file handling
- Lists and loops
- Conditional logic
- Statistical calculations

---

## Example CSV Data

```csv
time,temp,pressure,vibration,joint_angle,motor_speed
0,120,40,2.0,10,100
1,122,42,2.1,20,105
2,121,41,2.0,30,110
3,180,70,5.5,45,130
4,123,42,2.2,60,120
5,400,90,15.0,120,250