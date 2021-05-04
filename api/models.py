from django.db import models


# creating tables
class MovieList(models.Model):
    movie_title = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ["-movie_title"]

    def __str__(self):
        return self.movie_title


class MovieRatings(models.Model):
    ratings_descriptions = models.TextField(blank=True)
    published = models.DateField(auto_now=True, auto_now_add=False)
    movie_list = models.ForeignKey(
        MovieList, related_name="movie_list", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-ratings_descriptions"]

    def __str__(self):
        return self.ratings_descriptions
