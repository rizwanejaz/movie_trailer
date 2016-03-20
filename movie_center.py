import movie
import fresh_tomatoes

# start creating instances of Movie

hulk = movie.Movie("Hulk",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/5/59/Hulk_movie.jpg/220px-Hulk_movie.jpg",
                   "https://www.youtube.com/watch?v=xbqNb2PFKKA")


jumanji = movie.Movie("Jumanji",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Jumanji_poster.jpg/220px-Jumanji_poster.jpg",
                   "https://www.youtube.com/watch?v=OJKHQLM8AbM")


kung_fu_panda = movie.Movie("Kung Fu Panda 3",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/Kung_Fu_Panda_3_poster.jpg/220px-Kung_Fu_Panda_3_poster.jpg",
                   "https://www.youtube.com/watch?v=10r9ozshGVE")

a_bugs_life = movie.Movie("A Bug's Life",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/A_Bug%27s_Life.jpg/220px-A_Bug%27s_Life.jpg",
                   "https://www.youtube.com/watch?v=Ljk2YJ53_WI")

alvin_and_chipmunks = movie.Movie("Alvin and the Chipmunks: The Road Chip trailer",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/4/44/AlvinChipmunksTheRoadChip_poster.jpg/220px-AlvinChipmunksTheRoadChip_poster.jpg",
                   "https://www.youtube.com/watch?v=xA6cOSEZhzM")

star_wars = movie.Movie("Star Wars The Force Awakens",
                   "http://www.freedvdcover.com/wp-content/uploads/freedvdcover_star_wars_the_force_awakens_2015_custom_front-610x410.jpg",
                   "https://www.youtube.com/watch?v=l3U90zeuipU")

# We need to put the instances inside list
movies = [hulk, jumanji, kung_fu_panda, a_bugs_life, alvin_and_chipmunks, star_wars]

# open_movies_page takes a list of movies as param
fresh_tomatoes.open_movies_page(movies)
