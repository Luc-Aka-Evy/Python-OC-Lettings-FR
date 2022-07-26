## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Luc-Aka-Evy/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profiles);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  profiles_profiles where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

#### Déploiement (Heroku)

### Prérequis

- [CircleCI](https://circleci.com/signup/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--emea-en-dsa-maxConv-auth-nb&utm_term=g_-_c__dsa_&utm_content=&gclid=Cj0KCQjwlemWBhDUARIsAFp1rLXh3RH0rSg4vZNsF2XIt81wFvVdW-j33Kf22GMPybF-Dps_WXVtYOAaArUAEALw_wcB) (connectez-vous avec votre compte github cela sera plus simple pour la suite)
- Un compte [Docker Hub](https://hub.docker.com/)
- Docker [Version Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac), [Version Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
- Compte [Heroku](https://signup.heroku.com/)
- Heroku CLI
- Compte [Sentry
](https://sentry.io/signup/)

Cette section est la pour vous aider à déployer votre application sur Heroku,à poster l'image sur le Docker hub et fair son suivi via sentry.

- Dans un premier temps veuillez créer un compte et installer les logiciels indiqué dans les prérequis
- Allez sur votre compte CircleCi dans l'onglet 'Projects' dans la barre de navigation à gauche
- Selectionner le project que vous voulez set up dans notre cas 'Python-OC-Lettings' et choisissez l'option 'fastest' qui va utiliser le fichier config.yml du dossier circleci.
- une fois cela fait une pipeline devrait se lancer dans votre dashboard et vous devriez voir un onglet bleu running ou bien un rouge failed (ce qui est normal car il y a des variables d'environnement définit dans le fichier config.yml que nous n'avons pas encore renseigné sur Circleci).
- Allez sur votre compte docker hub dans l'onglet 'repositories' et créer un nouveau repo en cliquant sur 'create repository' et nommer le oc-lettings.
- Dans circleci retourner sur l'onglet 'project' selectionner votre projet, rendez-vous dans l'onglet 'projects settings' ensuite dans l'onglet 'Environment Variable'.
- Ajouter les variables 'DOCKER_LOGIN', 'DOCKER_PASSWORD', 'USERNAME' qui sont votre username et mot de passe docker. 
- Rendez vous dans votre terminal à la racine du projet
- Connectez-vous sur votre compte heroku via Heroku CLI avec la command `heroku login` (connexion via internet) ou `heroku login -i` (connexion via terminal en entrant votre email et le mot de passe associer à votre compte Heroku)
- Dans votre terminal entrer la command `heroku create APP_NAME` changer le APP_NAME par le nom que voulez car il se peut que le nom oc-lettings ne soit pas disponible.
- une fois que c'est fait rendez vous sur votre compte heroku pour vérifier que l'app a bien été crée.
- Rendez vous dans l'onglet account settings en cliquant sur votre profile.
- copier la valeur présente dans vore API KEY et ajouter la dans une varibale d'environnement sur circle ci sous le nom HEROKU_API_KEY et ajouter le nom de l'app dans une variable nommée HEROKU_APP_NAME.
- Connectez vous sur votre compte Sentry, dans l'onglet projects cliquer ensuite sur create project et selectionner django
- Récuperer la valeur qui est dans la variable 'dsn=valeur'
- Si vous êtes sur MAC os sur heroku selectionnez votre app et allez dans l'onglet settings et ajouter la valeur dans une variable SENTRY_DSN dans congif vars
- Si vous êtes sur windows ou linux aller dans le fichier oc-lettings-site/settings.py et remplacer la valeur 'os.getenv("SENTRY_DNS")' par la valeur du dsn donner sur sentry.
- Une fois que vous ava fait toute ces étapes vous pouvez faire un nouveau commit et push sur github et vous verrez la pipeline se laner dans circleci attendez jusqu'à ce que le running soit fini et affiche un bouton vert succes.
- Rendez vous sur votre compte docker hub pour vérifier quel'image d site a bien été push et tag avec le numéro SHA_1 de circle ci
- Rendez vous sur votre compte Heroku vous devriez voir dans l'onglet 'Overview' que le deploiement a bien été fait vous puvez cliquer sur le bouton open app pour voir que votre application fonctionne bien.
- Rendez vous sur sentry pour voir que votre aplication est bien suivi.

Félicitations vous avez déployer votre application avec succés.
