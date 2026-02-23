import streamlit as st
import time
import random

# Configuração da página
st.set_page_config(page_title="Com amor, Bianca!", page_icon="❤️")

# --- COLOQUE O LINK DA SUA FOTO AQUI ---
URL_DA_MINHA_FOTO = "https://suafoto.com/imagem.jpg" 

# Estilização customizada e Animação de Chuva
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
    
    /* Estilo das imagens/corações que caem */
    .falling-item {
        position: fixed;
        top: -15%;
        user-select: none;
        z-index: 9999;
        pointer-events: none;
        animation: fall linear forwards;
        border-radius: 50%; /* Deixa a foto redondinha */
    }

    @keyframes fall {
        to { transform: translateY(115vh) rotate(360deg); }
    }
    </style>
    """, unsafe_allow_html=True)

def chuva_personalizada(url_imagem):
    html_items = ""
    for i in range(25): # Quantidade de fotos caindo
        left = random.randint(0, 95)
        size = random.randint(50, 80) # Tamanho da foto em pixels
        duration = random.uniform(2, 5)
        delay = random.uniform(0, 3)
        
        # Cria a tag da imagem
        html_items += f'''
            <img src="{url_imagem}" class="falling-item" 
            style="left: {left}%; width: {size}px; height: {size}px; 
            animation-duration: {duration}s; animation-delay: {delay}s; object-fit: cover;">
        '''
    st.markdown(html_items, unsafe_allow_html=True)

st.title("Com amor, Bianca")
st.write("Clique no botão abaixo para descobrir.")

# Lógica do Clique
if st.button("CLIQUE AQUI ❤️"):
    # Disparar a chuva com a foto
    chuva_personalizada(https://i.imgur.com/4fydr4j.jpg)
    
    # Efeito de balões subindo
    st.balloons()
    
    # Texto central
    st.markdown('<p style="font-size: 40px; text-align: center; color: #ff4b4b; font-weight: bold;">'
                '❤️ TE AMO! HOJE, AMANHÃ E SEMPRE! ❤️</p>', unsafe_allow_html=True)
    
    time.sleep(1)
    st.success("Você é o amor da minha vida!")
