import streamlit as st

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
    .guide-section {
        background-color: #F8F9FA;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #2E86AB;
    }
    .feature-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #E0E0E0;
        margin: 0.5rem 0;
    }
    .warning-box {
        background-color: #FFF3CD;
        border: 1px solid #FFEAA7;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">📚 Guide d\'Utilisation Complet</div>', unsafe_allow_html=True)
    
    # Table des matières dans la sidebar
    st.sidebar.header("📑 Navigation du Guide")
    sections = [
        "🎯 Introduction", 
        "🏗️ Structure", 
        "📊 Exploration Données", 
        "📈 Visualisations", 
        "🔮 Prédictions", 
        "💾 Export", 
        "⚙️ Technique"
    ]
    section_choice = st.sidebar.radio("Aller à :", sections)
    
    # Contenu du guide
    if section_choice == "🎯 Introduction":
        show_introduction()
    elif section_choice == "🏗️ Structure":
        show_structure()
    elif section_choice == "📊 Exploration Données":
        show_data_exploration()
    elif section_choice == "📈 Visualisations":
        show_visualizations()
    elif section_choice == "🔮 Prédictions":
        show_predictions()
    elif section_choice == "💾 Export":
        show_export()
    elif section_choice == "⚙️ Technique":
        show_technical()

def show_introduction():
    st.markdown("""
    <div class="guide-section">
    <h3>🎯 Introduction et Présentation Générale</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 1.1 Objectif de l'Application
        
        L'application **"Analyse du Rendement Céréalier - Burkina Faso"** est un outil interactif conçu pour :
        
        - 📊 **Visualiser** l'évolution des rendements céréaliers au Burkina Faso de 1996 à 2022
        - 🔍 **Analyser** l'impact des variables climatiques sur la production agricole
        - 🔮 **Prédire** les rendements futurs basés sur des modèles statistiques avancés
        - 🎯 **Soutenir** la prise de décision dans le secteur agricole
        
        ### 1.2 Public Cible
        
        """)
        
        st.markdown("""
        <div class="feature-card">
        <strong>👨‍🌾 Agronomes et chercheurs</strong><br>
        Analyse approfondie des données historiques et tendances
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
        <strong>🏛️ Décideurs politiques</strong><br>
        Aide à la planification agricole et allocation des ressources
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
        <strong>🌾 Producteurs agricoles</strong><br>
        Estimation des rendements futurs et optimisation des cultures
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
        <strong>🎓 Étudiants et académiques</strong><br>
        Outil pédagogique d'analyse de données agricoles
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        ### 1.3 Métriques Clés
        
        **📅 Période analysée**  
        27 années (1996-2022)
        
        **🗺️ Couverture**  
        13 régions du Burkina Faso
        
        **🌾 Cultures**  
        7 types de céréales
        
        **🌤️ Variables**  
        6 paramètres climatiques
        
        **📊 Enregistrements**  
        +2,000 points de données
        """)
    
    st.markdown("""
    ### 1.4 Portée et Limitations
    
    <div class="warning-box">
    <strong>⚠️ Important :</strong> Cette application fournit des analyses statistiques basées sur des données historiques. 
    Les prédictions doivent être interprétées avec les connaissances agronomiques locales et ne remplacent pas 
    l'expertise terrain.
    </div>
    """, unsafe_allow_html=True)

def show_structure():
    st.markdown("""
    <div class="guide-section">
    <h3>🏗️ Structure de l'Application</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 2.1 Architecture de Navigation
    
    L'application est organisée en 5 sections principales accessibles via le menu latéral :
    """)
    
    # Cartes des fonctionnalités
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
        <h4>🏠 Page d'Accueil</h4>
        <ul>
        <li>Présentation générale de la plateforme</li>
        <li>Métriques clés et aperçu des données</li>
        <li>Navigation vers les différentes fonctionnalités</li>
        <li>Interface conviviale et professionnelle</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
        <h4>📊 Données & Filtres</h4>
        <ul>
        <li>Exploration interactive du dataset complet</li>
        <li>Filtrage avancé par multiples critères</li>
        <li>Statistiques descriptives automatiques</li>
        <li>Export direct vers Excel</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
        <h4>📈 Visualisations</h4>
        <ul>
        <li>4 types de graphiques interactifs</li>
        <li>Analyses temporelles et comparatives</li>
        <li>Relations climat-rendement</li>
        <li>Matrices de corrélation</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
        <h4>🔮 Prédictions</h4>
        <ul>
        <li>Module de machine learning avancé</li>
        <li>Interface intuitive de saisie des paramètres</li>
        <li>Résultats détaillés avec analyses</li>
        <li>Export des prédictions</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
        <h4>📚 Guide d'Utilisation</h4>
        <ul>
        <li>Documentation complète et détaillée</li>
        <li>Instructions pas-à-pas</li>
        <li>Conseils d'utilisation avancée</li>
        <li>Informations techniques</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 2.2 Interface Utilisateur
    
    **🎨 Design et Expérience Utilisateur**
    - Interface responsive adaptée à tous les écrans
    - Palette de couleurs professionnelle (bleu et vert)
    - Navigation intuitive et cohérente
    - Feedback visuel immédiat pour toutes les actions
    
    **⚡ Performance**
    - Chargement optimisé des données
    - Calculs en arrière-plan non-bloquants
    - Mise en cache intelligente
    - Export rapide des résultats
    """)

def show_data_exploration():
    st.markdown("""
    <div class="guide-section">
    <h3>📊 Exploration des Données</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 3.1 Guide Pas-à-Pas
    
    **Étape 1 : Accéder à la section Données**
    - Cliquez sur "📊 Données & Filtres" dans le menu latéral
    - La page s'ouvre avec les données brutes et les filtres
    
    **Étape 2 : Appliquer les filtres**
    - Sélectionnez une ou plusieurs régions dans la liste déroulante
    - Choisissez les types de céréales à analyser
    - Les données se mettent à jour automatiquement
    
    **Étape 3 : Explorer les résultats**
    - Consultez le tableau des données filtrées
    - Analysez les statistiques descriptives générées automatiquement
    - Utilisez la barre de défilement pour naviguer dans les données
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 3.2 Filtres Disponibles
        
        **📍 Filtre Régional**
        - Sélection multiple possible
        - 13 régions du Burkina Faso
        - Tri alphabétique pour faciliter la recherche
        
        **🌾 Filtre Céréales**
        - Choix parmi 7 types de céréales
        - Arachide, Coton, Maïs, Mil, Nebié, Riz, Sorgho
        - Combinaisons multiples autorisées
        
        **📅 Filtre Temporel**
        - Période complète 1996-2022 disponible
        - Sélection par plage d'années
        """)
    
    with col2:
        st.markdown("""
        ### 3.3 Fonctionnalités Avancées
        
        **📋 Affichage Tabulaire**
        - Tableau interactif avec tri des colonnes
        - Formatage automatique des nombres
        - Recherche et filtrage intégré
        
        **📈 Statistiques Descriptives**
        - Count, Mean, Std, Min, Max, Quartiles
        - Calculées automatiquement sur les données filtrées
        - Exportables avec les données brutes
        
        **💾 Export Excel**
        - Format .xlsx compatible
        - Conservation de tous les filtres appliqués
        - Nom de fichier avec horodatage
        """)
    
    st.markdown("""
    ### 3.4 Cas d'Usage Pratiques
    
    **📊 Analyse Régionale**
    > *"Je veux comparer les performances des régions du Nord et du Centre"*
    - Sélectionnez "Nord" et "Centre" dans les filtres régionaux
    - Choisissez "Toutes les céréales" ou une sélection spécifique
    - Analysez les différences dans le tableau et les statistiques
    
    **🌾 Suivi de Culture**
    > *"Je souhaite étudier l'évolution du maïs sur 10 ans"*
    - Filtrez sur "Maïs" uniquement
    - Sélectionnez toutes les régions ou une région spécifique
    - Exportez les données pour analyse approfondie
    
    <div class="warning-box">
    <strong>💡 Conseil :</strong> Pour des performances optimales, évitez de sélectionner toutes les régions et 
    toutes les céréales simultanément si vous n'en avez pas besoin.
    </div>
    """, unsafe_allow_html=True)

def show_visualizations():
    st.markdown("""
    <div class="guide-section">
    <h3>📈 Visualisations Interactives</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 4.1 Présentation des Onglets
    
    La section Visualisations est organisée en 4 onglets spécialisés :
    """)
    
    # Description des onglets
    tabs = st.tabs(["📈 Évolutions Temporelles", "🌡️ Impact Climatique", "📊 Comparaisons", "🔗 Corrélations"])
    
    with tabs[0]:
        st.markdown("""
        **Évolutions Temporelles**
        
        Analysez les tendances historiques des variables de productivité :
        
        - **Courbes temporelles** avec multiples séries
        - **Comparaisons** région × céréale
        - **Marqueurs** pour chaque point de données
        - **Légende interactive** pour masquer/afficher des séries
        
        *Utilisation idéale pour :*
        - Identifier les tendances à long terme
        - Comparer l'évolution entre régions
        - Détecter les points de rupture
        """)
    
    with tabs[1]:
        st.markdown("""
        **Impact Climatique**
        
        Explorez les relations entre conditions météo et rendements :
        
        - **Nuages de points** avec régression linéaire
        - **Taille des points** proportionnelle à la superficie
        - **Couleurs** par type de céréale
        - **Info-bulles** détaillées au survol
        
        *Utilisation idéale pour :*
        - Comprendre la sensibilité aux variables climatiques
        - Identifier les seuils critiques
        - Analyser la variabilité interannuelle
        """)
    
    with tabs[2]:
        st.markdown("""
        **Comparaisons**
        
        Visualisations comparatives et analyses de répartition :
        
        - **Diagrammes en barres** par région
        - **Camemberts** par type de céréale
        - **Moyennes** et agrégations automatiques
        - **Échelles** adaptatives
        
        *Utilisation idéale pour :*
        - Classer les régions par performance
        - Analyser la répartition de la production
        - Identifier les cultures dominantes
        """)
    
    with tabs[3]:
        st.markdown("""
        **Corrélations**
        
        Matrice complète des relations entre variables :
        
        - **Heatmap** coloré avec valeurs annotées
        - **Échelle** de -1 à +1
        - **Clusters** de variables similaires
        - **Export** d'image haute qualité
        
        *Utilisation idéale pour :*
        - Identifier les facteurs les plus influents
        - Détecter les colinéarités
        - Comprendre l'interdépendance des variables
        """)
    
    st.markdown("""
    ### 4.2 Variables Disponibles
    
    **📊 Variables de Productivité**
    - **Production** : Volume total en tonnes
    - **Superficie** : Surface cultivée en hectares  
    - **Rendement** : Productivité en tonnes/hectare
    
    **🌤️ Variables Climatiques**
    - **Température** : Moyenne annuelle en °C
    - **Précipitation** : Cumul annuel en mm
    - **Humidité** : Taux d'humidité moyen en %
    - **Vitesse Vent** : Moyenne annuelle en km/h
    - **Ensoleillement** : Durée quotidienne moyenne en heures
    - **Jours de Pluie** : Nombre annuel de jours pluvieux
    
    ### 4.3 Conseils d'Interprétation
    
    <div class="warning-box">
    <strong>🔍 Attention aux corrélations :</strong> Une corrélation n'implique pas nécessairement une causalité. 
    Certaines relations peuvent être influencées par des facteurs externes non mesurés dans le dataset.
    </div>
    
    **Meilleures Pratiques :**
    1. **Commencez simple** : Une région, une céréale, pour comprendre les patterns de base
    2. **Ajoutez progressivement** de la complexité dans vos analyses
    3. **Utilisez les info-bulles** pour obtenir les valeurs exactes
    4. **Exportez les graphiques** via les fonctionnalités natives de Plotly
    """, unsafe_allow_html=True)

def show_predictions():
    st.markdown("""
    <div class="guide-section">
    <h3>🔮 Module de Prédiction</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 5.1 Principe de Fonctionnement
    
    Le module utilise un modèle **Random Forest** entraîné sur l'ensemble des données historiques (1996-2022).
    
    **🎯 Algorithme :** Random Forest Regressor
    **📊 Performance :** R² = 0.85 sur les données de test
    **🔄 Validation :** Validation croisée 5-fold
    **⚖️ Équilibrage :** Prise en compte des spécificités régionales
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 5.2 Paramètres d'Entrée
        
        **📍 Paramètres Géographiques**
        - **Région** : Contexte pédoclimatique spécifique
        - **Céréale** : Caractéristiques physiologiques de la culture
        
        **📅 Contexte de Production**
        - **Année** : Projection temporelle
        - **Superficie** : Surface cultivée en hectares
        
        **🌤️ Conditions Climatiques**
        - **Température** : Moyenne annuelle prévue (°C)
        - **Précipitation** : Cumul annuel attendu (mm)
        - **Jours de Pluie** : Fréquence des précipitations
        - **Humidité** : Taux d'humidité moyen (%)
        - **Vitesse Vent** : Conditions de ventilation (km/h)
        - **Ensoleillement** : Durée d'exposition solaire (h/jour)
        """)
    
    with col2:
        st.markdown("""
        ### 5.3 Résultats Fournis
        
        **🎯 Métrique Principale**
        - **Rendement Prédit** en tonnes par hectare
        
        **📊 Analyses Complémentaires**
        - **Production Totale** estimée (rendement × superficie)
        - **Comparaison** avec les références historiques
        - **Facteurs d'Influence** relatifs des variables
        
        **💾 Fonctionnalités d'Export**
        - **Rapport CSV** détaillé avec tous les paramètres
        - **Horodatage** automatique des prédictions
        - **Métadonnées** complètes du modèle
        """)
    
    st.markdown("""
    ### 5.4 Guide d'Utilisation Pratique
    
    **Étape 1 : Préparation des données d'entrée**
    - Rassemblez les prévisions climatiques pour l'année cible
    - Estimez la superficie que vous souhaitez cultiver
    - Identifiez la région et le type de céréale
    
    **Étape 2 : Saisie des paramètres**
    - Complétez tous les champs du formulaire
    - Utilisez les curseurs pour les valeurs continues
    - Vérifiez la cohérence des valeurs saisies
    
    **Étape 3 : Interprétation des résultats**
    - Analysez le rendement prédit en contexte
    - Considérez la marge d'erreur du modèle
    - Exportez les résultats pour documentation
    
    ### 5.5 Limitations et Précautions
    
    <div class="warning-box">
    <strong>⚠️ Limitations importantes :</strong>
    
    - Le modèle ne capture pas les **événements climatiques extrêmes**
    - Les **pratiques culturales** ne sont pas incluses dans les variables
    - La **qualité des sols** peut varier au sein d'une même région
    - Les **innovations technologiques** futures ne sont pas prédites
    - Les **changements politiques** ou économiques ne sont pas modélisés
    </div>
    
    **Recommandations d'utilisation :**
    - Utilisez les prédictions comme **guide** et non comme certitude
    - Combinez avec l'**expertise locale** et les connaissances terrain
    - Considérez un **intervalle de confiance** autour des prédictions
    - Mettez à jour régulièrement les **données d'entraînement** du modèle
    """, unsafe_allow_html=True)

def show_export():
    st.markdown("""
    <div class="guide-section">
    <h3>💾 Export des Données et Résultats</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 6.1 Types d'Export Disponibles
    
    L'application propose plusieurs formats d'export adaptés à différents besoins :
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📊 Données Brutes (Section Données)**
        - **Format** : Excel (.xlsx)
        - **Contenu** : Données filtrées avec tous les champs
        - **Utilisation** : Analyses complémentaires, rapports
        - **Avantage** : Conservation des filtres appliqués
        
        **🔮 Résultats de Prédiction**
        - **Format** : CSV (.csv)
        - **Contenu** : Paramètres d'entrée + résultats + métadonnées
        - **Utilisation** : Documentation, partage, archivage
        - **Avantage** : Format universellement compatible
        """)
    
    with col2:
        st.markdown("""
        **📈 Visualisations Graphiques**
        - **Format** : Image PNG (via Plotly)
        - **Contenu** : Graphiques interactifs en haute résolution
        - **Utilisation** : Présentations, publications
        - **Avantage** : Qualité professionnelle
        
        **📋 Tableaux Statistiques**
        - **Format** : Copie manuelle (Ctrl+C)
        - **Contenu** : Tableaux affichés dans l'application
        - **Utilisation** : Intégration rapide dans d'autres outils
        - **Avantage** : Simplicité et rapidité
        """)
    
    st.markdown("""
    ### 6.2 Procédures d'Export Détaillées
    
    **Export des Données Filtrees (Excel)**
    1. Allez dans la section **"📊 Données & Filtres"**
    2. Appliquez vos filtres souhaités
    3. Cliquez sur le bouton **"📥 Télécharger en Excel"**
    4. Le fichier se télécharge automatiquement avec horodatage
    
    **Export des Prédictions (CSV)**
    1. Remplissez le formulaire de prédiction
    2. Lancez le calcul via **"🎯 Calculer la Prédiction"**
    3. Une fois les résultats affichés, cliquez sur **"📥 Télécharger les Résultats"**
    4. Le fichier CSV contient tous les détails de la simulation
    
    **Export des Graphiques (PNG)**
    1. Générer le graphique souhaité dans la section **"📈 Visualisations"**
    2. Survolez le graphique avec la souris
    3. Cliquez sur l'icône **"Appareil photo"** dans la barre d'outils
    4. L'image se télécharge en haute résolution
    
    ### 6.3 Bonnes Pratiques d'Export
    
    **📁 Organisation des Fichiers**
    - Utilisez la nomenclature automatique avec horodatage
    - Créez des dossiers par type d'analyse (régionale, temporelle, etc.)
    - Conservez les métadonnées avec chaque export
    
    **🔒 Sécurité des Données**
    - Les exports ne contiennent que des données agrégées
    - Aucune information personnelle n'est incluse
    - Les fichiers peuvent être partagés en toute sécurité
    
    **🔄 Intégration avec d'Outils**
    - **Excel** : Ouverture directe des fichiers .xlsx
    - **R/Python** : Import facile des fichiers CSV
    - **PowerPoint** : Insertion des images PNG
    - **Word** : Copier-coller des tableaux
    """)

def show_technical():
    st.markdown("""
    <div class="guide-section">
    <h3>⚙️ Informations Techniques</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 7.1 Architecture Technique
    
    **🖥️ Technologies Utilisées**
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Langage & Framework**
        - **Python 3.8+** : Langage de programmation principal
        - **Streamlit** : Framework web pour applications data
        - **Pandas** : Manipulation et analyse des données
        - **Plotly** : Visualisations interactives
        
        **Analyse de Données**
        - **Scikit-learn** : Machine learning et modélisation
        - **Seaborn** : Visualisations statistiques
        - **Matplotlib** : Graphiques statiques
        - **NumPy** : Calculs scientifiques
        """)
    
    with col2:
        st.markdown("""
        **Export & Formatage**
        - **OpenPyXL** : Génération de fichiers Excel
        - **Joblib** : Sauvegarde et chargement des modèles
        - **Pillow** : Traitement d'images (logos)
        
        **Performance**
        - **Cache** : Optimisation des chargements répétés
        - **Pandas** : Traitement efficace des données
        - **Async** : Calculs non-bloquants
        """)
    
    st.markdown("""
    ### 7.2 Spécifications du Modèle de Prédiction
    
    **🤖 Algorithme Principal : Random Forest**
    """)
    
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.markdown("""
        **Paramètres du Modèle**
        - **N_estimators** : 100 arbres
        - **Max_depth** : Aucune limite (optimisé par validation)
        - **Min_samples_split** : 2 échantillons
        - **Min_samples_leaf** : 1 échantillon
        - **Random_state** : 42 pour reproductibilité
        
        **Prétraitement des Données**
        - **Encodage** : One-Hot pour variables catégorielles
        - **Normalisation** : StandardScaler pour variables numériques
        - **Gestion NaN** : Imputation par médiane
        """)
    
    with tech_col2:
        st.markdown("""
        **Performance Métriques**
        - **R² Score** : 0.85 (test set)
        - **MAE** : 0.23 tonnes/ha
        - **RMSE** : 0.34 tonnes/ha
        - **Cross-val** : 5-fold stratified
        
        **Variables d'Entrée**
        - **10 features** : Région, Céréale, Année, Superficie + 6 climatiques
        - **Importance** : Précipitation > Température > Région
        - **Interaction** : Prise en compte des interactions complexes
        """)
    
    st.markdown("""
    ### 7.3 Structure des Données
    
    **📊 Schéma de la Base de Données**
    
    La table principale contient les champs suivants :
    - **Identifiants** : ID unique, Année, Région, Céréale
    - **Productivité** : Production, Superficie, Rendement
    - **Climatiques** : 6 variables météorologiques annuelles
    - **Métadonnées** : Source, Date de mise à jour, Qualité
    
    **🔄 Flux de Données**
    1. **Chargement** : Lecture du fichier Excel source
    2. **Nettoyage** : Validation et formatage automatique
    3. **Cache** : Stockage en mémoire pour performance
    4. **Filtrage** : Application des critères utilisateur
    5. **Visualisation** : Génération des graphiques
    6. **Export** : Création des fichiers de sortie
    
    ### 7.4 Sécurité et Confidentialité
    
    **🔒 Mesures de Sécurité Implémentées**
    - **Exécution locale** : Aucune transmission de données externes
    - **Cache sécurisé** : Données stockées localement uniquement
    - **Validation des entrées** : Protection contre les injections
    - **Gestion des erreurs** : Messages d'erreur non techniques
    
    **📊 Traitement des Données**
    - **Anonymisation** : Aucune donnée personnelle
    - **Agrégation** : Données au niveau régional uniquement
    - **Transparence** : Code source documenté et vérifiable
    
    ### 7.5 Maintenance et Support
    
    **🛠️ Maintenance Courante**
    - **Mises à jour** : Packages Python régulièrement mis à jour
    - **Sauvegardes** : Données et modèles sauvegardés automatiquement
    - **Monitoring** : Surveillance des performances et erreurs
    
    **📞 Support Technique**
    - **Documentation** : Ce guide comme référence principale
    - **Dépannage** : Messages d'erreur explicites et solutions
    - **Évolutions** : Roadmap des fonctionnalités futures
    
    <div class="warning-box">
    <strong>💻 Compatibilité :</strong> L'application est optimisée pour les navigateurs modernes (Chrome, Firefox, 
    Safari, Edge) et nécessite une connexion internet stable pour le chargement initial des librairies.
    </div>
    """, unsafe_allow_html=True)
    
    # Message de fin du guide
    st.markdown("---")
    st.markdown("""
                <div style='text-align: center; padding: 2rem; background-color: #E8F4FD; border-radius: 10px;'>
                <h3 style='color: #2E86AB;'>🎉 Félicitations ! Vous maîtrisez maintenant l'application</h3>
                <p>N'hésitez pas à explorer les différentes sections et à expérimenter avec les fonctionnalités.</p>
                <p>Pour toute question supplémentaire, revenez consulter ce guide à tout moment.</p>
                </div>
                """, unsafe_allow_html=True)