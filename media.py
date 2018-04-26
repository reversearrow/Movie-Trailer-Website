class Movies():
    """
    Movie class.

    Constructor Method Attributes:
        title (str): Title of the Movie.
        poster_image_url (str): URL of the Movie Poster.
        trailer_youtube_url (str): URL of the Youtube video.

    """

    # Constructor Method.
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
