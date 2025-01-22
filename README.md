# Near-Earth Object (NEO) Risk Assessment Pipeline

This project is an ETL (Extract, Transform, Load) pipeline for assessing the risk of potentially hazardous Near-Earth Objects (NEOs) using NASA's NEO API. It calculates a "risk score" for asteroids based on their size, speed, and distance from Earth, helping identify which objects pose the greatest threat.

---

## **Features**
- Fetches Near-Earth Object data from NASA's public API.
- Calculates a risk score for hazardous asteroids using a custom formula.
- Logs the pipeline's status and results for tracking and debugging.
- Supports configuration via environment variables for secure API key management.

---

## **Technologies Used**
- **Python**: Core programming language for the pipeline.
- **Requests**: For fetching data from the NASA API.
- **Logging**: For tracking pipeline execution and errors.

---

## **Folder Structure**



project/
├── src/
│   ├── config.py           # Configuration file for constants and API keys
│   ├── extract.py          # Extracts data from the NASA API
│   ├── transform.py        # Transforms and processes the NEO data
│   ├── utils.py            # Utility functions for logging and error handling
│   ├── main.py             # Main entry point for the ETL pipeline
├── logs/
│   └── app.log             # Logs of pipeline execution
├── .env                    # Environment variables (e.g., NASA_API_KEY)
├── requirements.txt        # List of dependencies
└── README.md               # Documentation



Risk Score Calculation
The risk score for each hazardous asteroid is calculated as:

Risk Score
=
Size (km)
×
Speed (km/h)
Distance (km)
Risk Score= 
Distance (km)
Size (km)×Speed (km/h)
​
 
Where:

Size (km): Maximum estimated diameter of the asteroid.
Speed (km/h): Relative velocity of the asteroid.
Distance (km): Closest approach distance from Earth.


Logging
All logs are stored in the logs/app.log file.
Logs include information about data fetch success, errors, and calculated results.
Sample Output
The pipeline identifies hazardous asteroids and logs their details:


2025-01-22 14:30:00 - INFO - Starting ETL pipeline from 2025-01-15 to 2025-01-22
2025-01-22 14:30:01 - INFO - Successfully fetched data for 2025-01-15 to 2025-01-22
2025-01-22 14:30:02 - INFO - Identified 3 hazardous asteroids.
2025-01-22 14:30:02 - INFO - Asteroid: 1997 XF11 | Risk Score: 45.67
2025-01-22 14:30:02 - INFO - Asteroid: Apophis | Risk Score: 30.12
2025-01-22 14:30:02 - INFO - Asteroid: Bennu | Risk Score: 20.87



