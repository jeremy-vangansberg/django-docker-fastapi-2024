# Application Full-Stack Django + FastAPI + PostgreSQL

Une application moderne utilisant une architecture microservices avec Django pour le frontend, FastAPI pour l'API, et PostgreSQL comme base de données.

## 🏗 Architecture

Le projet est composé de trois services principaux orchestrés avec Docker Compose :

### 🌐 Frontend (Django)
- Port : 8001
- Framework web complet avec interface utilisateur
- Utilise Django Tailwind pour le style
- Gestion des templates et des assets statiques
- Support de l'authentification et des sessions

### 🚀 API (FastAPI)
- Port : 8002
- API RESTful haute performance
- Intégration de modèles scikit-learn
- Documentation automatique des endpoints
- Optimisé pour les prédictions ML

### 💾 Base de données (PostgreSQL)
- Port : 5432
- Stockage persistant
- Volumes Docker pour la persistance des données
- Compatible avec Django ORM

## ⚙️ Prérequis

- Docker & Docker Compose
- Python 3.x
- Node.js (pour Tailwind CSS)

## 📦 Dépendances principales

### Frontend (Django)
- Django < 5.0
- django-tailwind
- django-widget-tweaks
- whitenoise
- psycopg2-binary
- gunicorn

### API (FastAPI)
- FastAPI < 1.0
- scikit-learn 1.4.0
- uvicorn < 1.0

## 🚀 Installation

1. Cloner le repository :
```bash
git clone [url-du-repo]
cd [nom-du-projet]
```

2. Configuration de l'environnement :
```bash
# Créer le fichier .env dans le dossier web/
cp web/.env.example web/.env
# Configurer les variables d'environnement nécessaires
```

3. Lancer les conteneurs :
```bash
docker-compose up -d
```

## 📂 Structure du projet

```
.
├── api/                    # Service FastAPI
│   ├── main.py            # Point d'entrée API
│   ├── api.py             # Définition des routes
│   ├── model.pkl          # Modèle ML pré-entraîné
│   └── requirements.txt   # Dépendances Python
├── web/                   # Service Django
│   ├── main/             # Application principale
│   ├── templates/        # Templates HTML
│   ├── static/           # Fichiers statiques
│   ├── theme/            # Configuration Tailwind
│   └── requirements.txt  # Dépendances Python
└── docker-compose.yaml    # Configuration Docker
```

## 🛠 Développement

- Hot-reload activé pour Django et FastAPI
- Les modifications du code sont automatiquement reflétées
- Tailwind CSS en mode JIT pour le développement
- Volumes Docker configurés pour le développement local

## 🔗 URLs importantes

- Frontend : http://localhost:8001
- API : http://localhost:8002/docs
- Base de données : postgresql://localhost:5432

## 📝 Scripts utiles

```bash
# Démarrer tous les services
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter tous les services
docker-compose down

# Reconstruire les images
docker-compose build
```

## 🔒 Sécurité

- Variables d'environnement pour les secrets
- CORS configuré pour la sécurité
- Whitenoise pour servir les fichiers statiques
- PostgreSQL avec authentification