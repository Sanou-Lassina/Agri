#!/bin/bash
# ==========================================================
# 🚀 Script d'installation et de lancement pour Agri Analytics BF
# ==========================================================

echo "=========================================="
echo "🌾 Bienvenue sur AGRI ANALYTICS BF Setup"
echo "=========================================="
sleep 1

# Vérification de Python
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 n'est pas installé. Installe-le avant de continuer."
    exit 1
else
    echo "✅ Python3 détecté."
fi

# Création d'un environnement virtuel
echo "📦 Création de l'environnement virtuel 'venv'..."
python3 -m venv venv

# Activation de l'environnement virtuel
echo "⚙️ Activation de l'environnement virtuel..."
source venv/bin/activate

# Mise à jour de pip
echo "⬆️ Mise à jour de pip..."
pip install --upgrade pip

# Installation des dépendances
if [ -f "requirements.txt" ]; then
    echo "📥 Installation des dépendances depuis requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ Aucun fichier requirements.txt trouvé."
    exit 1
fi

# Lancement de l'application Streamlit
echo "🚀 Lancement de l'application Streamlit..."
streamlit run app.py

# Fin du script
echo "=========================================="
echo "✅ Installation et lancement terminés."
echo "🌱 Profite de AGRI ANALYTICS BF !"
echo "=========================================="