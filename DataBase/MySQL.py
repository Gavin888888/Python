#!/usr/bin/env python
# encoding: utf-8
import MySQLdb
try:
    connect = MySQLdb.connect(host='localhost',user='root',passwd='lsb',port=3306)
    cur = connect.cursor()
    db_name = 'py_db'
#cur.execute('create database if not exists '+db_name)
    connect.select_db(db_name)
    #cur.execute('create table test(id int,info varchar(20))')
    value = [2,'hi python db']
    cur.execute('insert into test values(%s,%s)',value)
    connect.commit()
    cur.close()
    connect.close()
except MySQLdb.Error,e:
    print('-----db error :' + e)
finally:
    print('-------please try again')