from django.contrib import admin
from .models import MovieList, MovieRatings

# Register your models here.
admin.site.register(MovieList)
admin.site.register(MovieRatings)
