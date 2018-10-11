#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'Saikikky'

import MySQLdb

conn = MySQLdb.Connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '19961125',
    db = 'pymysql',
    charset = 'utf8'
)

cursor = conn.cursor()

print conn
print cursor

cursor.close()
conn.close()