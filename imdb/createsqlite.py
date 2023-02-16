import sqlite3 as sql
conn = sql.connect("imdb.db")


# cursor.execute("CREATE DATABASE imdb")

cursor = conn.cursor()


# cursor.execute(""" CREATE TABLE "allshows" (
#     "imdbrank" INT NOT NULL UNIQUE,
#     "name" TEXT NOT NULL,
#     "year" TEXT NOT NULL,
#     "rating" FLOAT NOT NULL,
#     "genre" TEXT NOT NULL,
#     "certificate" TEXT NOT NULL,
#     "run_time" TEXT NOT NULL,
#     "tagline" TEXT NOT NULL,
#     "budget" TEXT NOT NULL,
#     "box_office" TEXT NOT NULL,
#     "directors" TEXT NOT NULL,
#     "writers" TEXT NOT NULL,
#     PRIMARY KEY ("imdbrank") )""")

    