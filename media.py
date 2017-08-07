# This is the file that has the classes.
#Code is orginal, though follows the Udacity course pretty closely.
class Video():
    """Parent of anything that is a video. Contains Title, Time Length, and year released"""
    def __init__(self, title, duration, year_released):
        self.title = title
        self.duration = duration
        self.year_released = year_released

class Movie(Video):
    """Contains log line, poster url, trailer url, and rating + parent"""
    VALID_RATINGS = ["G","PG","PG-13","R","NC-17","NR"]
    #"Log Line" is a movie industry term. Usually used to pitch a movie idea in a single sentence.
    #e.g. 'A former slaver and a nobleman's son team up to resolve the appearances of ghosts in the city of Waterdeep' -Ghosts of Skullport
    #e.g. 'A child's favorite toy's status is threatened with the arrival of new Space Toy action figure.' -Toy Story
    def __init__(self, title, duration, year_released, log_line, poster, trailer, country, rating):
        Video.__init__(self, title, duration, year_released)
        self.log_line = log_line
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.country = country
        if rating.upper() in self.VALID_RATINGS:
            self.rating = rating.upper()
        else:
            self.rating = "NR"
    def show_all(self):
        print "Title: ",self.title
        print "Duration: ",self.duration
        print "Year: ",self.year_released
        print "Logline: ",self.log_line
        print "Poster Address: ",self.poster
        print "Trailer Address: ",self.trailer_youtube_url
        print "Country: ",self.country
        print "Rating: ",self.rating
