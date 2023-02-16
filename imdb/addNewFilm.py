import time
from connecting import *



# subroutine
def insertNewFilm():
    
    film = []
    contin = True
    while contin:

        try:
            rank = int(input("Rank on IMDB: "))
            name = input("name of film: ")
            year = input("year: ")
            rating = float(input("rating (1 - 10): "))
            genre = input("genre: ")
            certificate = input("certificate: ")
            run_time = input("run_time: ")
            tagline = input("tagline: ")
            budget = input("budget: ")
            box_office = input("box_office: ")
            directors = input("directors: ")
            writers = input("writers: ")
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
            

        # Rating = input("How would you rate the film (U, PG, 12+, 15+, 18+): ")
        # Genre = input("Genre of the film: ")

        contin = False


    # YearReleased = int(YearReleased)
    # duration = int(duration)
    # append data to the list called members
    film.append(rank)
    film.append(name)
    film.append(year)
    film.append(rating)
    film.append(genre)
    film.append(certificate)
    film.append(run_time)
    film.append(tagline)
    film.append(budget)
    film.append(box_office)
    film.append(directors)
    film.append(writers)

    
    cursor.execute("INSERT INTO allshows VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", film)
    #commit any pending transaction to the songs table in the database
    conn.commit()

    print(f"{name} inserted in the allshows table")
    time.sleep(3)

    #read from the members table
    # call the read subroutine from the readMembers python file
 

if __name__ == "__main__":
    insertNewFilm()
