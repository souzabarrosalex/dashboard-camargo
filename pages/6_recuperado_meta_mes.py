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
        ### RECUPERADO META MÊS  
        """
                    )
    recuperado_meta = '6_recuperado_meta.png'  # Substitua pelo caminho da sua imagem
    st.image(recuperado_meta)    

executar_tarefa()