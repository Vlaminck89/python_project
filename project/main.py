# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 11:16:29 2025

@author: thoma
"""

import pandas as pd
import sqlite3
from sqlite3 import Error
from service.service import db_connectie
from models import car

conn = db_connectie()
cur = conn.cursor()
query ='''
select * 
from cars
'''
data = pd.read_sql_query(query, conn)
print(data)
conn.close()