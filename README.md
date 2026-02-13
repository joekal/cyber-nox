# CYBER-NOX — Cybersécurité & Innovation Digitale

Bienvenue sur le dépôt officiel de **CYBER-NOX**, votre partenaire de confiance en RDC pour la transformation numérique, la cybersécurité avancée et le développement web de pointe.

## 📋 Vue d'ensemble

CYBER-NOX propose deux pôles complémentaires :

### 🔐 Pôle Cybersécurité
- **Audits & Pentests** : Tests d'intrusion (Black/White box) et audit d'infrastructure
- **Protection des Données** : Mise en place de politiques de sécurité strictes et conformité aux normes internationales
- **Formation & Sensibilisation** : Formation des équipes pour renforcer le « pare-feu humain »

### 💻 Pôle Développement Digital
- **Applications Web & Mobile** : Développement sur mesure (React, Django, Flutter)
- **Branding Numérique** : CV digitaux, portfolios interactifs, identités visuelles
- **Régie IT (Outsourcing)** : Mise à disposition de développeurs qualifiés

---

## 🚀 Démarrage rapide

### Prérequis

- Python 3.8+
- Django 4.2.26
- pip (ou conda)
- Git

### Installation locale

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/joekal/cyber-nox.git
   cd cyber-nox
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install django==4.2.26
   ```

4. **Configurer les variables d'environnement**
   
   Créez un fichier `.env` à la racine du projet (`cybernox_project/`) :
   ```bash
   cd cybernox_project
   cat > .env <<EOF
   DJANGO_SECRET_KEY=votre_clé_secrète_production
   EMAIL_HOST_USER=votre_email@gmail.com
   EMAIL_HOST_PASSWORD=votre_mot_de_passe_app
   EOF
   ```

   **Note** : L'application charge automatiquement le fichier `.env` via un lecteur personnalisé dans `settings.py`. Aucune dépendance `python-dotenv` requise.

5. **Appliquer les migrations**
   ```bash
   python manage.py migrate
   ```

6. **Créer un superutilisateur (admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Démarrer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

   Accédez à http://127.0.0.1:8000/

---

## 📁 Structure du projet

```
cyber-nox/
├── cybernox_project/          # Dossier Django
│   ├── cybernox_project/      # Configuration du projet
│   │   ├── settings.py        # Paramètres Django (inclut le loader .env)
│   │   ├── urls.py            # Routage principal
│   │   ├── wsgi.py            # Configuration WSGI
│   │   └── asgi.py            # Configuration ASGI
│   ├── website/               # Application Django principale
│   │   ├── models.py          # Modèles (Service, TeamMember, Project, ContactMessage)
│   │   ├── views.py           # Vues (vue home avec envoi d'email)
│   │   ├── admin.py           # Admin Django
│   │   ├── migrations/        # Migrations de base de données
│   │   └── templates/
│   │       └── website/
│   │           └── index.html # Template principal (Tailwind CSS)
│   ├── static/
│   │   └── img/               # Images statiques
│   ├── .env                   # Variables d'environnement (À créer)
│   ├── db.sqlite3             # Base de données SQLite
│   └── manage.py              # Commandes Django
├── README.md                  # Ce fichier
└── .gitignore                 # Fichiers à ignorer dans Git
```

---

## ⚙️ Configuration

### Paramètres Django principaux (`settings.py`)

- **`DEBUG = True`** : Mode développement (à changer en `False` en production)
- **`ALLOWED_HOSTS = []`** : À configurer pour votre domaine en production
- **Base de données** : SQLite par défaut (adapter pour PostgreSQL en production)
- **Email** : Configuré pour Gmail SMTP

### Email (Formulaire de contact)

La vue `home` dans `website/views.py` envoie automatiquement un email à **`kalalajonathan297@gmail.com`** quand le formulaire de contact est soumis.

**Configuration requise** :
- `EMAIL_HOST_USER` : Votre adresse Gmail
- `EMAIL_HOST_PASSWORD` : Mot de passe d'application Gmail (créé via [Paramètres Google](https://myaccount.google.com/apppasswords))

Variables lues depuis le fichier `.env` (aucune dépendance externe) via le loader personnalisé dans `settings.py`.

---

## 🔄 Flux de contact

1. Visiteur remplit le formulaire de contact sur la page d'accueil
2. Données sauvegardées dans la table `ContactMessage` de la base de données
3. Email envoyé à l'adresse configurée avec les détails du message
4. Message de succès affiché au visiteur

---

## 🎨 Template frontal

Le template `index.html` utilise :
- **Tailwind CSS** : Framework CSS utilitaire
- **Phosphor Icons** : Icônes modernes
- **Animations personnalisées** : Reveal, float, scroll spy
- **Responsive design** : Mobile-first

---

## 🗄️ Modèles de données

### `ContactMessage`
```python
- name : CharField (nom du visiteur)
- email : EmailField (email du visiteur)
- subject : CharField (sujet du message)
- message : TextField (contenu du message)
- created_at : DateTimeField (timestamp automatique)
```

### `Service`
```python
- title : CharField
- description : TextField
- category : CharField (CYBER ou DEV)
```

### `TeamMember`
```python
- name : CharField
- title : CharField
- bio : TextField
- image : ImageField
```

### `Project`
```python
- title : CharField
- description : TextField
- image : ImageField
- link : URLField (optionnel)
```

---

## 🛠️ Commandes utiles

```bash
# Démarrer le serveur
python manage.py runserver

