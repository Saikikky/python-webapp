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

sql = "select * from user"
cursor.execute(sql)

rs = cursor.fetchall()
for row in rs:
    print "userid=%s, username=%s" % row

cursor.close()
conn.close()