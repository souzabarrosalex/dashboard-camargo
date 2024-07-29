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
        ### QUEBRA PERIODO  
        """
                    )
    quebra_1 = '3_quebra_periodo.png'  # Substitua pelo caminho da sua imagem
    st.image(quebra_1)    
executar_tarefa()