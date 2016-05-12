#!/usr/bin/env Python
#coding:utf-8
'''
Created on 2016年5月5日

@author: Administrator
'''
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='1111',db='security');

cur = conn.cursor()

reCount = cur.execute('select * from emails')

cur.close()

conn.close()

print reCount
