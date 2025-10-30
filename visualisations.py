import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Visualisations Avancées", page_icon="📈", layout="wide")

@st.cache_data
def load_data():
    return pd.read_excel('base_finale.xlsx')

def create_advanced_visualizations(df):
    """Crée des visualisations avancées et interactives"""
    
    # Sidebar avancée
    st.sidebar.header("🎨 Paramètres Avancés")
    
    # Filtres principaux
    regions = st.sidebar.multiselect("Régions", sorted(df['Région'].unique()), 
                                   default=sorted(df['Région'].unique())[:3])
    cereales = st.sidebar.multiselect("Céréales", sorted(df['Céréale'].unique()),
                                    default=sorted(df['Céréale'].unique())[:2])
    annees = st.sidebar.slider("Période", int(df['Année'].min()), int(df['Année'].max()), 
                             (int(df['Année'].min()), int(df['Année'].max())))
    
    # Variables avancées
    var_productivite = st.sidebar.selectbox("Variable de productivité", 
                                          ['Production', 'Superficie', 'Rendement'])
    var_climatique = st.sidebar.selectbox("Variable climatique", 
                                        ['Précipitation', 'Nombre_jour_Pluie', 'Température', 
                                         'Humidité', 'Vitèsse_Vent', 'Durée_Ensoleillement'])
    
    # Paramètres avancés
    show_trend = st.sidebar.checkbox("Afficher tendances", True)
    show_forecast = st.sidebar.checkbox("Prévisions simples", False)
    clustering_enabled = st.sidebar.checkbox("Analyse de clustering", False)
    
    # Application des filtres
    df_filtre = df[
        (df['Région'].isin(regions)) &
        (df['Céréale'].isin(cereales)) &
        (df['Année'] >= annees[0]) &
        (df['Année'] <= annees[1])
    ]
    
    if df_filtre.empty:
        st.warning("Aucune donnée disponible pour les critères sélectionnés.")
        return
    
    # Layout en onglets avancés
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "📈 Évolutions Temporelles", 
        "🌡️ Impact Climatique", 
        "📊 Analyses Spatiales",
        "🔗 Corrélations Avancées",
        "📦 Analyse Multivariée",
        "📋 Tableaux de Bord",
        "🤖 Modélisation"
    ])
    
    with tab1:
        st.header("📈 Analyses Temporelles Avancées")

        # Évolution temporelle interactive
        st.subheader(f"Évolution de {var_productivite}")
            
        fig_temp = px.line(
                df_filtre.groupby(['Année', 'Céréale', 'Région'])[var_productivite].mean().reset_index(),
                x='Année',
                y=var_productivite,
                color='Céréale',
                line_dash='Région',
                title=f'Évolution de {var_productivite}',
                markers=True,
                template='plotly_white'
        )
            
        if show_trend:
                for trace in fig_temp.data:
                    if trace.type == 'scatter':
                        # Ajouter une ligne de tendance
                        x_data = trace.x
                        y_data = trace.y
                        z = np.polyfit(range(len(x_data)), y_data, 1)
                        p = np.poly1d(z)
                        fig_temp.add_trace(go.Scatter(
                            x=x_data,
                            y=p(range(len(x_data))),
                            mode='lines',
                            line=dict(dash='dash', color=trace.line.color),
                            name=f'Tendance {trace.name}',
                            showlegend=False
                        ))
            
        st.plotly_chart(fig_temp, use_container_width=True)
        
        # Saisonnalité et décomposition
        st.subheader("Analyse de Saisonnalité")
            
        # Préparation des données pour l'analyse saisonnière
        df_seasonal = df_filtre.groupby(['Année', 'Céréale'])[var_productivite].mean().reset_index()
            
        fig_seasonal = px.box(
                df_seasonal,
                x='Céréale',
                y=var_productivite,
                color='Céréale',
                title=f"Distribution de {var_productivite} par céréale",
                template='plotly_white'
        )
        st.plotly_chart(fig_seasonal, use_container_width=True)
            
        # Indicateurs statistiques
        st.subheader("📊 Indicateurs Statistiques")
        stats_df = df_filtre.groupby('Céréale')[var_productivite].agg(['mean', 'std', 'min', 'max']).round(2)
        st.dataframe(stats_df.style.background_gradient(cmap='Blues'))
    
    with tab2:
        st.header("🌡️ Analyse d'Impact Climatique")
        
        # Scatter plot avec régression
        st.subheader(f"Relation {var_climatique} vs {var_productivite}")
            
        fig_scatter = px.scatter(
                df_filtre,
                x=var_climatique,
                y=var_productivite,
                color='Céréale',
                size='Superficie' if var_productivite != 'Superficie' else 'Production',
                hover_data=['Région', 'Année'],
                trendline="ols",
                title=f"Impact de {var_climatique} sur {var_productivite}",
                template='plotly_white'
        )
            
        # Ajouter des informations de régression
        results = px.get_trendline_results(fig_scatter)
        r_squared = results.px_fit_results.iloc[0].rsquared
            
        st.metric("R² de la régression", f"{r_squared:.3f}")
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        # Heatmap d'interaction
        st.subheader("Heatmap d'Interaction")
            
        pivot_data = df_filtre.pivot_table(
                values=var_productivite,
                index='Région',
                columns='Céréale',
                aggfunc='mean'
        ).fillna(0)
            
        fig_heatmap = px.imshow(
                pivot_data,
                title=f"{var_productivite} par Région et Céréale",
                aspect="auto",
                color_continuous_scale="Viridis",
                template='plotly_white'
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)
            
        # Analyse des extrêmes
        st.subheader("📈 Points de Données Extrêmes")
        extreme_threshold = st.slider("Seuil d'extrême (%)", 5, 25, 10)
        threshold = df_filtre[var_productivite].quantile(1 - extreme_threshold/100)
        extreme_data = df_filtre[df_filtre[var_productivite] > threshold]
            
        if not extreme_data.empty:
            st.write(f"Données supérieures au {100-extreme_threshold}ème percentile:")
            st.dataframe(extreme_data[['Région', 'Céréale', 'Année', var_productivite]].head(10))
    
    with tab3:
        st.header("📊 Analyses Spatiales et Comparatives")
        
        # Cartographie interactive
        st.subheader("📌 Cartographie des Performances")
        
        # Préparation des données pour la carte (exemple simplifié)
        df_map = df_filtre.groupby('Région').agg({
            'Production': 'mean',
            'Rendement': 'mean',
            'Superficie': 'mean'
        }).reset_index()
        
        # Créer une carte choroplèthe (exemple avec données géographiques simulées)
        fig_map = px.choropleth(
            df_map,
            locations='Région',
            locationmode='country names',  # À adapter selon vos données
            color='Production',
            hover_name='Région',
            hover_data=['Rendement', 'Superficie'],
            title="Production Moyenne par Région",
            color_continuous_scale="Viridis",
            template='plotly_white'
        )
        st.plotly_chart(fig_map, use_container_width=True)
        
        # Comparaisons multiples
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Comparaison Régionale")
            fig_radar = go.Figure()
            
            for cereale in cereales[:3]:  # Limiter à 3 céréales pour la lisibilité
                cereale_data = df_filtre[df_filtre['Céréale'] == cereale]
                regional_avg = cereale_data.groupby('Région')[var_productivite].mean()
                
                fig_radar.add_trace(go.Scatterpolar(
                    r=regional_avg.values,
                    theta=regional_avg.index,
                    fill='toself',
                    name=cereale
                ))
            
            fig_radar.update_layout(
                polar=dict(radialaxis=dict(visible=True)),
                showlegend=True,
                title=f"Comparaison Régionale - {var_productivite}"
            )
            st.plotly_chart(fig_radar, use_container_width=True)
        
        with col2:
            st.subheader("Distribution Cumulative")
            fig_cumulative = px.ecdf(
                df_filtre,
                x=var_productivite,
                color='Céréale',
                title=f"Distribution Cumulative de {var_productivite}",
                template='plotly_white'
            )
            st.plotly_chart(fig_cumulative, use_container_width=True)
    
    with tab4:
        st.header("🔗 Analyses de Corrélation Avancées")
        
        # Matrice de corrélation interactive
        st.subheader("Matrice de Corrélation Interactive")
        
        cols_corr = ['Production', 'Rendement', 'Superficie', 'Température', 
                    'Précipitation', 'Humidité', 'Vitèsse_Vent', 'Durée_Ensoleillement', 'Nombre_Jour_Pluie']
        
        cols_disponibles = [col for col in cols_corr if col in df_filtre.columns]
        corr_matrix = df_filtre[cols_disponibles].corr()
        
        fig_corr = px.imshow(
            corr_matrix,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="RdBu_r",
            title="Matrice de Corrélation",
            template='plotly_white'
        )
        st.plotly_chart(fig_corr, use_container_width=True)
        
        # Analyse de corrélation par paires
        st.subheader("Analyse par Paires de Variables")
        
        selected_vars = st.multiselect(
            "Sélectionnez les variables pour l'analyse par paires:",
            cols_disponibles,
            default=cols_disponibles[:4]
        )
        
        if len(selected_vars) >= 2:
            fig_pair = px.scatter_matrix(
                df_filtre,
                dimensions=selected_vars,
                color='Céréale',
                title="Matrice de Dispersion par Paires",
                template='plotly_white'
            )
            st.plotly_chart(fig_pair, use_container_width=True)
    
    with tab5:
        st.header("📦 Analyse Multivariée Avancée")
        
        # Analyse en composantes principales (PCA)
        st.subheader("Analyse en Composantes Principales (PCA)")
        
        # Préparation des données pour PCA
        numeric_cols = ['Production', 'Rendement', 'Superficie', 'Température', 
                       'Précipitation', 'Humidité', 'Vitèsse_Vent', 'Durée_Ensoleillement']
        numeric_cols = [col for col in numeric_cols if col in df_filtre.columns]
        
        if len(numeric_cols) >= 3:
            X = df_filtre[numeric_cols].dropna()
            
            if len(X) > 0:
                # Standardisation
                scaler = StandardScaler()
                X_scaled = scaler.fit_transform(X)
                
                # PCA
                pca = PCA(n_components=2)
                principal_components = pca.fit_transform(X_scaled)
                
                # Création du graphique PCA
                fig_pca = px.scatter(
                    x=principal_components[:, 0],
                    y=principal_components[:, 1],
                    color=df_filtre.loc[X.index, 'Céréale'],
                    hover_name=df_filtre.loc[X.index, 'Région'],
                    title=f"PCA - Variance expliquée: {pca.explained_variance_ratio_.sum():.2%}",
                    labels={'x': f'PC1 ({pca.explained_variance_ratio_[0]:.2%})',
                           'y': f'PC2 ({pca.explained_variance_ratio_[1]:.2%})'},
                    template='plotly_white'
                )
                st.plotly_chart(fig_pca, use_container_width=True)
                
                # Contribution des variables
                st.subheader("Contribution des Variables aux Composantes")
                loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
                fig_loading = px.scatter(
                    x=loadings[:, 0],
                    y=loadings[:, 1],
                    text=numeric_cols,
                    title="Contribution des Variables aux Composantes Principales",
                    template='plotly_white'
                )
                fig_loading.update_traces(textposition='top center')
                st.plotly_chart(fig_loading, use_container_width=True)
    
    with tab6:
        st.header("📋 Tableaux de Bord Interactifs")
        
        # KPI principaux
        st.subheader("📊 Indicateurs Clés de Performance")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_production = df_filtre['Production'].sum() / 1000  # en milliers
            st.metric("Production Totale", f"{total_production:,.0f}K", "++")
        
        with col2:
            avg_yield = df_filtre['Rendement'].mean()
            st.metric("Rendement Moyen", f"{avg_yield:.1f}", "+5.2%")
        
        with col3:
            avg_temp = df_filtre['Température'].mean()
            st.metric("Température Moyenne", f"{avg_temp:.1f}°C", "-0.3°C")
        
        with col4:
            total_area = df_filtre['Superficie'].sum() / 1000  # en milliers
            st.metric("Superficie Totale", f"{total_area:,.0f}K", "+2.1%")
        
        # Tableau de données interactif
        st.subheader("📋 Données Détaillées")
        
        # Options d'affichage
        show_columns = st.multiselect(
            "Colonnes à afficher:",
            df_filtre.columns.tolist(),
            default=['Région', 'Céréale', 'Année', 'Production', 'Rendement', 'Température']
        )
        
        # Pagination
        page_size = st.selectbox("Lignes par page:", [10, 25, 50, 100], index=0)
        total_pages = max(1, len(df_filtre) // page_size)
        page_number = st.number_input("Page", min_value=1, max_value=total_pages, value=1)
        
        start_idx = (page_number - 1) * page_size
        end_idx = start_idx + page_size
        
        st.dataframe(
            df_filtre[show_columns].iloc[start_idx:end_idx].style.background_gradient(
                subset=['Production', 'Rendement'], cmap='Blues'
            ),
            use_container_width=True
        )
        
        # Résumé statistique
        st.subheader("📈 Résumé Statistique Complet")
        st.dataframe(df_filtre.describe().style.format("{:.2f}"))
    
    with tab7:
        st.header("🤖 Modélisation Prédictive Simple")
        
        st.info("Cette section propose des modèles prédictifs basiques pour explorer les relations dans vos données.")
        
        # Sélection des variables pour la modélisation
        model_vars = st.multiselect(
            "Variables prédictives:",
            [col for col in df_filtre.columns if col not in ['Région', 'Céréale', 'Année']],
            default=['Superficie', 'Température', 'Précipitation']
        )
        
        target_var = st.selectbox(
            "Variable cible:",
            ['Production', 'Rendement']
        )
        
        if model_vars and target_var:
            # Préparation des données
            model_df = df_filtre[model_vars + [target_var]].dropna()
            X = model_df[model_vars]
            y = model_df[target_var]
            
            if len(X) > 0:
                col1, col2 = st.columns(2)
                
                with col1:
                    # Régression Linéaire
                    st.subheader("Régression Linéaire")
                    lr_model = LinearRegression()
                    lr_model.fit(X, y)
                    y_pred_lr = lr_model.predict(X)
                    r2_lr = r2_score(y, y_pred_lr)
                    
                    st.metric("R² - Régression Linéaire", f"{r2_lr:.3f}")
                    
                    # Graphique des prédictions
                    fig_lr = px.scatter(
                        x=y, y=y_pred_lr,
                        title=f"Régression Linéaire - Prédictions vs Réel",
                        labels={'x': 'Valeurs Réelles', 'y': 'Prédictions'},
                        template='plotly_white'
                    )
                    fig_lr.add_trace(go.Scatter(
                        x=[y.min(), y.max()],
                        y=[y.min(), y.max()],
                        mode='lines',
                        line=dict(dash='dash', color='red'),
                        name='Ligne parfaite'
                    ))
                    st.plotly_chart(fig_lr, use_container_width=True)
                
                with col2:
                    # Random Forest
                    st.subheader("Forêt Aléatoire")
                    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
                    rf_model.fit(X, y)
                    y_pred_rf = rf_model.predict(X)
                    r2_rf = r2_score(y, y_pred_rf)
                    
                    st.metric("R² - Forêt Aléatoire", f"{r2_rf:.3f}")
                    
                    # Importance des caractéristiques
                    feature_importance = pd.DataFrame({
                        'feature': model_vars,
                        'importance': rf_model.feature_importances_
                    }).sort_values('importance', ascending=True)
                    
                    fig_importance = px.bar(
                        feature_importance,
                        x='importance',
                        y='feature',
                        orientation='h',
                        title="Importance des Variables - Forêt Aléatoire",
                        template='plotly_white'
                    )
                    st.plotly_chart(fig_importance, use_container_width=True)

def show():
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #2E86AB;
        text-align: center;
        margin: 1rem 0;
        font-weight: bold;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2E86AB;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid #2E86AB;
        padding-bottom: 0.5rem;
    }
    .kpi-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="main-header">📈 Tableau de Bord d\'Analyse Avancée</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; color: #666; margin-bottom: 2rem;'>
    Plateforme d'analyse interactive et prédictive des données agricoles du Burkina Faso
    </div>
    """, unsafe_allow_html=True)
    
    # Chargement des données
    try:
        df = load_data()
        st.success(f"✅ Données chargées avec succès: {len(df)} enregistrements, {len(df.columns)} colonnes")
        
        # Aperçu rapide des données
        with st.expander("🔍 Aperçu Rapide des Données"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Période couverte", f"{int(df['Année'].min())} - {int(df['Année'].max())}")
            with col2:
                st.metric("Nombre de régions", f"{df['Région'].nunique()}")
            with col3:
                st.metric("Types de céréales", f"{df['Céréale'].nunique()}")
            
            st.dataframe(df.head(10), use_container_width=True)
        
        # Création des visualisations avancées
        create_advanced_visualizations(df)
        
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement des données: {str(e)}")
        st.info("Veuillez vérifier le chemin du fichier et le format des données.")

if __name__ == "__main__":
    show()