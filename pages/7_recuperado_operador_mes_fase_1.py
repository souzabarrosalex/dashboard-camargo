import streamlit as st
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
        ### RECUPERADO FASE 1  
        """
                    )
    recuperado_meta_fase_1 = '7_recuperado_meta_fase_1.png'  # Substitua pelo caminho da sua imagem
    st.image(recuperado_meta_fase_1)    

executar_tarefa()