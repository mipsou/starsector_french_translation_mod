import fetch_new_strings
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_parse_json():
    """Teste le parsing du fichier strings.json"""
    try:
        # Lecture du fichier source
        with open("D:/Fractal Softworks/Starsector/starsector-core/data/strings/strings.json", 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Test du parsing
        result = fetch_new_strings.parse_json_with_comments(content)
        
        if result:
            print("Parsing réussi!")
            # Afficher quelques clés pour vérification
            print("\nPremières clés trouvées:")
            if isinstance(result, dict):
                for key in list(result.keys())[:5]:
                    print(f"- {key}")
        else:
            print("Échec du parsing")
            
    except Exception as e:
        print(f"Erreur lors du test: {str(e)}")

if __name__ == "__main__":
    test_parse_json()
