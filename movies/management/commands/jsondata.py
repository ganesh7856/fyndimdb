# import os
import json
import requests
from movies.models import Movie,Genre



from django.core.management.base import BaseCommand

url = 'https://imdbmovies1.herokuapp.com/moviedbsave/'


json_file ='imdb.json'


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#
#
#         with open(json_file) as f:
#             json_data = json.loads(f.read())
#             for index, each_json in enumerate(json_data, start=1):
#                 try:
#                     requests.post(url,auth=('ganesh', 'ganesh'), data=each_json)
#                     if requests.status_code == 200:
#                         print('Successful')
#                 except Exception as e:
#                     # print(index, ']',  each_json['name'])
#                     pass

class Command(BaseCommand):

    def handle(self, *args, **options):
        json_path = json_file
        with open(json_path) as f:
            data = json.load(f)
            genre_set = set()
            genre_dict = {}
            movie_list = []
            for _movie in data:
                movie = _movie.copy()
                genres = movie.get('genres', [])
                for g in genres:
                    genre_set.add(g.strip())
                movie['popularity'] = movie['99popularity']
                del movie['99popularity']
                del movie['genre']

                movie_list.append(Movie(**movie))

            for genre in list(genre_set):
                stripped_name = genre.strip()
                g, created = Genre.objects.get_or_create(name=stripped_name)
                genre_dict[stripped_name] = g

            Movie.objects.bulk_create(movie_list)
            all_movies = Movie.objects.all()
            for i, movie in enumerate(data, start=0):
                genres = []
                for genre in movie.get('genres', []):
                    genres.append(genre_dict[genre.strip()])

                all_movies[i].genres.add(*genres)