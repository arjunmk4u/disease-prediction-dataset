import pandas as pd
import numpy as np

# Define the number of samples
n_samples = 1000

# Generate synthetic data
np.random.seed(42)  # For reproducibility
patient_id = np.arange(1, n_samples + 1)
age = np.random.randint(18, 90, size=n_samples)
sex = np.random.choice(['M', 'F'], size=n_samples)
bmi = np.round(np.random.uniform(15, 40, size=n_samples), 1)
bp_sys = np.random.randint(90, 180, size=n_samples)
bp_dia = np.random.randint(60, 120, size=n_samples)
chol_total = np.random.randint(150, 300, size=n_samples)
chol_hdl = np.random.randint(30, 100, size=n_samples)
chol_ldl = chol_total - chol_hdl - np.random.randint(10, 50, size=n_samples)
blood_sugar = np.random.randint(70, 200, size=n_samples)
family_history = np.random.choice([0, 1], size=n_samples)  # 0: No, 1: Yes
smoking_status = np.random.choice(['Non-smoker', 'Ex-smoker', 'Smoker'], size=n_samples)
alcohol_consumption = np.random.choice(['None', 'Low', 'Moderate', 'High'], size=n_samples)
target_disease = np.random.choice([0, 1], size=n_samples)  # 0: No disease, 1: Disease

# Generate synthetic data for various diseases
diseases = {
    'Diabetes': np.random.choice([0, 1], size=n_samples),
    'Heart Disease': np.random.choice([0, 1], size=n_samples),
    'Lung Disease': np.random.choice([0, 1], size=n_samples),
    'Ulcer': np.random.choice([0, 1], size=n_samples),
    'Kidney Disease': np.random.choice([0, 1], size=n_samples)
}

# Create a DataFrame
data = pd.DataFrame({
    'Patient ID': patient_id,
    'Age': age,
    'Sex': sex,
    'BMI': bmi,
    'Blood Pressure (Sys)': bp_sys,
    'Blood Pressure (Dia)': bp_dia,
    'Cholesterol (Total)': chol_total,
    'Cholesterol (HDL)': chol_hdl,
    'Cholesterol (LDL)': chol_ldl,
    'Blood Sugar': blood_sugar,
    'Family History': family_history,
    'Smoking Status': smoking_status,
    'Alcohol Consumption': alcohol_consumption,
    'Target Disease': target_disease
})

# Add disease columns to the DataFrame
for disease, values in diseases.items():
    data[disease] = values

# Save the DataFrame to a CSV file
data.to_csv('extended_disease_prediction_dataset.csv', index=False)
