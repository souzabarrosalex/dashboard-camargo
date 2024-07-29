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
        ### NÃO ATUADOS DAYCOLLECTION  
        """
                    )
    nao_atuados_daycollection = '10_nao_atuados_daycollection.png'  # Substitua pelo caminho da sua imagem
    st.image(nao_atuados_daycollection)    

executar_tarefa()