# Créer les migrations après modification des modèles
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Accéder à l'admin Django
# http://127.0.0.1:8000/admin/

# Lancer les tests (s'il y en a)
python manage.py test

# Collecter les fichiers statiques (production)
python manage.py collectstatic --noinput
```

---

## 📤 Déploiement sur GitHub

### Pousser le code

```bash
cd /home/kalel/Documents/projet-cyber-nox

# Ajouter la remote (si pas déjà fait)
git remote add origin https://github.com/joekal/cyber-nox.git

# Renommer la branche en 'main'
git branch -M main

# Ajouter et committer
git add .
git commit -m "Initial commit — Cyber-NOX project"

# Pousser vers GitHub
git push -u origin main
```

### `.gitignore`

Le fichier `.gitignore` exclut automatiquement :
- Dossiers virtuels (`venv/`)
- Fichiers `.env` (secrets)
- `__pycache__/`, `*.pyc`
- `db.sqlite3` (données locales)
- Logs et fichiers IDE

---

## 🔐 Sécurité

⚠️ **Rappels importants** :

1. **Ne commitez jamais** de fichier `.env` contenant des secrets
2. **Changez `DEBUG = False`** en production
3. **Générez une nouvelle `SECRET_KEY`** unique en production
4. **Configurez `ALLOWED_HOSTS`** pour vos domaines
5. **Utilisez HTTPS** en production
6. **Sécurisez votre base de données** (PostgreSQL/MySQL pour la prod)

---

## 📝 Licence

Propriété de **CYBER-NOX**. Tous droits réservés.

---

## 📞 Contact

- **Email** : contact@cyber-nox.com
- **Localisation** : Kinshasa, RDC
- **Registre** : RCCM CD/KNG/RCCM/24-B-00000

---

## ✅ Checklist de mise en production

- [ ] Modifier `DEBUG = False`
- [ ] Générer une nouvelle `SECRET_KEY`
- [ ] Configurer `ALLOWED_HOSTS` avec vos domaines
- [ ] Passer la base de données de SQLite à PostgreSQL
- [ ] Configurer un système de email robuste (SES, SendGrid, etc.)
- [ ] Mettre en place HTTPS/SSL
- [ ] Configurer les logs et monitoring
- [ ] Tester en environnement de staging
- [ ] Sauvegardes automatiques de la base de données
- [ ] Documenter les procédures de déploiement et rollback

---

**Merci de contribuer à CYBER-NOX ! 🚀**
