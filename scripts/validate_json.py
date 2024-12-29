import json
import os
import sys
from pathlib import Path

def validate_json_file(file_path):
    """Valide un fichier JSON et vérifie sa structure."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Vérification spécifique pour tips.json
        if file_path.name == 'tips_fr.json':
            if 'tips' not in data:
                return False, "Le fichier tips_fr.json doit avoir une clé 'tips'"
            for tip in data['tips']:
                if isinstance(tip, dict):
                    if 'freq' not in tip or 'tip' not in tip:
                        return False, f"Tip invalide : {tip} - doit avoir 'freq' et 'tip'"
                    if not isinstance(tip['freq'], (int, float)):
                        return False, f"Fréquence invalide dans : {tip}"
                    if not isinstance(tip['tip'], str):
                        return False, f"Tip invalide (doit être une chaîne) : {tip}"
                elif not isinstance(tip, str):
                    return False, f"Tip invalide (doit être une chaîne ou un dict) : {tip}"
        
        return True, "OK"
    except json.JSONDecodeError as e:
        return False, f"Erreur JSON : {str(e)}"
    except Exception as e:
        return False, f"Erreur : {str(e)}"

def main():
    """Point d'entrée principal."""
    # Force l'encodage en UTF-8 pour la sortie
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')

    base_dir = Path("D:/Fractal Softworks/Starsector/mods/french_translation")
    json_dir = base_dir / "localization/data/strings/french"
    
    if not json_dir.exists():
        print(f"Dossier non trouvé : {json_dir}")
        return
    
    all_valid = True
    for file in json_dir.glob("*.json"):
        print(f"\nValidation de {file.name}...")
        valid, message = validate_json_file(file)
        if not valid:
            all_valid = False
            print(f"[ERREUR] {message}")
        else:
            print("[OK]")
    
    if all_valid:
        print("\nTous les fichiers sont valides !")
    else:
        print("\nDes erreurs ont été trouvées.")
        sys.exit(1)

if __name__ == "__main__":
    main()
