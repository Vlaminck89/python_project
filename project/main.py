# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 11:16:29 2025

@author: thoma
"""

import pandas as pd
import sqlite3
from sqlite3 import Error
from service.service import db_connectie
from models.car import Car
from models.customer import Customer

conn = db_connectie()
# car = Car('Fiat', 'Punto', '2020', '1-TZE-243', 100)
# car.voeg_auto_toe(conn)
c = Customer('Lars', 'Vermeers', 'larsvermeers@gmail.com', '0477323412', 'Klaproosstraat 27, 3842 Zwolle')
c.voeg_customer_toe(conn)
# cur = conn.cursor()
# query ='''
# select * 
# from customers
# '''
# data = pd.read_sql_query(query, conn)
# print(data)
conn.close()