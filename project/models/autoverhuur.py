# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 10:17:50 2025

@author: thoma
"""

import pandas as pd


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
    
    def get_rentals(conn):
       try:
           query = '''
           SELECT * FROM Rentals
           INNER JOIN Cars USING (carID)
           INNER JOIN Customers USING (customerID);
           '''
           df = pd.read_sql_query(query, conn)
           rentals = df[["rentalID", "carID", "brand", "model", "year", "license_plate",
                         "total_price", "customerID", "first_name", "last_name"]]
           return rentals
       except Exception as e:
           print(f'Fout bij het opvragen van de query: {e}')
    
    def get_opbrengst_per_klant(conn):
        try:
            query = '''
            select * from Rentals
            inner join Customers using (customerID);
            '''
            df = pd.read_sql_query(query, conn)
            opbrengst = df[["customerID", "first_name", "last_name", "total_price"]]
            opbrengst_per_klant = opbrengst.groupby(["customerID", "first_name", "last_name"], as_index= False)["total_price"].sum()      
            opbrengst_per_klant = opbrengst_per_klant.sort_values(by= "total_price", ascending= False)
            return opbrengst_per_klant
        except Exception as e:
            print(f'Fout bij het opvragen van de query: {e}')
    
    def get_opbrengst_per_auto(conn):
        try:
            query = '''
            select * from Rentals
            inner join cars using (carID);
            '''
            df = pd.read_sql_query(query, conn)
            opbrengst = df[["carID", "brand", "model", "total_price"]]
            opbrengst_per_auto = opbrengst.groupby(["carID", "brand", "model"], as_index= False)["total_price"].sum()
            opbrengst_per_auto = opbrengst_per_auto.sort_values(by= "total_price", ascending= False)
            return opbrengst_per_auto
        except Exception as e:
            print(f'Fout bij het opvragen van de query: {e}')
            
    @staticmethod
    def excel_verhuur(conn, excel_file):
        try:
            rentals = Autoverhuur.get_rentals(conn)
            opbrengst_per_klant = Autoverhuur.get_opbrengst_per_klant(conn)
            opbrengst_per_auto = Autoverhuur.get_opbrengst_per_auto(conn)
            with pd.ExcelWriter(excel_file) as writer:
                rentals.to_excel(excel_writer= writer, sheet_name='Huurovereenkomsten', index=False)
                opbrengst_per_klant.to_excel(excel_writer= writer, sheet_name='Opbrengst per klant', index= False)
                opbrengst_per_auto.to_excel(excel_writer= writer, sheet_name='Opbrengst per auto', index= False)
        except Exception as e:
            print(f'Fout bij het opvragen van de query: {e}')
            
    @staticmethod
    def csv_verhuur(conn, csv_file):
        try:
            rentals = Autoverhuur.get_rentals(conn)
            rentals.to_csv(csv_file, index= False)
        except Exception as e:
            print(f'Fout bij het opvragen van de query: {e}')
            

    