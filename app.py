import streamlit as st
import time

# Configuração da página
st.set_page_config(page_title="Com amor, Bianca!", page_icon="❤️")

# Estilização customizada para o botão e o texto
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        color: white;
        border: 2px solid white;
    }
    .big-font {
        font-size: 50px !important;
        text-align: center;
        color: #ff4b4b;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Ei, tenho um segredo... 🤫")
st.write("Clique no botão abaixo para descobrir.")

# Lógica do Clique
if st.button("CLIQUE AQUI ❤️"):
    # Efeito de balões subindo (nativos do Streamlit)
    st.balloons()
    
    # Simula uma pequena "chuva" de corações com texto
    placeholder = st.empty()
    
    with placeholder.container():
        st.markdown('<p class="big-font">❤️ TE AMO ❤️</p>', unsafe_allow_html=True)
        
        # Aqui criamos a "chuva" visual usando colunas
        cols = st.columns(5)
        for i in range(10): # Repete o ciclo de corações
            for col in cols:
                col.write("❤️")
            time.sleep(0.1)

    # Mensagem final carinhosa
    st.snow() # Isso cria um efeito suave de partículas caindo
    st.success("Você é muito especial!")
