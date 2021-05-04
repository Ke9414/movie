from rest_framework import serializers
from .models import MovieList, MovieRatings

# creating serializers


class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRatings
        fields = ['movie_list', 'ratings_descriptions']


class MovieListSerializers(serializers.ModelSerializer):
    movie_list = MovieRatingSerializer(read_only=True, many=True)

    class Meta:
        model = MovieList
        fields = ['movie_title', 'movie_list']


class CreateMovieSerializer(serializers.Serializer):
    movie_title = serializers.CharField(max_length=50)
    movie_list = serializers.IntegerField()

    def create(self, validated_data):
        return MovieList.objects.create(validated_data)


class RatingsMovieSerializer(serializers.ModelSerializer):
    movie_list = CreateMovieSerializer(many=True, read_only=True)

    class Meta:
        model = MovieRatings
        fields = [
            'id',
            'ratings_descriptions',
            'movie_list'
        ]

    def update(self, instance, validated_data):
        ratings = validated_data.pop('movie_list')
        instance.movie_title = validated_data.get(
            "movie_title", instance.movie_title)
        instace.save()

        keep_movie_list = []
        existing_data = [c.id for c in instance.movie_list]
        for rating in ratings:
            if "id" in rating.keys():
                if MovieList.objects.filter(id=rating["id"]).exists():
                    c = MovieList.objects.get(id=rating["id"])
                    c.movie_title = rating.get('movie_title')
                    c.movie_list = rating.get('movie_list')
                    c.save()
                    keep_movie_list.append(c.id)
                if MovieRatings.objects.filter(id=rating["id"]).exists():
                    c = MovieRatings.objects.get(id=rating["id"])
                    c.movie_list = rating.get('movie_list')
                    c.ratings_descriptions = rating.get('ratings_descriptions')
                    c.save()
                    keep_movie_list.append(c.id)

    # def create(self, validated_data):
    #     movie_list = validated_data.pop('movie_list')
    #     ratings = MovieList.objects.create(**validated_data)

    #     for movie in movie_list:
    #         MovieRatings.objects.create(
    #             **movie_list, ratings_descriptions=ratings)
    #     return ratings

    # def create(self, validated_data):
    #     movie_data = validated_data.pop('movie_list')
    #     ratings = MovieRatings.objects.create(**validated_data)
    #     for movies_data in movie_data:
    #         MovieList.objects.create(movie_title=ratings, **movies_data)
    #     return ratings

    # def update(self, instance, validated_data):
    #     movie_data = validated_data.pop('movie_list')
    #     ratings = (instance.movie_list).all()
    #     ratings = list(ratings)
    #     print("===>", ratings)
    #     instance.movie_title = validate_data.get(
    #         'movie_title', instance.movie_title)
    #     instance.ratings_descriptions = validated_data.get(
    #         'ratings_descriptions', instance.ratings_descriptions)
    #     instance.save()

    #     for movies_data in movie_data:
    #         print("====>", movies_data.ratings_descriptions)
    #         rating = ratings.pop(0)
    #         rating.movie_title = movies_data.get(
    #             'movie_title', movies_data.movie_title)
    #         rating.ratings_descriptions = movies_data.get(
    #             'ratings_descriptions', movies_data.ratings_descriptions)
    #         ratings.save()
    #     return instance

    # def create(self, validated_data):
    #     return MovieList.objects.create(validated_data)


# class MovieListSerializers(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     movie_title = serializers.CharField(max_length=50)

#     def create(self, validated_date):
#         return MovieList.objects.create(validated_date)

#     def update(self, instance, validated_date):
#         instance.movie_title = validated_date.get(
#             'movie_title', instance.movie_title)
#         instance.save()
#         return instance
