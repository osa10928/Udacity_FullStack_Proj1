# Movie Trailer Website

Movie Trailer Website is code simply used to create a website of your favorite movies that also shows their trailers when the movie is clicked. It runs on python and uses the class Media to create the attributes the movie initiated with the attributes that will be shown on the static webpage. Finally, it uses a custom module 'fresh tomatoes' (thanks to Udacity), to create and launch webpage.

## Clone Repository

Can clone this git repository from your terminal by entering:
`git clone https://github.com/osa10928/Udacity_FullStack_Proj1.git`

(You can copy/paste the url by clicking the clone button on the top right)

## Specifiacations

Requires python
`'python' >= '2.7.6'`

Uses python's shell IDLE which can be easily added to you system:
`sudo apt-get install idle`

## Demo

To run a demo of this application, ensure you have met the specifications, namely they you are running at least python 2.7.6 and that you have IDLE installed. Run demo by following these instructions:
1. Launch terminal
2. Clone this repository to your device using instructions above.
3. From terminal launch idle by entering:
    `idle python`
4. Open "entertainment.py" from the idle terminal
5. From the 'run' tab select run module

After following these instructions terminal should launch the demo webpage built by this application.

## Build Your Own!!

Following these simple steps will allow you to build  a webpage populated with your favorite movies!

1. Create a "media.py" document. This will hold the class Movie which will be used to create instances of your movie
2. In thi document create a class Movie similar to the one in this repository. Give it the attributes "title", "storyline", "movie", "poster", and "youtube trailer".
3. Create a "entertainment.py" document. This will create and hold instances of you favorite movies, and launch the webpage.
4. Use the class Movie (located in the media.py file) to create your own instances of your favorite movies. Give the attributes of "title", "storyline", "movie poster", and "youtube trailer". Create as many as you want!

`berserk = media.Movie("Berserk", "An orphan becomes a mercenary that battles men and demons", "https://i.pinimg.com/564x/12/eb/2c/12eb2c2b24ef6d7fcac2bc102bf62005.jpg", "https://www.youtube.com/watch?v=XkDYnXTBrI8")`

5. To create and launch webpage we need to use the fresh_tomatoes.py document located in this repository. Copy and paste the contents of fresh_tomatoes.py located in this repository to your own fresh_tomatoes.py document located in your root folder.
6. Import fresh_tomatoes to entertainment.py. Call the function fresh_tomatoes.open_movie_page with an array of you movie instances as the argument. (It may be easier to story you movie instances in a variable)

`fresh_tomatoes.open_movies_page([the_matrix, liar_liar, everything_must_go, berserk])` or

`movies = [the_matrix, liar_liar, everything_must_go, berserk, men_in_black]`
`fresh_tomatoes.open_movies_page([movies])`
7. Finally, run module by going to the run tab and clicking, run module. You new movies webpage should launch!!

Clone repository for and follow the demo instructions for an example of how this process works, then create your own!.

## Contribution

Thanks to the Udacity team for providing 'fresh tomatoes', an abstraction that turned movie instances into a website.

