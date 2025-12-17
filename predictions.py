import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from datetime import datetime

def show():
    st.markdown("""
    <style>
    .section-header {
        font-size: 1.8rem;
        color: #2E86AB;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid #2E86AB;
        padding-bottom: 0.5rem;
    }
    .prediction-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">🔮 Prédiction du Rendement</div>', unsafe_allow_html=True)
    
    st.info("""
    🎯 Ce module utilise un modèle de machine learning (Random Forest) entraîné sur les données historiques 
    de 1996 à 2022 pour prédire les rendements céréaliers en fonction des paramètres climatiques et agronomiques.
    """)
    
    # Chargement du modèle
    @st.cache_resource
    def load_model():
        try:
            return joblib.load('model_rendement.pkl')
        except:
            st.error("❌ Modèle non trouvé. Vérifiez que le fichier 'model_rendement.pkl' est présent.")
            return None
    
    model = load_model()
    
    if model is None:
        return
    
    # Formulaire de prédiction
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Paramètres d'Entrée")
        
        region = st.selectbox("Région", 
                            ['Sahel', 'Centre', 'Boucle du Mouhoun', 'Centre-Sud', 
                            'Centre-Nord', 'Hauts-Bassins', 'Cascades', 'Plateau Centrale',
                            'Est', 'Centre-Ouest', 'Nord', 'Sud-Ouest'])
        
        cereale = st.selectbox("Type de Céréale", 
                            ['Arachide', 'Coton', 'Maïs', 'Mil', 'Nebié', 'Riz', 'Sorgho'])
        
        annee = st.number_input("Année de projection", 
                            min_value=2023, max_value=2030, value=2023)
        
        superficie = st.number_input("Superficie cultivée (ha)", 
                                min_value=0.0, value=100000.0, step=500.0)
    
    with col2:
        st.subheader("🌤️ Conditions Climatiques")
        
        temperature = st.slider("Température moyenne annuelle (°C)", 15.0, 40.0, 30.0, 0.5)
        precipitation = st.slider("Précipitations moyennes annuelles (mm)", 0.0, 1000.0, 200.0, 10.0)
        nb_jour_pluie = st.slider("Nombre de jour moyen annuel de pluie", 0, 360, 80)
        humidite = st.slider("Humidité relative moyenne annuelle (%)", 0.0, 100.0, 65.0, 1.0)
        vent = st.slider("Vitèsse du vent moyen annuel (km/h)", 0.0, 50.0, 22.0, 1.0)
        ensoleillement = st.slider("Durée moyenne d'ensoleillement (heures/jour)", 0.0, 12.0, 6.0, 0.5)
    
    # Bouton de prédiction
    if st.button("🎯 Calculer la Prédiction", type="primary", use_container_width=True):
        # Création des données d'entrée
        input_data = pd.DataFrame({
            'Région': [region],
            'Céréale': [cereale],
            'Année': [annee],
            'Superficie': [superficie],
            'Température': [temperature],
            'Précipitation': [precipitation],
            'Nombre_Jour_Pluie': [nb_jour_pluie],
            'Humidité': [humidite],
            'Vitèsse_Vent': [vent],
            'Durée_Ensoleillement': [ensoleillement]
        })
        
        try:
            # Prédiction
            prediction = model.predict(input_data)
            production_totale_region = prediction[0]  # Production totale prédite pour la région (en tonnes)
            
            # Calcul du rendement par hectare
            rendement_par_ha = production_totale_region / superficie if superficie > 0 else 0
            
            # Ajout de styles CSS supplémentaires
            st.markdown("""
            <style>
            .metric-card {
                background: white;
                padding: 1.5rem;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
                margin: 0.5rem;
            }
            .metric-value {
                font-size: 2rem;
                font-weight: bold;
                color: #2E86AB;
                margin: 0.5rem 0;
            }
            .metric-label {
                font-size: 1rem;
                color: #666;
                margin-bottom: 0.5rem;
            }
            .comparison-positive {
                color: #28a745;
                font-weight: bold;
            }
            .comparison-negative {
                color: #dc3545;
                font-weight: bold;
            }
            </style>
            """, unsafe_allow_html=True)
            
            # Section principale des résultats
            st.markdown('<div class="section-header">📊 Résultats de la Prédiction</div>', unsafe_allow_html=True)
            
            
            # Métriques principales dans un tableau
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Production prédit de la région estimé</div>
                    <div class="metric-value">{production_totale_region:.2f}</div>
                    <div>tonnes</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Rendement de la région estimé</div>
                    <div class="metric-value">{rendement_par_ha:.2f}</div>
                    <div>tonnes/ha</div>
                </div>
                """, unsafe_allow_html=True)
            
            
        except Exception as e:
            st.error(f"❌ Erreur lors de la prédiction : {str(e)}")
            st.error("Veuillez vérifier les données d'entrée et réessayer.")
    
    with st.expander("ℹ️ À propos de ces résultats"):
        st.markdown(f"""
        **Interprétation des résultats :**
        
        Cette prédiction fournit une **estimation régionale** du rendement de **{cereale}** dans la région 
        **{region}** pour l'année **{annee}**, basée sur les paramètres climatiques que vous avez saisis.
        
        **Points clés :**
        - ✅ **Prédiction régionale** : Spécifique à {region}
        - ✅ **Basée sur le climat** : Intègre température ({temperature}°C), précipitations ({precipitation}mm), etc.
        - ✅ **Modèle statistique** : Entraîné sur données historiques 1996-2022
        - ⚠️ **Estimation** : À utiliser pour la planification, pas comme garantie
        
        **Utilisation recommandée :** Planification agricole, estimation des besoins en intrants, projection des récoltes.
        """)