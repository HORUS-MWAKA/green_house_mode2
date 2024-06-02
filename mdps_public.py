import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

#diabetes_model = pickle.load(open('mode_aeration_saved', 'rb'))

#heart_disease_model = pickle.load(open('mode_watering_saved', 'rb'))

#parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))




    
    # page title
st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
col1, col2 = st.columns(3)

with col1:
    Temperature = st.text_input('Temperature')

with col2:
    Humidity = st.text_input('Humidity')

with col1:
    Moisture = st.text_input('Moisture')

with col2:
    Watering = st.text_input('Watering')
    
    

