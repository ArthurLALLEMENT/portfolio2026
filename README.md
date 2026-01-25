# Nitroclash Legacy Hub

Un ecosysteme de mini-jeux web performant, concu pour la communaute Nitroclash. Ce projet transforme une base de donnees de joueurs en une serie d'experiences interactives incluant du management, des tournois et un mode arcade.

## Fonctionnalites

### Arcade : Ghost Dodge
Un shoot em up nerveux developpe en JavaScript pur avec integration de l API Web Audio.
- **Moteur de jeu** : Gestion de la difficulte progressive et systeme de niveaux.
- **Boss System** : Apparition d ennemis de taille superieure tous les 50 points.
- **Power-ups** : Module d invincibilite temporaire avec retour visuel neon.
- **Persistence** : Sauvegarde du meilleur score via localStorage.

### Arena Tournament
Generateur dynamique d arbres de competition.
- Tirage aleatoire base sur une liste de 206 pseudos.
- Visualisation structuree des phases de qualifications jusqu a la finale.

### Nitro Manager
Interface de gestion permettant de simuler la creation d une equipe.
- Design base sur le Glassmorphism (effets de transparence et flou).
- Algorithme de simulation de match integre.

## Fiche Technique

- **Langages** : HTML5, CSS3, JavaScript ES6+.
- **Audio** : Generation de sons synthetiques via Web Audio API (sans fichiers externes).
- **Rendu** : HTML5 Canvas pour le moteur de jeu et le systeme de particules en arriere-plan.
- **Architecture** : Application statique (Client-side uniquement).

## Structure des repertoires

```text
├── public/
│   ├── html/          # Points d entree (index, manager, tournament, arcade)
│   ├── css/           # Design system et animations
│   └── js/
│       ├── database.js   # Base de donnees des joueurs
│       ├── arcade.js     # Logique et moteur du jeu arcade
│       ├── particles.js  # Gestionnaire de particules d arriere-plan
│       └── main.js       # Initialisation et compteurs du hub
└── README.md
```

## Deploiement et Installation
### Cloner le depot : git clone https://github.com/votre-pseudo/nitro-games.git

### Executer le fichier public/html/index.html dans un navigateur.

### Aucune dependance ou serveur requis pour le fonctionnement local.
