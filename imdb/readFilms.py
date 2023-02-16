
from connecting import *

def read():
    contindel = True
    while contindel:
        print("Enter 1: search All.\nEnter 2: search by genre.\nEnter 3: search by year.\nEnter 4: search by rating")
        option = input("Enter a number: ")
        if option == "1":
            contindel = False
            readAll()
            
        elif option == "2":
            contindel = False
            readGenre()
        
        elif option == "3":
            readYear()
            contindel = False

        elif option == "4":
            readRating()
            contindel = False
            
        else:
            print("Invalid number entered")


def readRating():
    fieldval = input("Search rating (ex. Entering 8 shows 8.0 to 8.9): ")
    fieldval = "'" + fieldval + "%'"
    cursor.execute(f"SELECT * FROM allshows WHERE rating LIKE {fieldval}")
    row = cursor.fetchall() # records fetched saved/passed in to the row varible
    for record in row:
        print(record)

def readYear():
    fieldval = input("Search by year: ")
    fieldval = "'" + fieldval + "'"
    cursor.execute(f"SELECT * FROM allshows WHERE year = {fieldval}")
    row = cursor.fetchall() # records fetched saved/passed in to the row varible
    for record in row:
        print(record)

def readGenre():
    fieldval = input("Search by genre: ")
    fieldval = "'%" + fieldval + "%'"
    cursor.execute(f"SELECT * FROM allshows WHERE genre LIKE {fieldval}")
    row = cursor.fetchall() # records fetched saved/passed in to the row varible
    for record in row:
        print(record)

def readAll():
    cursor.execute("SELECT * FROM allshows")
    row = cursor.fetchall() # records fetched saved/passed in to the row varible
    for record in row:
        print(record)

# Why use if __name__ == "__main__":?
if __name__ == "__main__":
    read()