import os
import shutil
from pathlib import Path

def backup_game_files():
    """Crée une sauvegarde des fichiers de jeu originaux."""
    game_dir = Path("../")
    backup_dir = game_dir / "backup"
    
    if not backup_dir.exists():
        backup_dir.mkdir()
        
    files_to_backup = [
        game_dir / "data/strings/descriptions.csv",
        game_dir / "data/strings/ships.csv",
        game_dir / "data/strings/systems.csv"
    ]
    
    for file in files_to_backup:
        if file.exists():
            shutil.copy2(file, backup_dir / file.name)
            print(f"Backup créé pour {file.name}")

def install_translations():
    """Installe les traductions dans le répertoire du jeu."""
    mod_dir = Path(".")
    game_dir = Path("../")
    
    files_to_install = [
        ("translations/strings/descriptions_fr.csv", "data/strings/descriptions.csv"),
        ("translations/strings/ships_fr.csv", "data/strings/ships.csv"),
        ("translations/strings/systems_fr.csv", "data/strings/systems.csv")
    ]
    
    for src, dst in files_to_install:
        src_path = mod_dir / src
        dst_path = game_dir / dst
        
        if src_path.exists():
            # Créer les répertoires si nécessaire
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Copier le fichier
            shutil.copy2(src_path, dst_path)
            print(f"Installation de {src} vers {dst}")

def restore_originals():
    """Restaure les fichiers originaux du jeu."""
    game_dir = Path("../")
    backup_dir = game_dir / "backup"
    
    if not backup_dir.exists():
        print("Aucune sauvegarde trouvée")
        return
    
    for file in backup_dir.glob("*.csv"):
        dst_path = game_dir / "data/strings" / file.name
        shutil.copy2(file, dst_path)
        print(f"Restauration de {file.name}")

def main():
    print("=== Test d'intégration des traductions ===\n")
    
    # Créer une sauvegarde
    print("1. Création des sauvegardes...")
    backup_game_files()
    
    # Installer les traductions
    print("\n2. Installation des traductions...")
    install_translations()
    
    print("\nTest d'intégration terminé!")
    print("Vous pouvez maintenant lancer le jeu pour tester les traductions.")
    print("Pour restaurer les fichiers originaux, utilisez l'option --restore")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--restore":
        restore_originals()
    else:
        main()
