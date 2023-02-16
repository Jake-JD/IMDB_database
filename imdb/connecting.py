import sqlite3 as sql

# conn = mysql.connect( host="localhost", database="imdb", user=dbUSer, password = dbPass )

conn = sql.connect("imdb.db")

cursor = conn.cursor()
