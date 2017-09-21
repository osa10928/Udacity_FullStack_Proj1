# Movie Trailer Website

Movie Trailer Website is code simply used to create a website of your favorite movies that also shows their trailers when the movie is clicked. It runs on python and uses the class Media to create the attributes the movie initiated with the attributes that will be shown on the static webpage. Finally, it uses a custom module 'fresh tomatoes' (thanks to Udacity), to create and launch webpage.

## Specifiacations

Runs on python
`'python' >= '2.7.6'`

## Usage

Use the class Movie (located in the media file) to create your an instance of your favorite movie. Give the attributes of "title", "storyline", "movie poster", and "youtube trailer".

`berserk = media.Movie("Berserk", "An orphan becomes a mercenary that battles men and demons", "https://i.pinimg.com/564x/12/eb/2c/12eb2c2b24ef6d7fcac2bc102bf62005.jpg", "https://www.youtube.com/watch?v=XkDYnXTBrI8")`

To create website call open_movies_page (using 'fresh tomatoes') on an array of movie instances:

`fresh_tomatoes.open_movies_page([the_matrix, liar_liar, everything_must_go, berserk])`

Clone repository for an example.

## Clone Repository

`git clone https://github.com/osa10928/Udacity_FullStack_Proj1.git`
(You can copy/paste the url by clicking the clone button on the top right)

## Contribution

Thanks to the Udacity team for providing 'fresh tomatoes', an abstraction that turned movie instances into a website.

