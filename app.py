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
        <style>
            :root {
                --primary-color: #2e7d32;
                --primary-light: #4caf50;
                --primary-dark: #1b5e20;
                --accent-color: #ffc107;
                --text-light: #ffffff;
                --text-dark: #333333;
                --gradient: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary-color) 50%, var(--primary-light) 100%);
                --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                --transition: all 0.3s ease;
            }
            
            .header-container {
                background: var(--gradient);
                padding: 1.5rem 0;
                box-shadow: var(--shadow);
                position: relative;
                overflow: hidden;
                border-radius: 10px;
                margin-bottom: 2rem;
            }
            
            .header-container::before {
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M0,0 L100,0 L100,100 Z" fill="rgba(255,255,255,0.1)"/></svg>');
                background-size: cover;
            }
            
            .header-content {
                max-width: 100%;
                margin: 0 auto;
                padding: 0 2rem;
                position: relative;
                z-index: 1;
                text-align: center;
            }
            
            .logo-title {
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 0.5rem;
                flex-wrap: wrap;
            }
            
            .logo-icon {
                font-size: 2.5rem;
                margin-right: 0.75rem;
                animation: pulse 2s infinite;
            }
            
            .main-title {
                color: var(--text-light);
                margin: 0;
                font-size: 2.5rem;
                font-weight: 700;
                text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
                letter-spacing: 0.5px;
            }
            
            .subtitle {
                color: var(--text-light);
                font-size: 1.2rem;
                margin: 0;
                font-weight: 400;
                opacity: 0.9;
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
            }
            
            .tagline {
                background-color: rgba(255, 255, 255, 0.2);
                display: inline-block;
                padding: 0.5rem 1.5rem;
                border-radius: 50px;
                margin-top: 1rem;
                font-size: 0.9rem;
                font-weight: 500;
                color: var(--text-light);
                backdrop-filter: blur(5px);
                border: 1px solid rgba(255, 255, 255, 0.3);
            }
            
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.1); }
                100% { transform: scale(1); }
            }
            
            @media (max-width: 768px) {
                .main-title {
                    font-size: 2rem;
                }
                
                .subtitle {
                    font-size: 1rem;
                }
                
                .logo-icon {
                    font-size: 2rem;
                }
            }
        </style>

        <div class="header-container">
            <div class="header-content">
                <div class="logo-title">
                    <div class="logo-icon">🌾</div>
                    <h1 class="main-title">AGRI ANALYTICS BF</h1>
                </div>
                <p class="subtitle">Plateforme Intelligente d'Analyse du Rendement Céréalier</p>
                <div class="tagline">Burkina Faso</div>
            </div>
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
            <p class="subtitle">Realiser par Lassina SANOU, Stagiaire chez ADE</p>
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