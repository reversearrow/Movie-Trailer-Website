from fresh_tomatoes import open_movies_page


class Movies():
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


dark_knight = Movies("Dark Knight", "https://ca.movieposter.com/posters/archive/main/69/MPW-34753",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")
avengers = Movies("Avengers", "https://ca.movieposter.com/posters/archive/main/152/MPW-76269",
                  "https://www.youtube.com/watch?v=eOrNdBpGMv8")


favorite_movies = [dark_knight, avengers]

open_movies_page(favorite_movies)
