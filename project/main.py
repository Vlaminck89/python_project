# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 11:16:29 2025

@author: thoma
"""

import pandas as pd
from sqlite3 import Error
from service.service import db_connectie
from models.car import Car
from models.customer import Customer
from models.autoverhuur import Autoverhuur
from datetime import datetime
import os

def main():
    try:
        conn = db_connectie()
    except Error as e:
        print(f'Fout bij het connecteren met de database: {e}')
        
    huidig_pad = os.path.abspath(os.getcwd())
    excel_map = os.path.join(huidig_pad, "Excel_reports") 
    if not os.path.exists(excel_map):
        os.mkdir(excel_map)
    else:
        pass
    csv_map = os.path.join(huidig_pad, "Csv_reports")
    if not os.path.exists(csv_map):
        os.mkdir(csv_map)
    else:
        pass

    while True:

        print('---Auto Rental menu---')
        print()
        print('1. Voeg klant toe')
        print('2. Voeg auto toe')
        print('3. Autoverhuur toevoegen')
        print('4. Rapport verhuur to_excel')
        print('5. Rapport verhuur to_csv')
        print('6. Stop programma')

        try:
            keuze = int(input('Maak een keuze:\n'))
        except ValueError:
            print('Foutieve ingave: kies een cijfer uit het keuzemenu.')
            continue

        if keuze == 1:
            first = input('Geef de voornaam:\n')
            last = input('Geef de achternaam:\n')
            mail = input('Geef het e-mail adres:\n')
            phone = input('Geef het telefoonnummer:\n')
            address = input('Geef het adres:\n')
            customer = Customer(first, last, mail, phone, address)
            customer.voeg_customer_toe(conn)
            
        elif keuze == 2:
            brand = input('Geef het merk van de auto:\n')
            model = input('Geef het model van de auto:\n')
            year = int(input('Geef het bouwjaar van de auto:\n'))
            license_plate = input('Geef de nummerplaat van de auto:\n')
            price = float(input('Geef de huurprijs van de auto:\n'))
            car = Car(brand, model, year, license_plate, price)
            car.voeg_auto_toe(conn)
            
        elif keuze == 3:
            df_klant = pd.read_sql_query('SELECT * from customers', conn)
            print(df_klant[['customerID', 'first_name', 'last_name']])
            while True:
                try:
                    keuze_klant = int(input('\nGeef het customerID in om de klant te selecteren:\n'))
                    if keuze_klant in df_klant['customerID'].values:
                        break
                    else:
                        print('\nOngeldig customerID, selecteer een ID uit de lijst.')
                except ValueError:
                    print('\nGeef een geldig getal in.')
                    
            df_car = pd.read_sql_query('SELECT * from cars', conn)
            print(df_car[['carID', 'brand', 'model']])
            while True:
                try:
                    keuze_auto = int(input('\nGeef het carID om de auto te selecteren:\n'))
                    if keuze_auto in df_car['carID'].values:
                        break
                    else:
                        print('Ongeldig carID, selecteer een ID uit de lijst.')
                except ValueError:
                    print('\nVoer een geldig getal in.')
                    
            while True:
                start_datum = input('Geef de startdatum van het verhuur: (DD-MM-YY)\n')
                try:
                    start_datum = datetime.strptime(start_datum, '%d-%m-%y').date()
                    break
                except ValueError:
                    print('\nFoutieve ingave: geef het formaat (DD-MM-YY)')
            
            while True:
                eind_datum = input('\nGeef de einddatum van het verhuur: (DD-MM-YY)\n')
                try:
                    eind_datum = datetime.strptime(eind_datum, '%d-%m-%y').date()
                    break
                except ValueError:
                    print('\nFoutieve ingave: geef het formaat (DD-MM-YY)')
                    
            aantal_dagen = (eind_datum - start_datum).days
            cur = conn.cursor()
            cur.execute("SELECT price FROM Cars WHERE carID = ?", (keuze_auto,))
            prijs = cur.fetchone()
            prijs = prijs[0]
            totaal_prijs = float(abs(aantal_dagen)) * float(prijs)
            verhuur = Autoverhuur(keuze_klant, keuze_auto, start_datum, eind_datum, totaal_prijs)
            verhuur.voeg_verhuur_toe(conn)
            print('\n--------------------------\n')
            print(f'Verhuur werd geregistreerd.\nPrijs voor het verhuur: € {totaal_prijs}\n')
        
        elif keuze == 4:
            bestandsnaam = input('Geef de bestandsnaam van het rapport:\n').strip()
            bestandsnaam_excel= f"{bestandsnaam}.xlsx"
            excel_file = os.path.join(excel_map, bestandsnaam_excel)
            Autoverhuur.excel_verhuur(conn, excel_file)
            pad= os.path.abspath(os.getcwd())
            print(f'\n{bestandsnaam_excel} is terug te vinden in de map excel in {pad}\n')
            
        elif keuze == 5:
            bestandsnaam= input('Geef de bestandsnaam van het rapport:\n').strip()
            bestandsnaam_csv= f"{bestandsnaam}.csv"
            csv_file = os.path.join(csv_map, bestandsnaam_csv)
            Autoverhuur.csv_verhuur(conn, csv_file)
            pad= os.path.abspath(os.getcwd())
            print(f'\n{bestandsnaam_csv} is terug te vinden in de map excel in {pad}\n')
            
        elif keuze == 6:
            break
        
    conn.close()
    
if __name__ == '__main__':
    main()
