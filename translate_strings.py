import os
import csv
import json
import requests
from deep_translator import GoogleTranslator

def translate_descriptions():
    translation_file = os.path.join('translations', 'strings', 'descriptions.csv')
    temp_file = os.path.join('translations', 'strings', 'descriptions_temp.csv')

    # Lire le fichier de traduction
    translations = []
    with open(translation_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            translations.append(row)

    # Traduire chaque texte
    translator = GoogleTranslator(source='en', target='fr')
    
    for row in translations:
        if row['text1'] and not row['text1'].startswith('FR:'):
            try:
                # Traduire par morceaux pour éviter les limites de longueur
                text = row['text1']
                chunks = [text[i:i+4500] for i in range(0, len(text), 4500)]
                translated_chunks = []
                
                for chunk in chunks:
                    translated = translator.translate(chunk)
                    translated_chunks.append(translated)
                
                translated_text = ' '.join(translated_chunks)
                row['text1'] = f"FR: {translated_text}"
                print(f"Traduit: {row['id']}")
            except Exception as e:
                print(f"Erreur lors de la traduction de {row['id']}: {str(e)}")

    # Sauvegarder les traductions
    with open(temp_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'text1'], quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(translations)

    # Remplacer le fichier original par le fichier temporaire
    os.replace(temp_file, translation_file)

if __name__ == "__main__":
    translate_descriptions()
