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


sql_insert = "insert into user (userid, username) values(11,'name11')"
sql_update = "update user set username='name91' where userid=10"
sql_delete = "delete from user where userid<3"

try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount

    conn.commit()
except Exception as e:
    print e
    #发生了错误之后数据库回滚
    conn.rollback()

cursor.close()
conn.close()