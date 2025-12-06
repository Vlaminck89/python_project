# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 10:17:50 2025

@author: thoma
"""

class Autoverhuur:
    def __init__(self, customerID, carID, start_date, end_date, price):
        self._customerID = customerID
        self._carID = carID
        self._start_date = start_date
        self._end_date = end_date
        self._price = price
        
    def voeg_verhuur_toe(self, conn):
        try:
            cur = conn.cursor()
            query = '''
            INSERT INTO Rentals (customerID, carID, start_date, end_date, price)
            VALUES (?, ?, ?, ?, ?)
            '''
            parameters = (self._customerID, self._carID, self._start_date, self._end_date, self._price)
            cur.execute(query, parameters)
            conn.commit()
        except Exception as e:
            print(f'Fout bij het toevoegen van de verhuur: {e}')