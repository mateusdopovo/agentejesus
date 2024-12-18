import streamlit as st
from agente_jesus import jesus_agent

st.title("Agente Jesus")
st.write("Faça uma pergunta e receba uma resposta inspirada nos ensinamentos bíblicos.")

pergunta = st.text_input("Digite sua pergunta:")

if st.button("Perguntar"):
    resposta = jesus_agent(pergunta)
    st.write("Jesus responde:")
    st.write(resposta)
