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

#print conn
#print cursor

sql = "select * from user"
cursor.execute(sql)

print cursor.rowcount

rs = cursor.fetchone()
print rs

rs = cursor.fetchmany(3)
print rs

rs = cursor.fetchall()
print rs

cursor.close()
conn.close()