import streamlit as st
def executar_tarefa():

    st.set_page_config(
            page_title="CAMARGO",
            page_icon="",
            layout='wide'
                            )
    logo = 'x_99_logo_camargo.png'  # Substitua pelo caminho da sua imagem
    st.image(logo)
    st.markdown(
        """
        ### PRODUÇÃO ULTIMOS 30 DIAS 
        """
                    )
    resultado_dia = 'x_01_Produção de Acordos.png'  # Substitua pelo caminho da sua imagem
    st.image(resultado_dia)  

executar_tarefa()