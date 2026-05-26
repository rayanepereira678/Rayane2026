import streamlit as st

st.set_page_config(page_title="Empresas Parceiras", layout="wide")

st.title("Empresas Parceiras")

col1, col2, col3 = st.columns(3)

with col1:
    try:
        st.image("spacex.png")
    except:
        st.write("Imagem não encontrada")
    st.subheader("SpaceX")
    st.write("Empresa aeroespacial criada por Elon Musk.")
    st.link_button("Acessar Site", "https://www.spacex.com/")

with col2:
    try:
        st.image("apple.png")
    except:
        st.write("Imagem não encontrada")
    st.subheader("Apple")
    st.write("Empresa conhecida por iPhone, iPad e MacBook.")
    st.link_button("Acessar Site", "https://www.apple.com/br/")

with col3:
    try:
        st.image("netflix.png")
    except:
        st.write("Imagem não encontrada")
    st.subheader("Netflix")
    st.write("Plataforma de streaming mundial.")
    st.link_button("Acessar Site", "https://www.netflix.com/br/")
