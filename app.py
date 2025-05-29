
import streamlit as st

# --- CONFIGURAÇÕES DA PÁGINA ---
st.set_page_config(page_title="FiscAI", layout="wide", page_icon="🤖")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
        body {
            background-color: #0b0f1a;
            color: #ffffff;
        }
        .fiscai-title {
            font-family: 'Courier New', monospace;
            font-size: 72px;
            color: #00f0ff;
            text-align: center;
            padding-top: 50px;
        }
        .slogan {
            font-family: 'Arial', sans-serif;
            font-size: 20px;
            color: #94d6ff;
            text-align: center;
            margin-top: -10px;
        }
        .footer {
            position: fixed;
            bottom: 20px;
            width: 100%;
            text-align: center;
            font-size: 14px;
            color: #888;
        }
        .sidebar-title {
            font-size: 24px;
            color: #00f0ff;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.markdown("<div class='sidebar-title'>🧰 Ferramentas</div>", unsafe_allow_html=True)
st.sidebar.markdown("🔹 Importador XML NF-e")
st.sidebar.markdown("🔹 Conversor PDF Energia")
st.sidebar.markdown("🔹 Download Automático IPTU")
st.sidebar.markdown("🔹 Resumo ICMS / CST")

# --- CONTEÚDO PRINCIPAL ---
st.markdown("<div class='fiscai-title'>FiscAI</div>", unsafe_allow_html=True)
st.markdown("<div class='slogan'>Automatize. Analise. Avance.</div>", unsafe_allow_html=True)

st.markdown("---")
st.write("🚀 Aqui futuramente estarão as ferramentas inteligentes para leitura de XML, PDF e muito mais.")

st.markdown("<div class='footer'>© 2025 - Desenvolvido com 💡 por Carlos Eduardo</div>", unsafe_allow_html=True)
