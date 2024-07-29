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
        ### RANK DO DIA  
        """
                    )
    rank_do_dia = '2_rank_do_dia.jpeg'  # Substitua pelo caminho da sua imagem
    st.image(rank_do_dia)    

executar_tarefa()