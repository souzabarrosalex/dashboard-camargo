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
        ### META BANCO GERAL LEVES
        """
                    )
    resultado_dia = 'x_10_meta_banco_geral_leves.png'  # Substitua pelo caminho da sua imagem
    st.image(resultado_dia)  

executar_tarefa()