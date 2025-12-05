# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 11:42:41 2025

@author: thoma
"""

from environs import Env

env = Env()
env.read_env()

db_database = env.str("DB_DATABASE")