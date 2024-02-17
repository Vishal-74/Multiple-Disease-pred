import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open('trained_model.sav', 'rb'))
heart_disease_model = pickle.load(open('trained_model(1).sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity', 'heart'],
                          default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)  
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')       
        SkinThickness = st.text_input('Skin Thickness value')   
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')   
    with col2:
        Glucose = st.text_input('Glucose Level')    
        Insulin = st.text_input('Insulin Level')   
        BMI = st.text_input('BMI value')    
        Age = st.text_input('Age of the Person')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')   
    
    # Code for Prediction
    diab_diagnosis = ''
   
    if st.button('Diabetes Test Result'):
        try:
            # Convert input to numeric values
            Pregnancies = float(Pregnancies)
            Glucose = float(Glucose)
            BloodPressure = float(BloodPressure)
            SkinThickness = float(SkinThickness)
            Insulin = float(Insulin)
            BMI = float(BMI)
            DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
            Age = float(Age)
            
            # Make prediction
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        except ValueError:
            diab_diagnosis = 'Please fill in all the input fields with valid numeric values.'
        
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)   
    with col1:
        age = st.text_input('Age')       
        cp = st.text_input('Chest Pain types')       
        restecg = st.text_input('Resting Electrocardiographic results')       
        oldpeak = st.text_input('ST depression induced by exercise')        
        ca = st.text_input('Major vessels colored by flourosopy')
    with col2:
        sex = st.text_input('Sex')       
        trestbps = st.text_input('Resting Blood Pressure')        
        chol = st.text_input('Serum Cholestoral in mg/dl')       
        thalach = st.text_input('Maximum Heart Rate achieved')       
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')       
        exang = st.text_input('Exercise Induced Angina')       
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
   
    heart_diagnosis = ''
       
    if st.button('Heart Disease Test Result'):
        try:
            # Convert input to numeric values
            age = float(age)
            sex = float(sex)
            cp = float(cp)
            trestbps = float(trestbps)
            chol = float(chol)
            fbs = float(fbs)
            restecg = float(restecg)
            thalach = float(thalach)
            exang = float(exang)
            oldpeak = float(oldpeak)
            slope = float(slope)
            ca = float(ca)
            thal = float(thal)
            
            # Make prediction
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except ValueError:
            heart_diagnosis = 'Please fill in all the input fields with valid numeric values.'
        
        st.success(heart_diagnosis)
