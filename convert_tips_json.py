import json

# Lire le fichier JSON source
with open('data/strings/tips_fr.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Retirer les préfixes "FR:" de tous les tips
for i, tip in enumerate(data['tips']):
    if isinstance(tip, dict):
        if tip['tip'].startswith('FR:'):
            tip['tip'] = tip['tip'][3:]
    elif isinstance(tip, str):
        if tip.startswith('FR:'):
            data['tips'][i] = tip[3:]

# Écrire le fichier JSON mis à jour
with open('data/strings/tips_fr.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
