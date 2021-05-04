from django.shortcuts import render
from api.models import MovieList, MovieRatings
from api.serializers import MovieListSerializers, MovieRatingSerializer, CreateMovieSerializer, RatingsMovieSerializer
from rest_framework import viewsets, mixins, views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ListMovie(views.APIView):
    """
    List all movies
    """

    def get(self, request, format=None):
        if request.method == "GET":
            movies = MovieList.objects.all()
            serializer = MovieListSerializers(movies, many=True)
            return Response(serializer.data)
    # permission_classes = [IsAuthenticated, ]

    # def post(self, request, format=None):
    #     serializer = MovieListSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create movie


class CreateMovie(views.APIView):
    """
    Create a movie
    """

    def post(self, request, format=None):
        serializer = MovieListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Show detail movie


class MovieDetails(views.APIView):
    """
    Retrieve pk and update movie
    """

    def get_object(self, pk):
        try:
            return MovieList.objects.get(pk=pk)
        except MovieList.DoesNotExist:
            content = {'Oops': 'nothing to see here'}
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        movies = self.get_object(pk)
        serializer = MovieListSerializers(movies)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        if request.method == "PUT":
            movies = self.get_object(pk)
            serializer = RatingsMovieSerializer(movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update movie


class UpdateMovie(views.APIView):
    def get_object(self, pk):
        try:
            return MovieList.objects.get(pk=pk)
        except MovieList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        movies = self.get_object(pk)
        serializer = MovieListSerializers(movies)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        if request.method == "PUT":
            movies = self.get_object(pk)
            serializer = RatingsMovieSerializer(movies, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete movie


class DeleteMoview(views.APIView):
    def get_object(self, pk):
        try:
            return MovieList.objects.get(pk=pk)
        except MovieList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        if request.method == "DELETE":
            movie = self.get_object(pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
