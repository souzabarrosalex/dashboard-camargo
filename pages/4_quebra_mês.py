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
        ### QUEBRA MÊS  
        """
                    )
    quebra_mes = '4_quebra_mes.png'  # Substitua pelo caminho da sua imagem
    st.image(quebra_mes)    
executar_tarefa()