import streamlit as st

# CSS personnalisé pour un design agricole professionnel
st.markdown("""
<style>
    /* Style général */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Header personnalisé */
    .header-container {
        background: linear-gradient(135deg, #2e7d32 0%, #4caf50 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Style de la barre latérale */
    .css-1d391kg, .css-1lcbmhc {
        background: linear-gradient(180deg, #1b5e20 0%, #2e7d32 100%);
    }
    
    /* Style des éléments de la barre latérale */
    .sidebar .sidebar-content {
        background-color: #1b5e20;
    }
    
    /* Style des radio buttons dans la sidebar */
    .stRadio > div {
        flex-direction: column;
        gap: 10px;
    }
    
    .stRadio > div > label {
        background-color: #4caf50 !important;
        padding: 12px 16px !important;
        border-radius: 8px !important;
        margin: 5px 0 !important;
        color: white !important;
        font-weight: 500 !important;
        border: none !important;
        transition: all 0.3s ease !important;
    }
    
    .stRadio > div > label:hover {
        background-color: #388e3c !important;
        transform: translateX(5px);
    }
    
    .stRadio > div > label[data-testid="stRadio"]:has(input:checked) {
        background-color: #ff9800 !important;
        color: white !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Masquer la navigation automatique des pages */
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Style pour les titres */
    h1, h2, h3 {
        color: #2e7d32;
    }
    
    /* Cartes et conteneurs */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #4caf50;
        margin: 10px 0;
    }
    
    /* Boutons */
    .stButton button {
        background-color: #4caf50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: 500;
    }
    
    .stButton button:hover {
        background-color: #388e3c;
    }
</style>
""", unsafe_allow_html=True)

# En-tête personnalisé avec image à droite et meilleur alignement
def render_header():
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        <div style="padding: 0.5rem 0;">
            <h1 style="color: #2e7d32; margin: 0; font-size: 2.2em;">🌾 AGRI ANALYTICS BF 🌾</h1>
            <p style="color: #4caf50; font-size: 1.1em; margin: 0; font-weight: 500;">
                Plateforme Intelligente d'Analyse du Rendement Céréalier - Burkina Faso
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        try:
            st.image("ade.jpg", width=800)
        except FileNotFoundError:
            st.markdown("""
            <div style="text-align: center; padding: 0.5rem;">
                <span style="font-size: 3em;">🌾</span>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")


# Barre latérale améliorée
def render_sidebar():
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h2 style="color: blue; margin-bottom: 2rem;">🌱 Navigation</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Options de navigation avec icônes et descriptions
    page_options = [
        "🏠 Accueil",
        "📊 Données & Filtres", 
        "📈 Visualisations",
        "🔮 Prédictions",
        "📚 Guide"
    ]
    page = st.sidebar.radio("**Sélectionnez une section:**", page_options)
    
    return page

# Application principale
def main():
    # Afficher l'en-tête
    render_header()
    
    # Afficher la barre latérale et récupérer la page sélectionnée
    page = render_sidebar()

    # Chargement des pages en fonction de la sélection
    try:
        if page == "🏠 Accueil":
            import accueil
            accueil.show()
        elif page == "📊 Données & Filtres":
            import donnees_filtres
            donnees_filtres.show()
        elif page == "📈 Visualisations":
            import visualisations
            visualisations.show()
        elif page == "🔮 Prédictions":
            import predictions
            predictions.show()
        elif page == "📚 Guide":
            import guide
            guide.show()
    except Exception as e:
        st.error(f"Erreur lors du chargement de la page: {str(e)}")
        st.info("Veuillez vérifier que tous les modules sont correctement importés.")

if __name__ == "__main__": 
    main()