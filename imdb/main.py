from connecting import *
import addNewFilm
import updateNewFilm
import DeleteFilms
import readFilms

# cursor.execute("DROP TABLE allshows")

# cursor.execute("TRUNCATE allshows")

# cursor.execute("DELETE FROM allshows WHERE Title = 'test1'")

# conn.commit()

def showDB():
    cursor.execute("SHOW DATABASES")
    for dbs in cursor:
        print(dbs)
        
def showTables():
    cursor.execute("SHOW TABLES")
    for tables in cursor:
        print(tables)

def showAll():
    cursor.execute("SELECT * FROM allshows")
    for row in cursor:
        print(row)


def createTable():
    cursor.execute(
        """ CREATE TABLE `imdb`.`allshows` (
        `imdbrank` INT NOT NULL,
        `name` VARCHAR(68) NOT NULL,
        `year` VARCHAR(45) NOT NULL,
        `rating` FLOAT NOT NULL,
        `genre` VARCHAR(45) NOT NULL,
        `certificate` VARCHAR(45) NOT NULL,
        `run_time` VARCHAR(45) NOT NULL,
        `tagline` VARCHAR(320) NOT NULL,
        `budget` VARCHAR(45) NOT NULL,
        `box_office` VARCHAR(45) NOT NULL,
        `directors` VARCHAR(65) NOT NULL,
        `writers` VARCHAR(58) NOT NULL,
        PRIMARY KEY (`imdbrank`),
        UNIQUE INDEX `rank_UNIQUE` (`imdbrank` ASC) VISIBLE);
        """)


def menu():
    while True:
        print("\nEnter 1: Read IMDB.\nEnter 2: Add films.\nEnter 3: Update film.\nEnter 4: Delete film.\nEnter 5: Exit")
        option = input("\nEnter number: ")
        if option == "1":
            # continMenu = False
            readFilms.read()
            menu()
        elif option == "2":
            # continMenu = False
            addNewFilm.insertNewFilm()
            menu()
        elif option == "3":
            # continMenu = False
            updateNewFilm.update()
            menu()
        elif option == "4":
            # continMenu = False
            DeleteFilms.delete()
            menu()
        elif option == "5":
            quit()
        else:
            print("Invalid number entered")
    
menu()
# createTable()
# showDB()
# showAll()
# menu()