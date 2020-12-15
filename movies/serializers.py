from rest_framework import serializers
from .models import Movie,Genre


class MovieSerializer(serializers.ModelSerializer):

 genres = serializers.SlugRelatedField(many=True,slug_field='name',queryset=Genre.objects.all())

 class Meta:
         model = Movie
         fields = '__all__'

class GenerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields =['name',]




class MovieDBSerializer(serializers.ModelSerializer):

    genres = GenerSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        Genres_data = validated_data.pop('genres')
        movie = Movie.objects.create(**validated_data)
        for genre in Genres_data:
            Genre.objects.create(movie=movie, **genre)
        return movie



# class GenerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gener
#         fields = '__all__'
#
# class MovieSerializer(serializers.ModelSerializer):
#
#     geners = GenerSerializer(many=True)
#
#     class Meta:
#         model = Movie
#         fields = '__all__'
#
#     def create(self, validated_data):
#         Geners_data = validated_data.pop('tracks')
#         movie = Movie.objects.create(**validated_data)
#         for track_data in Geners_data:
#             Gener.objects.create(album=movie, **Geners_data)
#         return movie

    #
    # geners = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name',
    #      )
    #
    # class Meta:
    #     model = Movie
    #     fields = '__all__'

