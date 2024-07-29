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
    nao_atuados_pesados = '11_nao_atuados_pesados.png'  # Substitua pelo caminho da sua imagem
    st.image(nao_atuados_pesados)    

executar_tarefa()