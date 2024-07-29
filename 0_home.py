import streamlit as st
import time
def executar_tarefa():

    st.set_page_config(
            page_title="CAMARGO",
            page_icon="",
            layout='wide'
                            )
    logo = 'logo_camargo.png'  # Substitua pelo caminho da sua imagem
    st.image(logo)
    st.markdown(
        """
        ### PRODUÇÃO DO DIA E MES ANTERIOR  
        """
                    )
    resultado_dia = '0_producao_dia_e_mes_anterior.png'  # Substitua pelo caminho da sua imagem
    st.image(resultado_dia)  

executar_tarefa()
