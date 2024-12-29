#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tempfile
import shutil
import codecs

translations = {
    'atropos': {
        'old': r'A rack of advanced guided torpedoes.*?chemical charge\.',
        'new': '''Un rack de torpilles guidées avancées. La charge utile est plus petite que d'habitude pour faire de la place au système de guidage avancé et à la masse de réaction du système de manœuvre.

La torpille Atropos est une grande torpille guidée à portée étendue. Chaque rack monte deux torpilles qui peuvent être tirées séparément, permettant aux capitaines d'attaque une flexibilité maximale. L'ogive nucléaire catalysée par antimatière typiquement utilisée dans les ogives de torpilles est absente ici car l'interférence baryonique du détonateur perturberait les systèmes de guidage. Elle est remplacée par une charge chimique plus petite, mais toujours puissante.'''
    },
    'atropos_single': {
        'old': r'A single advanced, guided torpedo.*?single torpedo\.',
        'new': '''Une seule torpille guidée avancée. La charge utile est plus petite que d'habitude pour faire de la place au système de guidage avancé et à la masse de réaction du système de manœuvre.'''
    },
    'breach': {
        'old': r'A fast, heavily armored missile.*?anti-armor warhead\.',
        'new': '''Un missile lourdement blindé et rapide avec un bon guidage et une petite ogive spécialisée anti-blindage.'''
    },
    'breachpod': {
        'old': r'A one-shot missile weapon.*?anti-armor warhead\.',
        'new': '''Une arme à missile à usage unique. Le missile est lourdement blindé et rapide avec un bon guidage et une petite ogive spécialisée anti-blindage.'''
    },
    'pilum': {
        'old': r'A two-stage missile.*?shield-piercing warheads\.',
        'new': '''Un rack de missiles anti-bouclier à longue portée. Les missiles Pilum sont conçus pour percer les boucliers ennemis avec leurs ogives perforantes.'''
    },
    'pilum_large': {
        'old': r'A large rack of long-range.*?shield-piercing warheads\.',
        'new': '''Un grand rack de missiles anti-bouclier à longue portée. Les missiles Pilum sont conçus pour percer les boucliers ennemis avec leurs ogives perforantes.'''
    },
    'phasecl': {
        'old': r'A phase cloak system.*?phase space\.',
        'new': '''Un système de camouflage phasique. Permet au vaisseau de se déphaser temporairement dans un espace dimensionnel alternatif.'''
    },
    'phasecl_bomber': {
        'old': r'A phase cloak system.*?phase space\.',
        'new': '''Un système de camouflage phasique. Permet au vaisseau de se déphaser temporairement dans un espace dimensionnel alternatif.'''
    },
    'typhoon': {
        'old': r'A launcher for Typhoon reaper torpedoes.*?antimatter-catalyzed nuclear warhead\.',
        'new': '''Un lanceur de torpilles Typhoon. La torpille Typhoon est une arme à longue portée équipée d'une ogive nucléaire catalysée par antimatière.'''
    },
    'cyclone': {
        'old': r'A launcher for Cyclone reaper torpedoes.*?antimatter-catalyzed nuclear warhead\.',
        'new': '''Un lanceur de torpilles Cyclone. La torpille Cyclone est une arme à longue portée équipée d'une ogive nucléaire catalysée par antimatière.'''
    }
}

import re

def update_translations():
    # Lire le contenu du fichier en binaire
    with open('translations/strings/descriptions.csv', 'rb') as f:
        raw_content = f.read()
    
    # Détecter l'encodage
    try:
        content = raw_content.decode('utf-8')
    except UnicodeDecodeError:
        try:
            content = raw_content.decode('latin1')
        except UnicodeDecodeError:
            content = raw_content.decode('cp1252')

    # Appliquer chaque traduction
    for weapon_id, translation in translations.items():
        pattern = f'"{weapon_id}","{translation["old"]}"'
        replacement = f'"{weapon_id}","{translation["new"]}"'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Créer un fichier temporaire
    temp_fd, temp_path = tempfile.mkstemp()
    try:
        with os.fdopen(temp_fd, 'w', encoding='utf-8', newline='') as temp_file:
            temp_file.write(content)
        
        # Remplacer le fichier original par le fichier temporaire
        shutil.move(temp_path, 'translations/strings/descriptions.csv')

    except Exception as e:
        print(f"Erreur : {e}")
        if os.path.exists(temp_path):
            os.unlink(temp_path)

if __name__ == '__main__':
    update_translations()
