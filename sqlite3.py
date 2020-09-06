# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:21:07 2020

@author: hemahemu
"""



#sqlite3 doesnot require separate server process
import sqlite3
#To use the module you have to create a connection object that represents the database
conn=sqlite3.connect('python1.db')
#once created a connection then, can create a cursor object than you can call its execute() method to perform SQL commands
c=conn.cursor()

#creating a table and inserting row
c.execute('''CREATE TABLE studb(name,skill,college,id)''')
c.execute("INSERT INTO studb VALUES('hemu','python','abc','1')")

#saving and closing
conn.commit()
conn.close()

#fetching the values from db
#sqlite3 doesnot require separate server process
import sqlite3
#To use the module you have to create a connection object that represents the database
conn=sqlite3.connect('python1.db')
#once created a connection then, can create a cursor object than you can call its execute() method to perform SQL commands

c=conn.cursor()
#creating a table and inserting row
c.execute('''CREATE TABLE studb(name,skill,college,id)''')
c.execute("INSERT INTO studb VALUES('hemu','python','abc','1')")

c.execute("SELECT * from studb")
#printing row value return by select query
for row in c:
    print(row)