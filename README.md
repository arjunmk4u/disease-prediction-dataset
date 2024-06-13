<h1>Disease and health condition dataset</h1>
This repository contains a program to create a dataset that contains the details of health conditions of different patients and their disease. The actual aim of this dataset is to predict which disease will affect you in future by analyzing the current health conditions like blood pressure, sugar level, cholesterol, etc. 
<br>

As of now the dataset is completely random and thus prediction may be incorrect. Additional dataset has to be added to this dataset or should use on the prediction model in order to get a good prediction score. Also  this dataset contains no valid data regarding medical information.
<br>

### Dataset features
The extended_disease_prediction_dataset.csv file contains the csv file created using the program
Key Variables:

-   **Patient ID:** Unique identifier for each patient.
-   **Age:** Age of the patient at the time of data collection.
-   **Sex:** Gender of the patient (M: Male, F: Female).
-   **BMI:** Body Mass Index.
-   **Blood Pressure (Sys/Dia):** Systolic and diastolic blood pressure readings.
-   **Cholesterol (Total/HDL/LDL):** Levels of total, HDL, and LDL cholesterol.
-   **Blood Sugar:** Fasting blood glucose levels.
-   **Family History:** History of specific diseases among immediate family members (0: No, 1: Yes).
-   **Smoking Status:** Current smoking status (Non-smoker, Ex-smoker, Smoker).
-   **Alcohol Consumption:** Frequency and quantity of alcohol consumption (None, Low, Moderate, High).
-   **Target Disease:** Binary indicator representing the presence (1) or absence (0) of the specific disease used for model training (this can be omitted if specific diseases are being targeted).
-   **Diabetes:** Binary indicator for diabetes (0: No, 1: Yes).
-   **Heart Disease:** Binary indicator for heart disease (0: No, 1: Yes).
-   **Lung Disease:** Binary indicator for lung disease (0: No, 1: Yes).
-   **Ulcer:** Binary indicator for ulcer (0: No, 1: Yes).
-   **Kidney Disease:** Binary indicator for kidney disease (0: No, 1: Yes).

dataset.py file contains the code for creating the desired dataset. Note that the datas are randomly prepared. <br>
You can created n number of entries by changing the value of n_samples variable.
