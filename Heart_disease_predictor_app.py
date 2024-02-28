import streamlit as st
import pickle
import numpy as np
import pandas as pd

pickle_in = open(r"C:\Users\welcome\Desktop\Projects\AIML_Projects\Heart_Disease\heart.pkl", "rb")
Classifier = pickle.load(pickle_in)

def predict_note_authentication(input_data):
    input_as_float = [float(x) for x in input_data]  # Convert input strings to floats
    input_reshaped = np.array(input_as_float).reshape(1, -1)
    pred = Classifier.predict(input_reshaped)

    if pred[0] == 0:
        result = 'The Patient has no heart Disease'
    else:
        result = 'The Patient has heart Disease'
    return result

def main():
    st.title("Heart Disease Predictor App")
    
    st.markdown("""
    ##     
    - **Age:** displays the age of the individual.
    - **Sex:** displays the gender of the individual using the following format:  
      1 = male  
      0 = female  
    - **Chest-pain type:** displays the type of chest-pain experienced by the individual using the following format:  
      0 = typical angina  
      1 = atypical angina  
      2 = non — anginal pain  
      3 = asymptomatic  
    - **Resting Blood Pressure:** displays the resting blood pressure value of an individual in mmHg (unit)
    - **Serum Cholesterol:** displays the serum cholesterol in mg/dl (unit)
    - **Fasting Blood Sugar:** compares the fasting blood sugar value of an individual with 120mg/dl. If fasting blood sugar > 120mg/dl then: 1 (true) else: 0 (false)
    - **Resting ECG:** displays resting electrocardiographic results  
      0 = normal  
      1 = having ST-T wave abnormality  
      2 = left ventricular hypertrophy  
    - **Max heart rate achieved:** displays the max heart rate achieved by an individual.
    - **Exercise induced angina:**  
      1 = yes  
      0 = no  
    - **ST depression induced by exercise relative to rest:** displays the value which is an integer or float.
    - **Peak exercise ST segment:**  
      1 = upsloping  
      2 = flat  
      3 = downsloping  
    - **Number of major vessels (0–3) colored by fluoroscopy:** displays the value as an integer or float.
    - **Thal:** displays the thalassemia:  
      0 = normal  
      1 = fixed defect  
      2 = reversible defect  
    
    - **Diagnosis of heart disease:** Displays whether the individual is suffering from heart disease or not:  
      0 = absence  
      1, 2, 3, 4 = present.
    """)
    
    age = st.text_input("AGE")
    st.text("(Age: 1 - 150)")

    sex = st.text_input("SEX")
    st.text("(Male: 1 & Female: 0)")

    cp = st.text_input("CP")
    st.text("(Enter Single Value From Range 0-3)")
    
    trestbps = st.text_input("TRESTBPS")
    st.text("(Enter Non-Decimal Value)")
    
    chol = st.text_input("CHOL")
    st.text("(Enter Non-Decimal Value)")

    fbs = st.text_input("FBS")
    st.text("(1 = True; 0 = False)")

    restecg = st.text_input("RESTECG")
    st.text("(Enter Single Value From Range 0-2)")

    thalach = st.text_input("THALACH")
    st.text("(Enter Non-Decimal Value)")

    exang = st.text_input("EXANG")
    st.text("(Exercise: 1 = YES; 0 = NO)")

    oldpeak = st.text_input("OLDPEAK")
    st.text("(Enter Decimal Value)")

    slope = st.text_input("SLOPE")
    st.text("(Enter Single Value From Range 0-2)")

    ca = st.text_input("CASE")
    st.text("(Enter Single Value From Range 0-4)")

    thal = st.text_input("THAL")
    st.text("(Enter Single Value From Range 0-3)")

    result=""
    if st.button("Predict"):
        result = predict_note_authentication([age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, oldpeak, slope, ca, thal])
    st.success(result)

if __name__=='__main__':
    main()
