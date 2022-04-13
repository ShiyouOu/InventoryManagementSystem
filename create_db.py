import sqlite3 as sql
conn = sql.connect('database.db')
print("Opened	database	successfully")
conn.execute('CREATE TABLE products (name TEXT, description TEXT, quantity INTEGER, checkin TEXT)')
print("Table created successfully")
conn.close()