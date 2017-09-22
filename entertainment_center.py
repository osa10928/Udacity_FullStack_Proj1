# import media which holds the class movie
# import fresh_tomatoes which holds the function that builds the website
import media
import fresh_tomatoes


# create instances of the Movie for each movie we want to show
the_matrix = media.Movie(
    "The Matrix", "Man leaves Dreamworld to fight AI overlords",
    "http://www.impawards.com/1999/posters/matrix_ver1.jpg",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8")
liar_liar = media.Movie(
    "Liar Liar", "A man can't lie",
    "https://fanart.tv/detailpreview/fanart/movies/1624/movieposter/liar-liar-54cd232f5e082.jpg",  # noqa
    "https://www.youtube.com/watch?v=C1no75lpOiw")
men_in_black = media.Movie(
    "Men In Black", "A movie about agents working with aliens",
    "http://www.joblo.com/posters/images/full/1997-men-in-black-poster1.jpg",
    "https://www.youtube.com/watch?v=1Q4mhYF9aQQ")
everything_must_go = media.Movie(
    "Everything Must Go", "A man lives on his lawn after a divorce",
    "http://www.impawards.com/2011/posters/everything_must_go.jpg",
    "https://www.youtube.com/watch?v=MZC-s2oNLT0")
the_lion_king = media.Movie(
    "The Lion King", "A prince lion must become king",
    "http://www.impawards.com/1994/posters/lion_king_ver7.jpg",
    "https://www.youtube.com/watch?v=4sj1MT05lAA")
berserk = media.Movie(
    "Berserk", "an orphan battles men then demons",
    "https://i.pinimg.com/564x/12/eb/2c/12eb2c2b24ef6d7fcac2bc102bf62005.jpg",
    "https://www.youtube.com/watch?v=XkDYnXTBrI8")


# place all the movies in an array to serve as an argument for
# fresh_tomatoes which uses the function open_movie_page to
# create and open the movie page
movies = [
    the_matrix, liar_liar, everything_must_go,
    berserk, men_in_black, the_lion_king]
fresh_tomatoes.open_movies_page(movies)
