import pandas as pd
import mysql.connector

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database = 'indigo'
    )
    mycursor = conn.cursor()
    print("Connection established")
except Exception as e:
    print(e)


# CREATE A DATABASE
# mycursor.execute("CREATE DATABASE indigo")
# conn.commit() #Used in write operations

# Create a table
# try:
#     mycursor.execute("""
#     CREATE TABLE airport(
#         airport_id INTEGER PRIMARY KEY,
#         code VARCHAR(10) NOT NULL,
#         name VARCHAR(255) NOT NULL,
#         city VARCHAR(50) NOT NULL )
#     """)
#     conn.commit()
#     print("Table created")
# except Exception as e:
#     print(e)

# INSERT DATA
# mycursor.execute("""
# INSERT INTO airport VALUES
# (1,"DEL","New Delhi", "IGIA"),
# (2,"CCU","Kolkata","NSCA"),
# (3,"BOM","Mumbai","CSMA")
# """)
# conn.commit()


# SEARCH/RETRIEVE
mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycursor.fetchall()
print(data)
for i in data:
    print(i[3])

# Update
# mycursor.execute("""
#     UPDATE airport
#     SET city = 'Bombay'
#     WHERE airport_id = 3
# """)
# conn.commit()


 # Delete
# mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
# conn.commit()

mycursor.execute("SELECT * FROM airport")
data = mycursor.fetchall()
print(data)