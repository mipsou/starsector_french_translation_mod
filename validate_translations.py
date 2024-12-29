import csv
import os
import re
from pathlib import Path

def validate_file_encoding(file_path):
    """Vérifie l'encodage UTF-8 avec BOM."""
    with open(file_path, 'rb') as f:
        raw = f.read()
        return raw.startswith(b'\xef\xbb\xbf')

def validate_csv_format(file_path):
    """Vérifie le format CSV et la présence des guillemets pour les champs multilignes."""
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            headers = next(reader)
            if headers != ['id', 'text1']:
                return False, "En-têtes CSV incorrects"
            
            for row in reader:
                if len(row) != 2:
                    return False, f"Format incorrect pour la ligne: {row}"
                if '\n' in row[1] and not (row[1].startswith('"') and row[1].endswith('"')):
                    return False, f"Guillemets manquants pour champ multiligne: {row[0]}"
        return True, "Format CSV valide"
    except Exception as e:
        return False, f"Erreur lors de la validation CSV: {str(e)}"

def validate_translation_prefix(file_path):
    """Vérifie que chaque traduction commence par 'FR:'."""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            if not row[1].strip().startswith('FR:'):
                return False, f"Préfixe 'FR:' manquant pour: {row[0]}"
    return True, "Tous les préfixes sont corrects"

def validate_special_chars(file_path):
    """Vérifie les caractères spéciaux problématiques."""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
        problematic = re.findall(r'[^\x00-\x7F\u00C0-\u017F\s]', content)
        if problematic:
            return False, f"Caractères problématiques trouvés: {set(problematic)}"
    return True, "Pas de caractères problématiques"

def main():
    translation_dir = Path("translations/strings")
    files_to_check = [
        translation_dir / "descriptions_fr.csv",
        translation_dir / "ships_fr.csv",
        translation_dir / "systems_fr.csv"
    ]
    
    print("=== Début de la validation des traductions ===\n")
    
    for file_path in files_to_check:
        print(f"\nValidation de {file_path.name}:")
        print("-" * 40)
        
        # Vérification de l'encodage
        if validate_file_encoding(file_path):
            print("[OK] Encodage UTF-8 avec BOM")
        else:
            print("[ERREUR] Encodage incorrect")
        
        # Vérification du format CSV
        success, message = validate_csv_format(file_path)
        print(f"[{'OK' if success else 'ERREUR'}] Format CSV: {message}")
        
        # Vérification des préfixes
        success, message = validate_translation_prefix(file_path)
        print(f"[{'OK' if success else 'ERREUR'}] Préfixes: {message}")
        
        # Vérification des caractères spéciaux
        success, message = validate_special_chars(file_path)
        print(f"[{'OK' if success else 'ERREUR'}] Caractères spéciaux: {message}")

if __name__ == "__main__":
    main()
