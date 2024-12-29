import shutil
import os
import sys
from pathlib import Path

def update_originals():
    """Met à jour les fichiers originaux depuis le dossier du jeu."""
    # Force l'encodage en UTF-8 pour la sortie
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')

    game_dir = Path("D:/Fractal Softworks/Starsector")
    mod_dir = game_dir / "mods/french_translation"
    
    # Chemins source (jeu)
    game_strings = game_dir / "starsector-core/data/strings"
    
    # Chemins destination (mod)
    mod_originals = mod_dir / "localization/data/strings/original"
    
    # Créer le dossier de destination s'il n'existe pas
    mod_originals.mkdir(parents=True, exist_ok=True)
    
    # Liste des fichiers à copier
    files_to_copy = [
        "tips.json",
        "strings.json",
        "descriptions.csv",
        "ship_names.json",
        "tooltips.json"
    ]
    
    # Copier chaque fichier
    files_copied = 0
    for file in files_to_copy:
        src = game_strings / file
        dst = mod_originals / file
        if src.exists():
            print(f"Copie de {file}...")
            shutil.copy2(src, dst)
            files_copied += 1
        else:
            print(f"[ATTENTION] Fichier non trouvé : {file}")
    
    print(f"\n[OK] Mise à jour terminée ! {files_copied} fichiers copiés.")

if __name__ == "__main__":
    update_originals()
