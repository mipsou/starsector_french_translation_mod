import csv
import json

def convert_csv_to_json(csv_file, json_file):
    # Lire le CSV avec l'encodage UTF-8
    with open(csv_file, 'r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        data = {}
        for row in csv_reader:
            freq = float(row['freq'])
            tip = row['tip']
            data[tip] = freq

    # Écrire le JSON avec l'encodage UTF-8
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    csv_file = "translations/strings/tips_fr.csv"
    json_file = "translations/strings/tips.json"
    convert_csv_to_json(csv_file, json_file)
