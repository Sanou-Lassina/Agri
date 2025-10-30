import streamlit as st
from PIL import Image
import base64

def show():
    # CSS personnalisé pour une apparence professionnelle
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #A23B72;
        margin: 1.5rem 0 1rem 0;
    }
    .feature-card {
        background-color: #F8F9FA;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2E86AB;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #2E86AB, #A23B72);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Section d'introduction
    st.markdown("""
    <div style='background-color: #E8F4FD; padding: 2rem; border-radius: 10px; margin: 1rem 0;'>
    <h3 style='color: #1a5276; margin-top: 0;'>Bienvenue sur la plateforme d'analyse des rendements céréaliers</h3>
    <p style='color: #333; line-height: 1.6;'>
    Cet outil interactif vous permet d'explorer, analyser et prédire les rendements céréaliers 
    au Burkina Faso sur la période 1996-2022. Utilisez la navigation sur la gauche pour accéder 
    aux différentes fonctionnalités.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # Métriques principales
    st.markdown('<div class="sub-header">📈 Aperçu des données</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">13</div>
            <div>Régions</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">7</div>
            <div>Types de céréales</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">27</div>
            <div>Années d'analyse</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">6</div>
            <div>Variables climatiques</div>
        </div>
        """, unsafe_allow_html=True)

    # Fonctionnalités principales
    st.markdown('<div class="sub-header">🚀 Fonctionnalités principales</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Exploration des données</h4>
            <p>Filtrez et explorez les données historiques par région, céréale et période</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>📈 Visualisations avancées</h4>
            <p>Graphiques interactifs et analyses temporelles des rendements</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🔮 Prédictions IA</h4>
            <p>Modèles de machine learning pour estimer les rendements futurs</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>📚 Documentation complète</h4>
            <p>Guide d'utilisation et informations techniques</p>
        </div>
        """, unsafe_allow_html=True)

    # Appel à l'action
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
    <h3 style='color: #2E86AB;'>Prêt à commencer votre analyse ?</h3>
    <p>Utilisez le menu de navigation sur la gauche pour explorer les différentes sections de l'application.</p>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9rem;'>
    <p>Plateforme d'Analyse du Rendement Céréalier - Burkina Faso • Développé avec Streamlit</p>
    </div>
    """, unsafe_allow_html=True)