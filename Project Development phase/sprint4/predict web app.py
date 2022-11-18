# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 23:22:17 2022

@author: user
"""


import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('heart_disease_model.sav', 'rb'))
def heart_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] !=0):
      return 'The person is  Heart Disease'
    if (prediction[0] ==0):
      return 'The person is not Heart Disease'
  
def main():
    
    
    # giving a title
    st.title('Heart Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Age = st.text_input('Enter the Age')
    Sex = st.text_input('Sex')
    Chest_pain_type = st.text_input('Chest pain type')
    BP	 = st.text_input('BP')
    Cholesterol = st.text_input('Cholesterol')
    FBS_over_120 = st.text_input('FBS over 120')
    EKG_results = st.text_input('EKG results')
    Max_HR = st.text_input('Max HR')
    Exercise_angina = st.text_input('Exercise angina')
    ST_depression = st.text_input('ST depression')
    Slope_of_ST = st.text_input('Slope of ST')
    Number_of_vessels_fluro	 = st.text_input('Number of vessels fluro')
    Thallium = st.text_input('Thallium')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_prediction([[Age, Sex, Chest_pain_type, BP, Cholesterol, FBS_over_120 , EKG_results , Max_HR,Exercise_angina,ST_depression,Slope_of_ST, Number_of_vessels_fluro,Thallium]	 ])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
  
    
  