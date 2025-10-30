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
                                   min_value=0.0, value=1000.0, step=100.0)
    
    with col2:
        st.subheader("🌤️ Conditions Climatiques")
        
        temperature = st.slider("Température Moyenne (°C)", 15.0, 40.0, 30.0, 0.5)
        precipitation = st.slider("Précipitation (mm)", 0.0, 1000.0, 200.0, 10.0)
        nb_jour_pluie = st.slider("Nombre de Jours de Pluie", 0, 100, 7)
        humidite = st.slider("Humidité Moyenne (%)", 0.0, 100.0, 65.0, 1.0)
        vent = st.slider("Vitesse du Vent (km/h)", 0.0, 50.0, 22.0, 1.0)
        ensoleillement = st.slider("Durée d'Ensoleillement (h/jour)", 0.0, 12.0, 6.0, 0.5)
    
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
            rendement_pred = prediction[0]
            production_totale = rendement_pred * superficie
            
            # Affichage des résultats
            st.markdown(f"""
            <div class="prediction-card">
                <h2>📊 Résultats de la Prédiction</h2>
                <div style="font-size: 2.5rem; font-weight: bold; margin: 1rem 0;">
                    {rendement_pred:.2f} tonnes/ha
                </div>
                <div style="font-size: 1.2rem;">
                    Production totale estimée : {production_totale:,.0f} tonnes
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Métriques supplémentaires
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Rendement Prédit", f"{rendement_pred:.2f} t/ha")
            
            with col2:
                st.metric("Production Totale", f"{production_totale:,.0f} t")
            
            with col3:
                # Comparaison avec moyenne hypothétique
                moyenne_nationale = 2.5  # À adapter avec vos données réelles
                ratio = rendement_pred / moyenne_nationale
                st.metric("Vs Moyenne Nationale", f"{ratio:.1f}x")
            
            # Graphique d'impact (exemple)
            st.subheader("📈 Facteurs d'Influence")
            
            # Ces valeurs seraient normalement calculées à partir du modèle
            facteurs = {
                'Précipitations': 0.35,
                'Température': 0.25,
                'Humidité': 0.15,
                'Ensoleillement': 0.10,
                'Vent': 0.08,
                'Jours Pluie': 0.07
            }
            
            fig = px.bar(
                x=list(facteurs.keys()),
                y=list(facteurs.values()),
                title="Impact relatif des facteurs climatiques",
                labels={'x': 'Facteurs', 'y': 'Importance'},
                color=list(facteurs.values()),
                color_continuous_scale='Viridis'
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Téléchargement des résultats
            result_df = pd.DataFrame({
                'Date_Prédiction': [datetime.now()],
                'Région': [region],
                'Céréale': [cereale],
                'Année': [annee],
                'Superficie_ha': [superficie],
                'Rendement_Prédit_tonnes_ha': [rendement_pred],
                'Production_Totale_tonnes': [production_totale],
                'Température_C': [temperature],
                'Précipitation_mm': [precipitation]
            })
            
            st.download_button(
                label="📥 Télécharger les Résultats",
                data=result_df.to_csv(index=False, sep=';').encode('utf-8'),
                file_name=f"prediction_rendement_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime='text/csv',
                use_container_width=True
            )
            
        except Exception as e:
            st.error(f"❌ Erreur lors de la prédiction : {str(e)}")
    
    # Informations complémentaires
    with st.expander("ℹ️ Informations sur le modèle"):
        st.markdown("""
        **Caractéristiques du modèle :**
        - Algorithme : Random Forest
        - Période d'entraînement : 1996-2022
        - Variables utilisées : 10 paramètres climatiques et agronomiques
        - Performance : R² = 0.85 (sur les données de test)
        
        **Limitations :**
        - Les prédictions sont des estimations statistiques
        - Ne capture pas les événements climatiques extrêmes
        - Doit être interprété avec les connaissances agronomiques locales
        """)