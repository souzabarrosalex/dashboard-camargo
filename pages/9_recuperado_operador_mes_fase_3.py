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
        ### RECUPERADO FASE 3  
        """
                    )
    recuperado_meta_fase_3 = '9_recuperado_meta_fase_3.png'  # Substitua pelo caminho da sua imagem
    st.image(recuperado_meta_fase_3)    

executar_tarefa()