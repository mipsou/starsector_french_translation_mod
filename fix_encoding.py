import os
import codecs

def fix_file_encoding(file_path):
    # Try to read the file with different encodings
    encodings = ['utf-8', 'latin1', 'cp1252', 'iso-8859-1']
    content = None
    
    for encoding in encodings:
        try:
            with codecs.open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
                break
        except UnicodeDecodeError:
            continue
    
    if content is None:
        print(f"Could not decode {file_path} with any of the attempted encodings")
        return False
    
    # Write the content back in UTF-8
    try:
        with codecs.open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully converted {file_path} to UTF-8")
        return True
    except Exception as e:
        print(f"Error writing {file_path}: {str(e)}")
        return False

# Files to fix
files_to_fix = [
    "data/strings/descriptions.csv",
    "translations/strings/descriptions.csv",
    "data/strings/strings.json",
    "translations/strings/strings.json",
    "data/world/factions/default_ship_roles.json",
    "translations/world/factions/default_ship_roles.json"
]

# Fix each file
for relative_path in files_to_fix:
    full_path = os.path.join("d:/Fractal Softworks/Starsector/mods/french_translation", relative_path)
    if os.path.exists(full_path):
        fix_file_encoding(full_path)
    else:
        print(f"File not found: {full_path}")
