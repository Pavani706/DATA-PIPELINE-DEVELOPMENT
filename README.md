# DATA-PIPELINE-DEVELOPMENT

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline built with Python using basic libraries such as pandas and scikit-learn. The pipeline processes employee data by extracting from a CSV, performing basic cleaning and transformations, and saving the cleaned data for downstream usage.

📁 Project Structure
etl-pipeline/ │ ├── employee_data.csv # Raw input data ├── processed_employee_data.csv # Output after ETL ├── extract.py # Script to generate or extract employee data ├── ETL_TRANSFORM.py # ETL script (transform and load) └── README.md # Project documentation

✅ Features
Extracts data from a CSV file.
Handles missing values using forward fill.
Encodes categorical columns using label encoding.
Scales numerical values like salary.
Outputs the cleaned data to a new CSV file.
🛠️ Requirements
Python 3.x
pandas
scikit-learn
You can install dependencies with:

pip install pandas scikit-learn
python extract.py
python ETL_TRANSFORM.py
processed_employee_data.csv
