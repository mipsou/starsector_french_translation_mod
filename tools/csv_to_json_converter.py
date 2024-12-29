import csv
import json
import os
import shutil
import logging

# Configuration du logging
logging.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
    with open('tools/config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def convert_tips_csv_to_json(csv_path, json_path):
    tips = []
    try:
        with open(csv_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if 'freq' in row and 'tip' in row:
                    freq = int(row['freq']) if row['freq'].isdigit() else 1
                    if freq == 0:  # Si freq=0, utiliser un objet
                        tips.append({"freq": freq, "tip": row['tip']})
                    else:  # Sinon, utiliser une chaîne simple
                        tips.append(row['tip'])
                    
        # Créer le répertoire de sortie si nécessaire
        os.makedirs(os.path.dirname(json_path), exist_ok=True)

        # Sauvegarder en JSON avec le format des tips
        with open(json_path, 'w', encoding='utf-8') as f:
            # Utiliser un format plus compact et sans indentation pour correspondre au format original
            output = {"tips": tips}
            json.dump(output, f, ensure_ascii=False, separators=(',', ':'))
            
        logging.info(f"Conversion réussie de {csv_path} vers {json_path}")
        
    except Exception as e:
        logging.error(f"Erreur lors de la conversion de {csv_path}: {str(e)}")
        raise

def convert_csv_to_json(csv_path, json_path, is_tips=False):
    if is_tips:
        return convert_tips_csv_to_json(csv_path, json_path)
        
    # Charger le CSV
    translations = {}
    try:
        with open(csv_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Si le CSV a une colonne 'text', l'utiliser directement
                if 'text' in row and row['text']:
                    translations[row['id']] = row['text']
                    continue
                    
                # Sinon, gérer les colonnes text1 à text4
                entry = {}
                for i in range(1, 5):
                    key = f'text{i}'
                    if key in row and row[key]:
                        entry[key] = row[key]
                
                # Si l'entrée n'a qu'une seule clé text1, la simplifier
                if len(entry) == 1 and 'text1' in entry:
                    translations[row['id']] = entry['text1']
                else:
                    translations[row['id']] = entry

        # Créer le répertoire de sortie si nécessaire
        os.makedirs(os.path.dirname(json_path), exist_ok=True)

        # Sauvegarder en JSON avec le format simplifié
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(translations, f, ensure_ascii=False, indent=2)
            
        logging.info(f"Conversion réussie de {csv_path} vers {json_path}")
        
    except Exception as e:
        logging.error(f"Erreur lors de la conversion de {csv_path}: {str(e)}")
        raise

def main():
    try:
        config = load_config()
        translations_dir = config['paths']['translations']
        output_dir = config['paths']['output']
        backup_dir = config['paths']['backup']

        # Créer une sauvegarde du répertoire de sortie
        if os.path.exists(output_dir):
            logging.info(f"Sauvegarde de {output_dir} vers {backup_dir}")
            shutil.copytree(output_dir, backup_dir, dirs_exist_ok=True)

        # Convertir chaque fichier CSV en JSON
        for file_id, file_config in config['files'].items():
            csv_file = os.path.join(translations_dir, file_config['csv'])
            json_file = os.path.join(output_dir, file_config['json'])
            
            if os.path.exists(csv_file):
                logging.info(f"Conversion de {file_config['csv']} vers {file_config['json']}")
                is_tips = file_id == 'tips'  # Vérifier si c'est le fichier tips
                convert_csv_to_json(csv_file, json_file, is_tips)
            else:
                logging.warning(f"Fichier source manquant: {csv_file}")
                
    except Exception as e:
        logging.error(f"Erreur lors de l'exécution: {str(e)}")
        raise

if __name__ == "__main__":
    main()
