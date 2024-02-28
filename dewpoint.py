import streamlit as st
import pandas as pd
import plotly.express as px
from joblib import load

loaded_model = load('dp_model.joblib')

container = st.container()

@st.cache_data
def load_data(file):
    df = pd.read_excel(file, header=1)
    df['DP Teorico'] = loaded_model.predict(df[['T Sep Frio', 'P Sep Frio']].values)
    return df

def create_chart(data):
  
    st.header("Line Chart")
    fig = px.line(data, x="HORA", y=['DP CPF °F', 'DP Teorico'], title="Comparación Dew Point Medido vs Teórico",  width=1100, height=600).update_xaxes(dtick=3600000, tickformat="%H")
    fig.update_layout(legend_title=None ,legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01),
        title_font=dict(color="grey",size=30),title={"x": .5, "y": .9,"xanchor": "center"}, legend_traceorder="reversed")
    fig.update_yaxes(title='DewPoint')
    st.plotly_chart(fig)

def main():
   
    file = st.sidebar.file_uploader("Upload a data set in CSV or EXCEL format", type=["csv","xlsx"])
    options = st.sidebar.radio('Pages', options = ['Calculo Dew Point', 'Comparacion DewPoint Teorico vs Medido' ])
    if options =='Calculo Dew Point':
        st.image('newplot.png')
        container.write(" # Calculo de Dew Point # ")
        st.write('Esta app usa 2 valores de entrada para predecir el Dew Point')
        with st.form("user_inputs"):
            presion = st.number_input('Presion barg', min_value=65.0)
            temperatura = st.number_input('Temperatura °F', min_value=-22.0) 
                
            submitted = st.form_submit_button("Submit")
            
            if submitted:
               nueva_prediccion=loaded_model.predict([[temperatura, presion]])[0]
               st.write(f"Se predice que el Dew Point Calculado es de {nueva_prediccion:.2f}")
    
    if options == 'Comparacion DewPoint Teorico vs Medido':
        container.write(" # Comparacion Dew Point Calculado vs Dew Point Teorico # ")
        if file is not None:
            data = load_data(file)
            create_chart(data)
        
                    
if __name__=="__main__":
    main()
