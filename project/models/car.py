# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:47:28 2025

@author: thoma
"""


class Car:
    def __init__(self, brand, model, year, license_plate, price):
        self._brand = brand
        self._model = model
        self._year = year
        self._license_plate = license_plate
        self._price = price

    def voeg_auto_toe(self, conn):
        try:
            cur = conn.cursor()
            query = '''
            INSERT INTO cars (brand, model, year, license_plate, price)
            VALUES (?, ?, ?, ?, ?)
            '''
            parameters = (self._brand, self._model, self._year,
                          self._license_plate, self._price)
            cur.execute(query, parameters)
            conn.commit()
            print(f'{self._brand} {self._model} met nummerplaat {
                  self._license_plate} is toegevoegd.')
        except Exception as e:
            print(f'Fout bij het toevoegen van de auto: {e}')
            
    def __str__(self):
        return ("Brand: " + self._brand +
        "\nModel: " + self._model +
        "\nYear: " + str(self._year) +
        "\nlicense plate: " + self._license_plate +
        "\nPrice: €" + str(self._price))


if __name__ == '__main__':
    brand = input('Geef het merk van de auto:\n')
    model = input('Geef het model van de auto:\n')
    year = int(input('Geef het bouwjaar van de auto:\n'))
    license_plate = input('Geef de nummerplaat van de auto:\n')
    price = float(input('Geef de huurprijs van de auto:\n'))
    car = Car(brand, model, year, license_plate, price)
    print(car)
