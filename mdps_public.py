# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

logic_watering_model = pickle.load(open('logic_watering_model.sav', 'rb'))

logic_aeration_model = pickle.load(open('logic_aeration_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('GreenHouse Predictive Model',
                          
                          ['Watering Prediction',
                           'Aeration Prediction',],
                          icons=['water','sun','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Watering Prediction'):
    
    # page title
    st.title('Watering Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)

    with col1:
        Temperature = st.text_input('Temperature')

    with col2:
        Humidity = st.text_input('Humidity')

    with col1:
        Moisture = st.text_input('Moisture')

    with col2:
        Watering = st.text_input('Watering')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Watering Test Result'):
        diab_prediction = logic_watering_model.predict([[Temperature, Humidity, Moisture, Watering]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Aeration Needed'
        else:
          diab_diagnosis = 'Aeration not needed'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Aeration Prediction'):
    
    # page title
    st.title('Aeration Prediction using ML')
    
    col1, col2 = st.columns(2)

    with col1:
        Temperature = st.text_input('Temperature')

    with col2:
        Humidity = st.text_input('Humidity')

    with col1:
        Moisture = st.text_input('Moisture')

    with col2:
        Aeration = st.text_input('Aeration')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Aeration Test Result'):
        heart_prediction = logic_aeration_model.predict([[Temperature, Humidity, Moisture, Aeration]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'Aeration Needed'
        else:
          heart_diagnosis = 'No Aeration'
        
    st.success(heart_diagnosis)
