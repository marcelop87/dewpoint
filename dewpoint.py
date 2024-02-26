import streamlit as st
from joblib import load

st.title('Calculo Teorico Dew Point')
st.write('Esta app usa 2 valores de entrada para predecir el Dew Point')
st.image('newplot.png')

with st.form("user_inputs"):
    presion = st.number_input('Presion barg', min_value=65)
    temperatura = st.number_input('Temperatura °F', min_value=-22)
    
    
    loaded_model = load('dp_model.joblib')
    nueva_prediccion=loaded_model.predict([[temperatura, presion]])[0]
    
    
    submitted = st.form_submit_button("Submit")
    if submitted:
       st.write(f"Se predice que el Dew Point Calculado es de {nueva_prediccion:.2f}")
