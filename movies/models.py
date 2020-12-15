from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    imdb_score = models.FloatField()
    popularity = models.FloatField(verbose_name='99popularity')

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)
    # movie = models.ForeignKey(Movie, related_name='geners', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='genres',related_query_name='genre' ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


