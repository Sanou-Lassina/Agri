import streamlit as st
import pandas as pd
import io
from datetime import datetime

@st.cache_data
def load_data():
    try:
        df = pd.read_excel('base_finale.xlsx')
        st.success("✅ Données chargées avec succès")
        return df
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement des données: {e}")
        return pd.DataFrame()

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
    .data-info {
        background-color: #E8F4FD;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">📊 Exploration des Données</div>', unsafe_allow_html=True)
    
    # Chargement des données
    df = load_data()
    
    # Vérifier si le DataFrame est vide
    if df.empty:
        st.error("Impossible de charger les données. Vérifiez le chemin du fichier.")
        return
    
    # Afficher les informations de base sur les données
    st.markdown(f"""
    <div class="data-info">
    <strong>📈 Informations sur le dataset :</strong><br>
    • {len(df)} enregistrements<br>
    • {len(df.columns)} colonnes<br>
    • Période : {int(df['Année'].min())} - {int(df['Année'].max())}<br>
    • {len(df['Région'].unique())} régions<br>
    • {len(df['Céréale'].unique())} types de céréales
    </div>
    """, unsafe_allow_html=True)
    
    # Filtres dans la sidebar
    st.sidebar.header("🔍 Filtres d'exploration")
    
    # S'assurer que les colonnes existent
    if 'Région' not in df.columns or 'Céréale' not in df.columns:
        st.error("Les colonnes 'Région' et 'Céréale' sont requises mais non trouvées dans le dataset.")
        st.write("Colonnes disponibles:", list(df.columns))
        return
    
    # Nettoyer et trier les valeurs uniques
    regions = sorted([str(region).strip() for region in df['Région'].unique() if pd.notna(region)])
    cereales = sorted([str(cereale).strip() for cereale in df['Céréale'].unique() if pd.notna(cereale)])
    
    # Vérifier qu'il y a des données disponibles
    if not regions or not cereales:
        st.error("Aucune donnée de région ou céréale disponible.")
        return
    
    st.sidebar.markdown("**Sélection des régions:**")
    regions_sel = st.sidebar.multiselect(
        "Choisissez une ou plusieurs régions:", 
        regions, 
        default=regions[:1] if regions else [],
        key="regions_filter"
    )
    
    st.sidebar.markdown("**Sélection des céréales:**")
    cereales_sel = st.sidebar.multiselect(
        "Choisissez une ou plusieurs céréales:", 
        cereales, 
        default=cereales[:1] if cereales else [],
        key="cereales_filter"
    )
    
    # Afficher le statut des filtres
    st.sidebar.markdown("---")
    st.sidebar.markdown("**📊 Statut des filtres:**")
    st.sidebar.write(f"Régions sélectionnées: {len(regions_sel)}")
    st.sidebar.write(f"Céréales sélectionnées: {len(cereales_sel)}")
    
    # Section principale - Affichage conditionnel
    if not regions_sel and not cereales_sel:
        st.info("🎯 **Commencez par sélectionner des régions et/ou des céréales dans les filtres à gauche.**")
        
        # Aperçu des données brutes
        with st.expander("👀 Aperçu des données brutes (premiers 20 enregistrements)", expanded=True):
            st.dataframe(df.head(20), use_container_width=True)
            
            # Informations détaillées sur le dataset
            st.subheader("📋 Informations détaillées du dataset")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Colonnes disponibles:**")
                for col in df.columns:
                    st.write(f"• {col}")
            
            with col2:
                st.write("**Statistiques générales:**")
                st.write(f"• Valeurs manquantes: {df.isnull().sum().sum()}")
                st.write(f"• Types de données:")
                for col, dtype in df.dtypes.items():
                    st.write(f"  - {col}: {dtype}")
    
    elif regions_sel and cereales_sel:
        # Filtrage des données avec gestion des erreurs
        try:
            df_filtre = df[
                (df['Région'].isin(regions_sel)) & 
                (df['Céréale'].isin(cereales_sel))
            ].copy()
            
            if df_filtre.empty:
                st.warning("⚠️ Aucune donnée ne correspond aux critères sélectionnés.")
                
                # Afficher les données disponibles pour aider au débogage
                with st.expander("🔍 Données disponibles pour débogage"):
                    st.write("**Régions dans le dataset:**", regions)
                    st.write("**Céréales dans le dataset:**", cereales)
                    st.write("**Aperçu des données brutes:**")
                    st.dataframe(df.head(10), use_container_width=True)
            else:
                st.success(f"✅ {len(df_filtre)} enregistrements trouvés pour {len(regions_sel)} région(s) et {len(cereales_sel)} céréale(s)")
                
                # Affichage du dataframe filtré
                st.subheader("📋 Données filtrées")
                st.dataframe(df_filtre, use_container_width=True)
                
                # Statistiques descriptives
                st.subheader("📈 Statistiques Descriptives")
                
                # Sélection des colonnes numériques pour les statistiques
                colonnes_numeriques = df_filtre.select_dtypes(include=['number']).columns
                
                if len(colonnes_numeriques) > 0:
                    stats = df_filtre[colonnes_numeriques].describe()
                    st.dataframe(stats, use_container_width=True)
                else:
                    st.info("Aucune colonne numérique trouvée pour les statistiques descriptives.")
                
                # Analyses supplémentaires
                st.subheader("🔍 Analyses par catégorie")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Production moyenne par région:**")
                    prod_region = df_filtre.groupby('Région')['Production'].mean().round(2)
                    st.dataframe(prod_region, use_container_width=True)
                
                with col2:
                    st.write("**Rendement moyen par céréale:**")
                    rendement_cereale = df_filtre.groupby('Céréale')['Rendement'].mean().round(2)
                    st.dataframe(rendement_cereale, use_container_width=True)
                
                # Export des données
                st.subheader("💾 Export des Données")

                col_export1, col_export2 = st.columns([2, 1])

                with col_export1:
                    st.info("Téléchargez les données filtrées au format Excel")

                with col_export2:
                    if df_filtre.empty:
                        st.warning("⚠️ Aucune donnée à exporter")
                    else:
                        # Créer un buffer en mémoire
                        buffer = io.BytesIO()
                        
                        # Utiliser pandas pour créer le fichier Excel
                        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                            # Écrire les données
                            df_filtre.to_excel(writer, index=False, sheet_name='Données filtrées')
                            
                            # Fermer le writer
                            writer.close()
                        
                        # Se déplacer au début du buffer
                        buffer.seek(0)
                        
                        st.download_button(
                            label=f"📥 Télécharger Excel ({len(df_filtre)} lignes)",
                            data=buffer,
                            file_name=f'donnees_filtrees_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx',
                            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                            use_container_width=True
                        )
        
        except Exception as e:
            st.error(f"❌ Erreur lors du filtrage des données: {e}")
            st.info("Vérifiez que les noms de régions et céréales correspondent exactement à ceux du dataset.")
    
    else:
        st.warning("⚠️ Veuillez sélectionner au moins une région ET une céréale pour afficher les données filtrées.")
        
        # Afficher ce qui est sélectionné
        if regions_sel:
            st.write(f"**Régions sélectionnées:** {', '.join(regions_sel)}")
        if cereales_sel:
            st.write(f"**Céréales sélectionnées:** {', '.join(cereales_sel)}")
        
        # Aperçu des données brutes
        with st.expander("👀 Aperçu des données brutes (premiers 15 enregistrements)"):
            st.dataframe(df.head(15), use_container_width=True)
    
    # Section de débogage (optionnelle - peut être masquée)
    with st.expander("🔧 Informations de débogage", expanded=False):
        st.write("**Colonnes du dataset:**", list(df.columns))
        st.write("**Types de données:**")
        st.write(df.dtypes)
        st.write("**Valeurs manquantes par colonne:**")
        st.write(df.isnull().sum())
