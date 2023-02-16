from connecting import *


def delete():
    contindel = True
    while contindel:
        print("Enter 1: Delete by imdb rank.\nEnter 2: Delete by name")
        option = input("Enter 1 or 2: ")
        if option == "1":
            contindel = False
            deleteByID()
        elif option == "2":
            contindel = False
            deleteByTitle()
        else:
            print("Invalid number entered")

def deleteByID():
    idField = input("Enter the imdb rank of the record to be deleted: ")
    cursor.execute(f"DELETE FROM allshows WHERE imdbrank = {idField}")
    conn.commit()
    print(f"Record {idField} deleted in the allshows table")

def deleteByTitle():
    titleField = input("Enter the name of the film you want deleted: ")
    titleField = "'" + titleField + "'"
    cursor.execute(f"DELETE FROM allshows WHERE name = {titleField}")
    conn.commit()
    print(f"Record {titleField} deleted in the allshows table")

if __name__ == "__main__":
    delete()