import os
import csv
import re

def clean_text(text):
    """Nettoie un texte en :
    - Supprimant les espaces multiples
    - Normalisant les sauts de ligne
    - Vérifiant le préfixe FR:
    """
    if not text:
        return text
        
    # Normaliser les sauts de ligne
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Supprimer les espaces multiples
    text = re.sub(r' +', ' ', text)
    
    # Supprimer les espaces en début/fin de ligne
    text = '\n'.join(line.strip() for line in text.split('\n'))
    
    # Vérifier et ajouter le préfixe FR: si c'est une traduction
    if text and not text.startswith('FR:') and any(c.isalpha() for c in text):
        text = f"FR:{text}"
    
    return text

def clean_csv_file(file_path):
    """Nettoie un fichier CSV de traduction."""
    if not os.path.exists(file_path):
        print(f"Le fichier n'existe pas : {file_path}")
        return
    
    # Lire le fichier
    rows = []
    fieldnames = ['id', 'type', 'text1', 'text2', 'text3', 'text4', 'notes']
    
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Nettoyer chaque champ de texte
            cleaned_row = row.copy()
            for field in ['text1', 'text2', 'text3', 'text4']:
                if field in cleaned_row:
                    cleaned_row[field] = clean_text(cleaned_row[field])
            rows.append(cleaned_row)
    
    # Écrire le fichier nettoyé
    with open(file_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def clean_all_translations():
    """Nettoie tous les fichiers de traduction."""
    translation_dir = 'translations/strings'
    if not os.path.exists(translation_dir):
        print(f"Répertoire de traduction non trouvé : {translation_dir}")
        return
    
    for filename in os.listdir(translation_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(translation_dir, filename)
            print(f"Nettoyage de {filename}...")
            clean_csv_file(file_path)

def validate_translations():
    """Valide les fichiers de traduction."""
    issues = []
    translation_dir = 'translations/strings'
    
    if not os.path.exists(translation_dir):
        print(f"Répertoire de traduction non trouvé : {translation_dir}")
        return issues
    
    for filename in os.listdir(translation_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(translation_dir, filename)
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                for i, row in enumerate(reader, start=2):  # Start at 2 to account for header
                    # Vérifier l'ID
                    if not row.get('id'):
                        issues.append(f"{filename}:{i} - ID manquant")
                    
                    # Vérifier les textes traduits
                    for field in ['text1', 'text2', 'text3', 'text4']:
                        if field in row and row[field]:
                            text = row[field]
                            if text.startswith('FR:'):
                                # Vérifier les caractères spéciaux
                                if re.search(r'[<>]', text):
                                    issues.append(f"{filename}:{i} - Caractères HTML dans {field}")
                                
                                # Vérifier les espaces multiples
                                if '  ' in text:
                                    issues.append(f"{filename}:{i} - Espaces multiples dans {field}")
    
    return issues

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Nettoyage et validation des fichiers de traduction')
    parser.add_argument('--clean', action='store_true', help='Nettoyer les fichiers')
    parser.add_argument('--validate', action='store_true', help='Valider les fichiers')
    
    args = parser.parse_args()
    
    if args.clean:
        clean_all_translations()
    
    if args.validate:
        issues = validate_translations()
        if issues:
            print("\nProblèmes trouvés :")
            for issue in issues:
                print(f"- {issue}")
        else:
            print("\nAucun problème trouvé !")
    
    if not args.clean and not args.validate:
        print("Aucune action spécifiée. Utilisez --clean ou --validate")
