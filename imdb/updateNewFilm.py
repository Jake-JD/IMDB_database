from connecting import *


def update():
    contin = True
    while contin:
        print("Enter 1: Update by ID.\nEnter 2: Update by title")
        option = input("Enter 1 or 2: ")
        if option == "1":
            contin = False
            updateByRank()
        elif option == "2":
            contin = False
            updateByTitle()
        else:
            print("Invalid number entered")


def updateByTitle():
    titleField = input("Enter the film name: ")
    

    titleContin = True
    while titleContin:
        fieldName = input("Enter field name ('name'/'year'/'rating'/'genre'/'certificate'/'run_time'/'tagline'/'budget'/'box_office'/'directors'/'writers'): ")
        print(fieldName)
        if fieldName == "name" or fieldName == "year" or fieldName == "rating" or fieldName == "genre" or fieldName == "certificate" or fieldName == "run_time" or fieldName == "tagline" or fieldName == "budget" or fieldName == "box_office" or fieldName == "directors" or fieldName == "writers":
            print("CORRECT VAL ENTERED ============================")
            titleContin = False
        else:
            titleContin = True

    newFieldValue = input(f"Enter the value for the field: {fieldName}: ")

    # print(newFieldValue)
    newFieldValue = "'" + newFieldValue + "'"
    titleField = "'" + titleField + "'"
    # print(newFieldValue)

    
    
    cursor.execute(f"UPDATE allshows SET {fieldName} = {newFieldValue} WHERE name = {titleField}")

    
    conn.commit()

    print(f"Record {titleField} updated in the allshows table")
  



def updateByRank():
     # SongID is the unique / primary key
    idField = input("Enter the Rank of the record to be updated: ")
    # field name to be updated
    fieldName = input("Enter field name ('name'/'year'/'rating'/'genre'/'certificate'/'run_time'/'tagline'/'budget'/'box_office'/'directors'/'writers'): ")

    newFieldValue = input(f"Enter the value for the field: {fieldName}: ")

    # print(newFieldValue)
    newFieldValue = "'" + newFieldValue + "'"
    # print(newFieldValue)

    # print(f"UPDATE allshows SET {fieldName} = {newFieldValue} WHERE imdbrank = {idField}")
    cursor.execute(f"UPDATE allshows SET {fieldName} = {newFieldValue} WHERE imdbrank = {idField}")
    conn.commit()

    print(f"Record {idField} updated in the allshows table")
    # time.sleep(3)

if __name__ == "__main__":
    update()