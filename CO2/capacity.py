#Import Python Libraries
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from funciones import bachu, bachuprob, zhoca
import pandas as pd
import plotly.express as px
# Insertar un icono
icon = Image.open("Resourse/logo.jpg")
# Desarrollo de la interfaz
st.set_page_config(
    page_title=" App Capacidad de almacenamiento Geológico", page_icon=icon
)
st.title("Geological CO2 Storage App")
st.write(
    "This application aims to calculate the geological storage capacity for oil reservoir using probabilistic methods"
    " and petrophysical input variables."
)
with st.sidebar:
    options = option_menu(
        "Main menu",
        options=["Home", "Reservoir data"],
        icons=["house", "gear"],
        menu_icon="cast",
    )
    options
image = Image.open("Resourse/ccus.jpg")
st.image(image, width=100, use_column_width=True)
st.caption("Proceso del proyecto Captura,uso y almacenamiento de CO2")
if options == "Home":
    st.markdown(
        """La ubicación de formaciones geológicas potencialmente efectivas para el almacenamiento geológico y la
         posterior evaluación de la capacidad regional de almacenamiento de CO2 en dichas formaciones son requisitos
          básicos para definir y predecir estrategias de entrada hacia la transición energética a nivel local, nacional
           o internacional. Sin duda, dicha evaluación será de gran interés para aquellos involucrados en actividades
            directamente relacionadas con el almacenamiento desde una perspectiva operativa especializada, y para los
             responsables del desarrollo de políticas y planes de acción, o quizás para las autoridades reguladoras."""
    )
    st.markdown(
        """Una de las tecnologías para reducir las emisiones es la captura, uso y almacenamiento de CO2 por su nombre
         en ingles CCUS, esta es una de las tecnologías màs prometedoras para reducir el impacto de los gases de efecto
          invernadero sobre el planeta """
    )
    st.markdown("El CCUS se maneja tomando el CO2 de fuentes estacionarias para luego procesarlo e inyectarlo en el subsuelo, así se obtiene el almacenamiento geológico, sin embargo, se le puede sacar beneficios extras como esel caso de la recuperación mejorada en yacimientos de petróleo.")
    video = open("Resourse/videoccus.mp4", "rb")
    st.video(video)
    st.caption("""Coalition, C.N. (2023) Texas must act to broadly deploy carbon capture, utilization, and storage (CCUS) as we face the growing global challenges demanding low carbon or carbon free products. visit our website to learn more: Https://t.co/wm9ikonp2k pic.twitter.com/bzgncqcytn, Twitter. Twitter. Available at: https://twitter.com/i/status/1610758082937688088 (Accessed: January 6, 2023). """
               )
    # OBJETIVO GENERAL
    st.header("""**Objetivo:** """)
    st.markdown(
        """Diseñar un aplicativo web que permita calcular el almacenamiento de CO2 en yacimientos de petróleo y gas,
         utilizando métodos probabilísticos y determinísticos"""
    )

elif options == "Reservoir data":
    with st.sidebar:
        options = option_menu(
            "Select Methodology",
            options=["Deterministic", "Probabilistic"],
            icons=["calculator", "calculator"],
        )
    if options == "Deterministic":
        st.subheader("**Método de Bachu determinístico**")
        st.subheader("Ingrese los valores petrofísicos de su reservorio:")
        densidad = st.number_input("Valor de densidad de CO2 en Kg/m3 :")
        Rf = st.number_input("Valor de Rf en tanto por 1 :")
        OOIP = st.number_input("Valor de OOIP en m3 :")
        Bo = st.number_input("Valor de factor volumetrico de formación del petróleo en By/Bn :")
        st.subheader("Capacidad de almacenamiento en Mt:")
        c = bachu(densidad, Rf, OOIP, Bo)
        st.success(c)
    elif options == "Probabilistic":
        st.subheader("**Seleccione el método:**")
        metodo = st.selectbox("Método", ("Bachu probabilístico", "Zhong y Carr"))
        if metodo == "Bachu probabilístico":
            st.subheader("**Método de Bachu probabilístico**")
            upload_file = st.file_uploader("Sube tu documento csv:")
            df = pd.read_csv(upload_file)
            st.subheader("**Los datos ingresados son:**")
            st.dataframe(df)
            bachuprob(df)
            st.subheader("**Resultado de Capacidad de Almacenamiento Geològico**")
            st.dataframe(df)
            fig_refi = px.bar(df, x='formacion', y='capacidad', color='formacion', range_y=[0, 1.2])
            fig_refi.update_xaxes(title='Formaciones Evaluadas', visible=True)
            fig_refi.update_yaxes(autorange=True, title='Capacidad de almacenamiento de CO2',
                                  visible=True, showticklabels=True)
            fig_refi.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                                   xaxis=dict(tickmode='linear', dtick=1))
            fig_refi.update_traces(textfont_size=16, textangle=0)
            st.plotly_chart(fig_refi)
        elif metodo == "Zhong y Carr":
            st.subheader("**Método de Zhong y Carr**")
            upload_file = st.file_uploader("Sube tu documento csv:")
            df = pd.read_csv(upload_file)
            st.subheader("**Los datos ingresados son:**")
            st.dataframe(df)
            zhoca(df)
            st.subheader("**Resultado de Capacidad de Almacenamiento Geològico**")
            st.dataframe(df)
            fig_refi = px.bar(df, x='formacion', y='Capacidad', color='formacion', range_y=[0, 1.2])
            fig_refi.update_xaxes(title='Formaciones Evaluadas', visible=True)
            fig_refi.update_yaxes(autorange=True, title='Capacidad de almacenamiento de CO2',
                                  visible=True, showticklabels=True)
            fig_refi.update_layout(template="plotly_dark", width=800, height=600, showlegend=True,
                                   xaxis=dict(tickmode='linear', dtick=1))
            fig_refi.update_traces(textfont_size=16, textangle=0)
            st.plotly_chart(fig_refi)