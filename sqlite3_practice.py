import sqlite3 #build in sqlite3 module

#connect the database (file will be created id doesnt exist)
conn = sqlite3.connect ('students.db')

#create a cursor to execute a sql
cursor = conn.cursor() #cursor execute the query 

#SQLITE DATA TYPES:
#INTEGER, REAL(FLOAT), TEXT(STR, DATE, CHAR), BLOB (BINARY DATA), NULL

#create table
cursor.execute("""
CREATE TABLE if not exists students(
    id int primary key autoincrement,
    name text not null,
    grade int,
    address text 
)"""
)
conn.commit()
