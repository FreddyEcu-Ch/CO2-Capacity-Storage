# Import Python Libraries
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from funciones import bachu, bachuprob
from sqlalchemy import create_engine
import pandas as pd
#Insertar un icono
icon = Image.open("Resourse/logo.jpg")
#Desarrollo de la interfaz
st.set_page_config(page_title=" App Capacidad de almacenamiento Geológico", page_icon = icon)
st.title('Geological CO2 Storage App')
st.write("This application aims to calculate the geological storage capacity for oil reservoir using probabilistic methods and petrophysical input variables.")
with st.sidebar:
    options = option_menu("Main menu", options=["Home", "Reservoir data"], icons=["house", "gear"], menu_icon="cast")
    options
image = Image.open("Resourse/ccus.jpg")
st.image(image, width=100, use_column_width=True)
if options == "Home":
    st.markdown("""La ubicación de formaciones geológicas potencialmente efectivas para el almacenamiento geológico y la posterior evaluación de la capacidad regional de almacenamiento de CO2 en dichas formaciones son requisitos básicos para definir y predecir estrategias de entrada hacia la transición energética a nivel local, nacional o internacional. Sin duda, dicha evaluación será de gran interés para aquellos involucrados en actividades directamente relacionadas con el almacenamiento desde una perspectiva operativa especializada, y para los responsables del desarrollo de políticas y planes de acción, o quizás para las autoridades reguladoras.""")
    st.markdown("""Una de las tecnologias para reducir las emisiones es la captura, uso y almacenamiento de CO2 por su nombre en ingles CCUS, esta es una de las tecnologìas màs prometedoras para reducir el impacto de los gases de efecto invernadero sobre el planeta """)
    # OBJETIVO GENERAL
    st.header("""**Objetivo:** """)
    st.markdown("""Diseñar un aplicativo web que permita calcular el almacenamiento de CO2 en yacimientos de petróleo y gas, utilizando mètodos probabilìsticos y deterministicos""")

elif options == "Reservoir data":
    with st.sidebar:
        options = option_menu("Select Methodology", options=["Deterministic", "Probabilistic"], icons=["calculator", "calculator"])
    if options == "Deterministic":
        st.subheader("**Mètodo de Bachu determinìstico**")
        st.subheader("Ingrese los valores petrofìsicos de su reservorio:")
        densidad = st.number_input("Valor de densidad de CO2 en Kg/m3 :")
        Rf = st.number_input("Valor de Rf en tanto por 1 :")
        OOIP = st.number_input("Valor de OOIP en m3 :")
        Bo = st.number_input("Valor de densidad en By/Bn :")
        st.subheader("Capacidad de almacenamiento en Mt:")
        c = bachu(densidad, Rf, OOIP, Bo)
        st.success(c)
    elif options == "Probabilistic":
        st.subheader("**Seleccione el método:**")
        metodo = st.selectbox("Método", ("Bachu probabilístico","Zhong y Carr"))
        if metodo == "Bachu probabilístico":
            st.subheader("**Mètodo de Bachu probabilístico**")
            #upload_file = st.sidebar.file_uploader("Sube tu documento csv:")
            engine = create_engine("sqlite:///CO2/CO2_EOR1.db")
            df = pd.read_sql_query("SELECT * FROM Datos", engine)
            df
            st.caption("*Base de datos de propiedades petrofísicas*")
            st.subheader("**Cálculo capacidad de almacenamiento**")
            df2 = bachuprob()
        elif metodo == "Zhong y Carr":
            st.subheader("**Método de Zhong y Carr**")
            #upload_file = st.sidebar.file_uploader("Sube tu documento csv:")


