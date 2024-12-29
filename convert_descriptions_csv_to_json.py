import csv
import json
import os

def clean_text(text):
    if text and text.startswith('FR:'):
        text = text[3:]  # Retire le préfixe "FR:"
    if text:
        # Normalise les sauts de ligne en \n
        text = text.replace('\r\n', '\n').replace('\r', '\n')
    return text

def convert_descriptions_csv_to_json(csv_file, json_file):
    # Lire le CSV avec l'encodage UTF-8
    with open(csv_file, 'r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        data = {}
        for row in csv_reader:
            id = row['id']
            type = row['type']
            text1 = clean_text(row['text1'])
            text2 = clean_text(row.get('text2', ''))
            text3 = clean_text(row.get('text3', ''))
            text4 = clean_text(row.get('text4', ''))
            
            # Créer l'entrée de description
            entry = {
                "type": type,
                "text1": text1,
                "text2": text2,
                "text3": text3,
                "text4": text4
            }
            
            # Supprimer les champs vides
            entry = {k: v for k, v in entry.items() if v}
            data[id] = entry

    # Créer le répertoire de sortie si nécessaire
    os.makedirs(os.path.dirname(json_file), exist_ok=True)

    # Écrire le JSON avec l'encodage UTF-8
    with open(json_file, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    csv_file = "data/strings/descriptions_fr.csv"
    json_file = "data/strings/descriptions_fr.json"
    convert_descriptions_csv_to_json(csv_file, json_file)
