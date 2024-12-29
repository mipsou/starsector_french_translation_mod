import json
import os
from datetime import datetime

VERSION_FILE = "localization_version.json"

def load_version():
    """Charge le fichier de version ou crée un nouveau si inexistant."""
    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "version": "1.0.0",
        "game_version": "0.97a-RC11",
        "last_update": datetime.now().isoformat(),
        "changes": []
    }

def save_version(version_data):
    """Sauvegarde les données de version dans le fichier."""
    with open(VERSION_FILE, 'w', encoding='utf-8') as f:
        json.dump(version_data, f, indent=4, ensure_ascii=False)

def increment_version(version_str, level='patch'):
    """Incrémente le numéro de version selon le niveau spécifié."""
    major, minor, patch = map(int, version_str.split('.'))
    if level == 'major':
        return f"{major + 1}.0.0"
    elif level == 'minor':
        return f"{major}.{minor + 1}.0"
    else:  # patch
        return f"{major}.{minor}.{patch + 1}"

def update_version(level='patch', game_version=None, changes=None):
    """Met à jour le fichier de version avec les nouvelles informations."""
    version_data = load_version()
    
    # Mettre à jour la version
    version_data['version'] = increment_version(version_data['version'], level)
    
    # Mettre à jour la version du jeu si spécifiée
    if game_version:
        version_data['game_version'] = game_version
    
    # Mettre à jour la date
    version_data['last_update'] = datetime.now().isoformat()
    
    # Ajouter les changements
    if changes:
        if not isinstance(changes, list):
            changes = [changes]
        version_data['changes'].extend(changes)
    
    save_version(version_data)
    return version_data

def get_version_info():
    """Retourne les informations de version actuelles."""
    return load_version()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Gestionnaire de version pour le mod de traduction')
    parser.add_argument('--level', choices=['major', 'minor', 'patch'], default='patch',
                      help='Niveau de mise à jour de version')
    parser.add_argument('--game-version', help='Version du jeu')
    parser.add_argument('--changes', nargs='+', help='Liste des changements')
    
    args = parser.parse_args()
    
    updated = update_version(
        level=args.level,
        game_version=args.game_version,
        changes=args.changes
    )
    print(f"Version mise à jour : {json.dumps(updated, indent=2, ensure_ascii=False)}")
