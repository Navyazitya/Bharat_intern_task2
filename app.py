import streamlit as st
import pickle
import numpy as np

# Load the saved logistic regression model
file_path = "C:\\Users\\DELL\\Desktop\\bharath_intern\\heart disease prediction\\gs_logistic_reg_heart_disease_model.pkl"
try:
    # Attempt to load the model from the pickle file
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully.")
except FileNotFoundError:
    print(f"File not found at: {file_path}")
except pickle.UnpicklingError:
    print("There was an error unpickling the file. The file may be corrupted or incompatible.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


def predict_heart_disease(features):
    # Convert features to a 2D array
    features = np.array(features).reshape(1, -1)
    try:
        prediction = model.predict(features)
        return prediction[0]  # Return the prediction (0 or 1)
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        return None


# Streamlit app
st.title("Heart Disease Prediction App")

# Create input fields for the user to enter their data
age = st.number_input("Age", min_value=1, max_value=120, value=25)
sex = st.selectbox("Sex", options=["Male", "Female"])
cp = st.selectbox("Chest Pain Type", options=["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0)
chol = st.number_input("Cholesterol Level (mg/dl)", min_value=0)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=["Yes", "No"])
restecg = st.selectbox("Resting ECG Results", options=["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"])
thalach = st.number_input("Max Heart Rate Achieved", min_value=0)
exang = st.selectbox("Exercise Induced Angina", options=["Yes", "No"])
oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, step=0.1)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=["Upsloping", "Flat", "Downsloping"])
ca = st.number_input("Number of Major Vessels (0-3) colored by Flourosopy", min_value=0, max_value=3, step=1)
thal = st.selectbox("Thalassemia", options=["Normal", "Fixed Defect", "Reversible Defect"])

# Map the user input to numerical values (convert categorical inputs to numerical values)
sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "Yes" else 0
exang = 1 if exang == "Yes" else 0

cp_dict = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}
cp_num = cp_dict[cp]

restecg_dict = {"Normal": 0, "Having ST-T wave abnormality": 1, "Showing probable or definite left ventricular hypertrophy": 2}
restecg_num = restecg_dict[restecg]

slope_dict = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
slope_num = slope_dict[slope]

thal_dict = {"Normal": 1, "Fixed Defect": 2, "Reversible Defect": 3}
thal_num = thal_dict[thal]

# Gather all features
features = [age, sex, cp_num, trestbps, chol, fbs, restecg_num, thalach, exang, oldpeak, slope_num, ca, thal_num]

# Create a button to make predictions
if st.button("Predict"):
    prediction = predict_heart_disease(features)
    if prediction == 1:
        st.warning("According to the model, you may have heart disease. Please consult a doctor for a proper diagnosis.")
    else:
        st.success("According to the model, you do not appear to have heart disease. Please maintain a healthy life")