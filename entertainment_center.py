from fresh_tomatoes import open_movies_page
from media import Movies

# Creating a Movie Object called Dark Knight.
dark_knight = Movies("Dark Knight", "https://ca.movieposter.com/posters/archive/main/69/MPW-34753",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")

# Creating a Movie Object called avengers.
avengers = Movies("Avengers", "https://ca.movieposter.com/posters/archive/main/152/MPW-76269",
                  "https://www.youtube.com/watch?v=eOrNdBpGMv8")


# Creating a Movie object called matrix.
matrix = Movies("Matrix", "https://ca.movieposter.com/posters/archive/main/9/A70-4902",
                "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# Creating a list, adding movie objectes inside it.
favorite_movies = [dark_knight, avengers, matrix]

# Generates fresh_tomatoes.html page
open_movies_page(favorite_movies)
