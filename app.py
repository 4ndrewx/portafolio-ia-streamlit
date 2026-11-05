import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Portafolio de IA | Andres Felipe Gonzalez",
    page_icon="✨",
    layout="wide",
)

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown(
    """
    <style>
    .main { background-color: #0E1117; }
    .stSidebar { background-color: #161B22 !important; }
    .hero-banner {
        background: linear-gradient(135deg, #7C3AED 0%, #4F46E5 50%, #EC4899 100%);
        padding: 35px;
        border-radius: 15px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    }
    .app-card {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .stButton>button {
        background: linear-gradient(135deg, #8B5CF6 0%, #6D28D9 100%);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 8px 16px;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #7C3AED 0%, #5B21B6 100%);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- BARRA LATERAL ---
st.sidebar.markdown("### 💻 Repositorio de IA")
st.sidebar.markdown(
    "<p style='color: #9CA3AF; font-size: 13px;'>Portafolio de Proyectos</p>",
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")
st.sidebar.write(
    "La Inteligencia Artificial permite mejorar la toma de decisiones con el uso"
    " de datos, automatizar tareas rutinarias y proporcionar análisis"
    " avanzados en tiempo real."
)
st.sidebar.markdown("---")
st.sidebar.markdown(
    "🔗 **Sitio Oficial:** [Universidad"
    " EAFIT](https://www.eafit.edu.co)<br>",
    unsafe_allow_html=True,
)

# --- HERO BANNER PRINCIPAL ---
st.markdown(
    """
    <div class="hero-banner">
        <h1 style="margin:0; font-size: 2.5rem;">Mis Aplicaciones de Inteligencia Artificial ✨</h1>
        <p style="margin-top: 10px; font-size: 1.1rem; opacity: 0.9;">Repositorio interactivo de proyectos e interfaces organizadas.</p>
    </div>
""",
    unsafe_allow_html=True,
)

# ==========================================
# SECCIÓN 1: INICIO Y PROCESAMIENTO BÁSICO
# ==========================================
st.markdown("### 🚀 Fundamentos y Primeras Apps")
col1, col2, col3 = st.columns(3)

with col1:
  st.markdown(
      '<div class="app-card"><h4>✨ Mi Primera App</h4></div>',
      unsafe_allow_html=True,
  )
  st.link_button(
      "Abrir App ↗",
      "https://mi-primera-app-a2ad8xawazwjcamzkwuaze.streamlit.app/",
  )

with col2:
  st.markdown(
      '<div class="app-card"><h4>📖 Lector de Fábulas</h4></div>',
      unsafe_allow_html=True,
  )
  st.link_button(
      "Abrir App ↗",
      "https://lector-de-fabulas-onlmswaqnqekpw8isal7yf.streamlit.app/",
  )

with col3:
  st.markdown(
      '<div class="app-card"><h4>☁️ Wordcloud Studio</h4></div>',
      unsafe_allow_html=True,
  )
  st.link_button(
      "Abrir App ↗", "https://wordcloud-studio-wkkt85jjfjj88unbf87wkm.streamlit.app/"
  )

st.markdown("---")

# ==========================================
# SECCIÓN 2: VISIÓN ARTIFICIAL Y OCR
# ==========================================
st.markdown("### 📷 Visión Artificial y Reconocimiento Óptico")
col4, col5, col6 = st.columns(3)

with col4:
  st.markdown(
      '<div class="app-card"><h4>🌐 Traductor de Fotos</h4></div>',
      unsafe_allow_html=True,
  )
  st.link_button(
      "Abrir App ↗",
      "https://traductor-de-fotos-gxjbmrf6dqnz4mmr98uote.streamlit.app/",
  )

with col5:
  st.markdown(
      '<div class="app-card"><h4>📄 Transcritor Fotos OCR</h4></div>',
      unsafe_allow_html=True,
  )
  st.link_button(
      "Abrir App ↗",
      "https://transcritor-fotos-ocr-4hkehuod46sszqcyh9ixmy.streamlit.app/",
  )

with col6:
  st.markdown(
      '<div class="app-card"><h4>🎯 YOLOv5 Streamlit App</h4></div>',
      unsafe_allow_html=True,
  )
  st.link_button(
      "Abrir App ↗",
      "https://yolov5-app-app-edztza6lgf84s9ctbuamxr.streamlit.app/",
  )

st.markdown("---")

# ==========================================
# SECCIÓN 3: PROCESAMIENTO DE TEXTO Y NLP
# ==========================================
st.markdown("### 💬 Procesamiento de Lenguaje Natural (NLP)")
col7, col8 = st.columns(2)

with col7:
  st.markdown(
      '<div class="app-card"><h4>📊 Analizador de Sentimientos</h4></div>',
      unsafe_allow_html=True,
  )
  st.link_button("Abrir App ↗", "https://hhy4fvxoujrgnx8svexgrt.streamlit.app/")

with col8:
  st.markdown(
      '<div class="app-card"><h4>🔍 Búsqueda TF-IDF</h4></div>',
      unsafe_allow_html=True,
  )
  # Reemplaza con la URL real de tu app TF-IDF cuando la despliegues
  st.link_button("Abrir App ↗", "https://gozwnplr4q8bgopwc7zllc.streamlit.app/")

st.markdown("---")

# ==========================================
# SECCIÓN 4: INTERACCIÓN Y GESTOS (MEDIAPIPE)
# ==========================================
st.markdown("### ✋ Interacción Multimodal y Visión en Vivo")
col9, col10 = st.columns(2)

with col9:
  st.markdown(
      '<div class="app-card"><h4>✋ Gestos con la Mano</h4></div>',
      unsafe_allow_html=True,
  )
  # Reemplaza con la URL real de tu app de gestos con la mano
  st.link_button("Abrir App ↗", "https://reconocimiento-gestos-mano-app-n5euvkxy3drpd3pnenpcpc.streamlit.app/")

with col10:
  st.markdown(
      '<div class="app-card"><h4>🕺 Baile Y.M.C.A.</h4></div>',
      unsafe_allow_html=True,
  )
  # Reemplaza con la URL real de tu app de YMCA
  st.link_button("Abrir App ↗", "https://reconocimiento-ymca-app-bgycbk7erdxddmtzjbvnvl.streamlit.app/")
