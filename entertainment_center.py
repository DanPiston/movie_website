import media
import fresh_tomatoes

# Create instances of Movie Class

usual_suspects = media.Movie(
        'The Usual Suspects',
        'Who is Keyser Soze?',
        'https://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg', # NOQA
        'https://www.youtube.com/watch?v=oiXdPolca5w')


hot_fuzz = media.Movie(
        'Hot Fuzz',
        "Everything isn't as peachy as it seems.",
        'http://www.impawards.com/2007/posters/hot_fuzz.jpg',
        'https://www.youtube.com/watch?v=ayTnvVpj9t4')


force_awakens = media.Movie(
        'The Force Awakens',
        '30 years after the destruction of the second Death Star',
        'https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg', # NOQA
        'https://www.youtube.com/watch?v=sGbxmsDFVnE')

deadpool = media.Movie(
        'Deadpool',
        'Chimichangas?',
        'https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg',
        'https://www.youtube.com/watch?v=gtTfd6tISfw')

guardians = media.Movie(
        'Guardians of the Galaxy',
        'Protectors of the Universe?',
        'https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg',
        'https://www.youtube.com/watch?v=d96cjJhvlMA')

kubo = media.Movie(
        'Kubo and the Two Strings',
        'Adventures of Kubo, the one eyed boy.',
        'https://upload.wikimedia.org/wikipedia/en/c/c4/Kubo_and_the_Two_Strings_poster.png', # NOQA
        'https://www.youtube.com/watch?v=p4-6qJzeb3A')


# Place movies into a list to iterate through
movies = [usual_suspects, hot_fuzz, force_awakens, deadpool, guardians, kubo]

# Call fresh_tomatoes module to generate HTML
fresh_tomatoes.open_movies_page(movies)
