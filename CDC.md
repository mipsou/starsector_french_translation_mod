# Cahier des Charges - Mod de Traduction Française pour Starsector

## 1. Objectif du Projet
Créer une traduction française complète et de qualité pour le jeu Starsector, en commençant par les descriptions d'armes et de vaisseaux.

## 2. Périmètre du Projet

### 2.1 Éléments à Traduire
- [ ] Tips et conseils de jeu
- [ ] Interface utilisateur
- [ ] Messages système
- [ ] Dialogues et événements
- [x] Descriptions des armes de base
- [ ] Descriptions des armes avancées
- [ ] Descriptions des vaisseaux
- [ ] Launcher (étape finale)

### 2.2 Priorités de Traduction
1. Tips et conseils de jeu
2. Interface utilisateur
3. Messages système
4. Dialogues et événements
5. Descriptions d'armes (en cours)
6. Descriptions de vaisseaux
7. Launcher (complexité élevée)

## 3. Spécifications Techniques

### 3.1 Format des Fichiers
- Fichiers CSV pour les traductions
  - Structure : id,type,text1,text2,text3,text4,notes
  - Type : WEAPON, SHIP, etc.
- Encodage UTF-8 avec BOM
- Préfixe "FR:" pour les traductions françaises

### 3.2 Organisation des Fichiers
- data/strings/ : Fichiers de traduction principaux
- data/config/ : Fichiers de configuration
- docs/ : Documentation du projet
- tools/ : Scripts et outils de gestion

### 3.3 Outils de Gestion
- clean_localization.py : Nettoyage des fichiers de traduction
- copy_old_localization.py : Migration des anciennes traductions
- handle_variant_names.py : Gestion des noms de variantes
- update_from_original.py : Mise à jour depuis les fichiers originaux
- version_manager.py : Gestion des versions de traduction

### 3.4 Système de Versionnage
- localization_version.json pour suivre les versions
- Compatibilité avec les versions du jeu
- Journal des modifications

### 3.5 Traduction du Launcher (Phase Finale)
Cette phase nécessitera :
- Modification des fichiers .jar du jeu (starfarer.api.jar, starfarer_obf.jar)
- Implémentation d'un système de localisation personnalisé
- Tests approfondis pour assurer la compatibilité
- Documentation détaillée du processus

#### Références pour le Launcher
- Mod de traduction chinoise comme exemple d'implémentation
- Nécessité de comprendre le code Java du launcher
- Potentielle collaboration avec d'autres projets de traduction

## 4. Structure des fichiers CSV

Les fichiers de traduction utilisent maintenant une structure standardisée avec les champs suivants :
- `id` : Identifiant unique de l'élément
- `type` : Type d'élément (weapon, ship, item, etc.)
- `text1` : Texte principal
- `text2` : Texte secondaire (optionnel)
- `text3` : Texte tertiaire (optionnel)
- `text4` : Texte quaternaire (optionnel)
- `notes` : Notes et commentaires pour les traducteurs

Les traductions doivent être préfixées par "FR:" pour être reconnues comme des traductions valides.

## 5. Scripts de gestion

### fetch_new_strings.py
- Récupère les nouvelles chaînes à traduire depuis les fichiers sources
- Supporte la nouvelle structure CSV avec type et champs multiples
- Préserve les traductions existantes
- Usage : `python fetch_new_strings.py --fetch`

### clean_localization.py
- Nettoie et valide les fichiers de traduction
- Vérifie la présence des IDs et la structure
- Normalise les espaces et sauts de ligne
- Vérifie le préfixe FR: pour les traductions
- Usage : 
  - `python clean_localization.py --clean` : Nettoie les fichiers
  - `python clean_localization.py --validate` : Vérifie les erreurs

### version_manager.py
- Gère les versions du mod de traduction
- Suit les versions du jeu
- Enregistre l'historique des changements
- Usage : `python version_manager.py --level [major|minor|patch] --changes "Description"`

## 6. Processus de traduction

### 6.1 Workflow Standard
1. Extraction des nouvelles chaînes
2. Traduction manuelle
3. Validation et nettoyage
4. Tests en jeu
5. Mise à jour de la version

### 6.2 Conventions de traduction
- Utilisation des guillemets français (« »)
- Respect des majuscules du texte source
- Conservation des variables et balises spéciales
- Documentation des choix de traduction difficiles

### 6.3 Tests et Validation
- Tests visuels en jeu
- Vérification des caractères spéciaux
- Validation des longueurs de texte
- Tests de compatibilité avec les mods

## 7. Maintenance et Mises à jour

### 7.1 Gestion des versions
- Versionnage sémantique (MAJOR.MINOR.PATCH)
- Documentation des changements dans CHANGELOG.md
- Tags Git pour chaque version

### 7.2 Sauvegarde et Restauration
- Backups automatiques avant les modifications majeures
- Scripts de restauration
- Gestion des conflits de version

### 7.3 Documentation
- Mise à jour du README.md
- Documentation des processus
- Guide de contribution

## 8. Protocole de Communication IA

### 8.1 Structure des Échanges
1. Analyse de la requête
2. Vérification des fichiers concernés
3. Proposition de modifications
4. Validation et application
5. Tests et confirmation

### 8.2 Règles de Modification
- Toujours vérifier l'encodage UTF-8
- Sauvegarder avant modification
- Respecter la structure existante
- Documenter les changements

### 8.3 Gestion des Erreurs
- Logging des erreurs
- Restauration automatique si nécessaire
- Rapport détaillé des problèmes
- Solutions alternatives proposées

## 9. Procédures de développement

1. Tout changement ou correction doit être documenté dans le fichier `devbook.md`
2. Les entrées dans le devbook doivent inclure :
   - La date et l'heure du changement
   - Le fichier modifié
   - La nature des modifications
   - La raison des modifications
   - Les références aux fichiers sources si pertinent

Le présent cahier des charges définit les règles et les spécifications techniques pour le mod de traduction française de Starsector. Il est essentiel de suivre ces règles pour garantir la qualité et la cohérence de la traduction.
