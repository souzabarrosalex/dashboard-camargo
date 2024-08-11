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
        ### RANK 16 A 30 
        """
                    )
    resultado_dia = 'x_03_Rank 16 a 30.png'  # Substitua pelo caminho da sua imagem
    st.image(resultado_dia)  

executar_tarefa()