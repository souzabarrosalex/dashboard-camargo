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
        ### PRODUÇÃO DO DIA  
        """
                    )
    producao_dia = '1_producao_dia.png'  # Substitua pelo caminho da sua imagem
    st.image(producao_dia)    

executar_tarefa()