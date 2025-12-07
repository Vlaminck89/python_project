# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 10:17:50 2025

@author: thoma
"""

import pandas as pd
import os
import openpyxl

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
            INSERT INTO Rentals (customerID, carID, start_date, end_date, total_price)
            VALUES (?, ?, ?, ?, ?)
            '''
            parameters = (self._customerID, self._carID,
                          self._start_date, self._end_date, self._price)
            cur.execute(query, parameters)
            conn.commit()
        except Exception as e:
            print(f'Fout bij het toevoegen van de verhuur: {e}')
    
    # @classmethod
    # def bestandsnaam_vragen(cls):
    #     huidig_pad = os.path.abspath(os.getcwd())
    #     print(huidig_pad)
    #     print(type(huidig_pad))
        
    @staticmethod
    def excel_verhuur(conn, excel_file):
        try:
            query = '''
            select * from Rentals
            inner join cars USING (carID)
            inner join Customers using (customerID);
            '''
            df = pd.read_sql_query(query, conn)
            rentals = df[["rentalID", "carID", "brand", "model", "year", "license_plate",
                          "total_price", "customerID", "first_name", "last_name"]]
            with pd.ExcelWriter(excel_file) as writer:
                rentals.to_excel(excel_writer=writer, sheet_name='Huurovereenkomsten', index=False)
        except Exception as e:
            print(f'Fout bij het opvragen van de query: {e}')

# if __name__ == '__main__':
#     # Autoverhuur.bestandsnaam_vragen()
    