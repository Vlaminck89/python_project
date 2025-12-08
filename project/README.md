# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 12:34:48 2025

@author: thoma
"""
## Packages te installeren
cf. requirements.txt in de map project

## Hoe te installeren
Creëer een virtual environnement in de map project via de commandprompt en
installeer de packages die in 'requirements.txt' staan.
Voorbeeld:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Doel
Deze applicatie beheert het verhuur van een autoverhuurfirma in een SQLite database.

## Functionaliteiten
- Klanten toevoegen
- Auto's toevoegen
- verhuur toevoegen
- Rapport exporteren naar Excel
- Rapport exporteren naar CSV

## Database
De database wordt geïnstalleerd in de project map.
Het configbestand leest de naam van de database uit het .env bestand en het service bestand
maakt de connectie met de database.