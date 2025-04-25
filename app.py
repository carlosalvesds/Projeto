import streamlit as st
import zipfile
import os
import pandas as pd
from io import BytesIO
from tempfile import TemporaryDirectory

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="NotaAI - Soluções Fiscais",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CONTROLE DE TEMA
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# TEMA
tema = "Escuro" if st.session_state.dark_mode else "Claro"

# SIDEBAR
with st.sidebar:
    st.title("🧰 Ferramentas")
    pagina = st.radio(
        "Selecione uma aplicação:",
        ["🏠 Home", "📥 Importador XML NF-e", "📥 Importador XML NFC-e", "📄 Conversor PDF"],
        index=0,
    )
    st.button(f"🔁 Mudar para tema { 'Claro' if tema == 'Escuro' else 'Escuro' }", on_click=toggle_theme)
    st.markdown("---")
    st.markdown("🔗 Desenvolvido por Carlos Eduardo")

# ESTILO CUSTOMIZADO
st.markdown(
    f"""
    <style>
    body {{
        background-color: {"#121212" if st.session_state.dark_mode else "#f5f5f5"};
        color: {"#f0f0f0" if st.session_state.dark_mode else "#000000"};
    }}
    .stButton>button {{
        background-color: {"#4CAF50" if st.session_state.dark_mode else "#0A66C2"};
        color: white;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# TELAS
if pagina == "🏠 Home":
    st.markdown(
        f"""
        <h1 style='color: {"#f0f0f0" if st.session_state.dark_mode else "#333"}'>💼 NotaAI</h1>
        <p style='font-size: 18px; color: {"#ccc" if st.session_state.dark_mode else "#555"}'>
        Solução inteligente para extração e análise de documentos fiscais.<br><br>
        Escolha uma das ferramentas no menu lateral para começar:
        </p>
        <ul>
        <li><b>Importador XML NF-e</b>: Geração de planilha Excel com abas estruturadas a partir de notas fiscais eletrônicas (modelo 55)</li>
        <li><b>Importador XML NFC-e</b>: Extração detalhada por item para conferência de cupons fiscais eletrônicos (modelo 65)</li>
        <li><b>Conversor de PDF</b>: Leitura de faturas de energia elétrica em PDF, conversão para Excel</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

elif pagina == "📥 Importador XML NF-e":
    st.header("📥 Importador XML NF-e")
    st.markdown("🔍 Carregue seus XMLs de NF-e para gerar a planilha estruturada.")
    uploaded_files = st.file_uploader("Upload de arquivos XML (.xml ou .zip)", type=["xml", "zip"], accept_multiple_files=True)
    if st.button("🚀 Processar XMLs") and uploaded_files:
        st.success("Processamento concluído com sucesso!")
        st.download_button("📥 Baixar Planilha NF-e", b"Arquivo Excel Simulado", file_name="notas_nfe.xlsx")

elif pagina == "📥 Importador XML NFC-e":
    st.header("📥 Importador XML NFC-e")
    st.markdown("🔍 Carregue seus XMLs de NFC-e para gerar a planilha item a item.")
    uploaded_files = st.file_uploader("Upload de arquivos NFC-e (.xml ou .zip)", type=["xml", "zip"], accept_multiple_files=True)
    if st.button("🚀 Processar NFC-e") and uploaded_files:
        st.success("Planilha NFC-e gerada!")
        st.download_button("📥 Baixar Planilha NFC-e", b"Arquivo Excel NFC-e", file_name="notas_nfce.xlsx")

elif pagina == "📄 Conversor PDF":
    st.header("📄 Conversor de PDF - Fatura de Energia Elétrica")
    st.markdown("🔌 Envie arquivos PDF para conversão automática em planilha.")
    uploaded_pdfs = st.file_uploader("Upload de PDFs ou ZIP com PDFs", type=["pdf", "zip"], accept_multiple_files=True)
    if st.button("⚡ Converter PDFs") and uploaded_pdfs:
        st.success("Faturas processadas com sucesso!")
        st.download_button("📥 Baixar Planilha Energia", b"Arquivo Excel Energia", file_name="faturas_energia.xlsx")
