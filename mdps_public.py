import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('mode_aeration_saved', 'rb'))

heart_disease_model = pickle.load(open('mode_watering_saved', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Temperature = st.text_input('Temperature')

    with col2:
        Humidity = st.text_input('Humidity')

    with col3:
        Moisture = st.text_input('Moisture')

    with col1:
        Watering = st.text_input('Watering')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Temperature, Humidity, Moisture, Watering]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
