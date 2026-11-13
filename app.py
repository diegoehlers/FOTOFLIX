
import streamlit as st

# ==========================================
# CONFIGURAÇÕES DO FOTOfLIX
# ==========================================

# COLE AQUI O LINK ATUAL DO SEU FOTOFLIX
FOTOFLIX_URL = https://script.google.com/macros/s/AKfycbyNCDQ-X1ffrvYGvXDP7JhMQm2p7bMFpSIG8y5LhABggNGhC9l16iorLK8Di-upu_bR/exec

st.set_page_config(
    page_title="FotoFlix",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# ESTILO VISUAL
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #141414;
    color: white;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    max-width: 850px;
    padding-top: 5rem;
}

.logo {
    color: #E50914;
    font-size: 54px;
    font-weight: 900;
    text-align: center;
    letter-spacing: -2px;
}

.subtitulo {
    color: #ffffff;
    font-size: 28px;
    font-weight: 700;
    text-align: center;
    margin-top: 35px;
}

.descricao {
    color: #b3b3b3;
    text-align: center;
    font-size: 16px;
    margin-top: 15px;
    margin-bottom: 35px;
}

.rodape {
    color: #777777;
    font-size: 12px;
    text-align: center;
    margin-top: 65px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# PÁGINA PRINCIPAL
# ==========================================

st.markdown(
    '<div class="logo">FotoFlix</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">'
    'Suas memórias, sempre por perto.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="descricao">'
    'Um espaço especial para guardar, '
    'compartilhar e reviver seus melhores momentos.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

if FOTOFLIX_URL.startswith("https://"):
    st.link_button(
        "🎬  ABRIR FOTOFLIX",
        FOTOFLIX_URL,
        type="primary",
        use_container_width=True
    )
else:
    st.warning(
        "Configure o endereço do FotoFlix "
        "no código app.py antes de publicar."
    )

st.write("")

st.markdown(
    '<div class="rodape">'
    'FotoFlix © 2026 | Feito para guardar momentos especiais.'
    '</div>',
    unsafe_allow_html=True
)
