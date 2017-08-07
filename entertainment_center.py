#Joel Gonzaga submission
#This page is all original Code
# Purpose of this document is to auto-create a website with input from both 'media.py' and 'fresh_tomatoes.py'
import media
import fresh_tomatoes
import random

#Below are 9 total movie objects. Input is Title, film duration, year, logline, poster URL, youtube linke URL, country of orgin, and rating.
#"Logline" is a film industry term. It is used to describe a movie in a single sentence.

# 1. "The Witch" - scary movie!
the_witch = media.Movie("The VVitch",
                        "1 hour, 32 minutes",
                        "2015",
                        "A 17th new England family disintergrates in the face of evil near their isolated homestead",
                        "https://upload.wikimedia.org/wikipedia/en/b/bf/The_Witch_poster.png",
                        "https://www.youtube.com/watch?v=iQXmlf3Sefg",
                        "United States",
                        "R")

# 2. "Metropolis" - mid 20th century sci-fi anime!
metropolis = media.Movie("Metropolis",
                         "1 hour, 48 minutes",
                         "2001",
                         "Kenichi and his uncle Shunsaku Ban become entangled with an ambitious industrialist, a lost robot girl, and political struggles of a plutocratic city-state.",
                         "https://upload.wikimedia.org/wikipedia/en/f/ff/Metropolisanime_poster.jpg",
                         "https://www.youtube.com/watch?v=ifl-N4RBpVI",
                         "Japan",
                         "PG-13")

# 3. "Hackers" - She's got a 55.6k bps modem!
hackers = media.Movie("Hackers",
                      "1 hour, 47 minutes",
                      "1995",
                      "A high school hacker and friends become the scapegoat of a corporate conspiracy.",
                      "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg",
                      "https://www.youtube.com/watch?v=Rn2cf_wJ4f4",
                      "United States",
                      "PG-13")

# 4. "Snatch" - London criminals: the unlucky, the brutal, and the incompentent!
snatch = media.Movie("Snatch",
                     "1 hour, 42 minutes",
                     "2001",
                     "An underground boxing promotor must answer to his murderous boss after a gypsy knocks out their prize fighter in one punch.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA2NDYxOGYtYjU1Mi00Y2QzLTgxMTQtMWI1MGI0ZGQ5MmU4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_SX684_AL_.jpg",
                     "https://www.youtube.com/watch?v=ni4tEtuTccc",
                     "United Kingdom",
                     "R")

# 5. "Secret Things" - maybe NSFW!
secret_things = media.Movie("Secret Things",
                            "1 hour, 55 minutes",
                            "2002",
                            "Two young, struggling, Parisian women use sex for pleasure and power at a corporate bank.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Choses_secrets_cover.jpg/440px-Choses_secrets_cover.jpg",
                            "https://www.youtube.com/watch?v=6Vk1_0p6haU",
                            "France",
                            "NR")

# 6. "The Lives of Others" - if only the NSA was this nice!
lives_of_others = media.Movie("The Lives of Others",
                              "2 hours 17 minutes",
                              "2006",
                              "In 1984 East Berlin, a politically rigid secret police agent empathizes with the artists spies on.",
                              "https://upload.wikimedia.org/wikipedia/en/9/9f/Leben_der_anderen.jpg",
                              "https://www.youtube.com/watch?v=FppW5ml4vdw",
                              "Germany",
                              "R")

# 7. "Secret of NIMH" - how the hell did this get a 'G' rating?!
secret_of_nimh = media.Movie("The Secret of NIMH",
                             "1 hour, 22 minutes",
                             "1982",
                             "A field mouse appeals to a colony of rats to save her sick son.",
                             "https://upload.wikimedia.org/wikipedia/en/8/84/The_Secret_of_NIMH.jpg",
                             "https://www.youtube.com/watch?v=cISmv0IGoQQ",
                             "United States",
                             "G")

# 8. "Stargate" - Look! Sci-fi when they still used puppets!
stargate = media.Movie("Stargate",
                       "1 hour, 56 minutes",
                       "1994",
                       "A pariah archeologist joins a military expedition to another planet ruled by the Egyptian god Ra.",
                       "https://upload.wikimedia.org/wikipedia/en/e/e0/Stargateposter.jpg",
                       "https://www.youtube.com/watch?v=kiJtZUPvJxY",
                       "United States",
                       "PG-13")

# 9. "Yojimbo" - Watch once, watch again. You rooted for the pyscho both times!
yojimbo = media.Movie("Yojimbo",
                      "1 hour, 50 minutes",
                      "1961",
                      "A ronin manipulates two warring gangs against each other as they destory an occupied town.",
                      "https://upload.wikimedia.org/wikipedia/en/8/8b/Yojimbo_%28movie_poster%29.jpg",
                      "https://www.youtube.com/watch?v=y_1iT_GmHTE",
                      "Japan",
                      "NR")

#The fucntion below is used to randomize the movies.
#The movies will appear in random order on the output HMTL file.
ordered_list = [the_witch,metropolis,hackers,snatch,secret_things,lives_of_others,secret_of_nimh,stargate,yojimbo]
random_movie_list = []
def make_random_movie_list(ordered_list):
    while len(ordered_list) > 0: # '0' here implies an empty list.
        start_of_list = 0
        end_of_list = len(ordered_list) -1
        randomly_choosen_film = ordered_list.pop(random.randint(start_of_list,end_of_list))
        random_movie_list.append(randomly_choosen_film)

#Runs the functions that make the website.
#Both functions must run in this order.
make_random_movie_list(ordered_list)
fresh_tomatoes.open_movies_page(random_movie_list)
