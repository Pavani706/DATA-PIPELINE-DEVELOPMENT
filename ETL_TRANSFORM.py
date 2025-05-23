import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Step 1: Extract
df = pd.read_csv("employee_data.csv")

# Step 2: Transform
# Fill missing values
df.fillna(method='ffill', inplace=True)

# Encode categorical columns
categorical_cols = ['first_name', 'last_name', 'job_title', 'department', 'email', 'address', 'phone_number', 'password']
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Scale numerical columns
numerical_cols = ['salary']
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Step 3: Load
df.to_csv("processed_employee_data.csv", index=False)
print("ETL process completed. Output saved as 'processed_employee_data.csv'")
