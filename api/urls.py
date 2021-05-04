from django.urls import path, include
from api.views import ListMovie, CreateMovie, MovieDetails, UpdateMovie, DeleteMoview
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("ListMovie", ListMovie)
# router.register("RatingsMovie", RatingsMovie)

urlpatterns = [
    path("list/", ListMovie.as_view()),
    path("create/", CreateMovie.as_view()),
    path("detail/<int:pk>", MovieDetails.as_view()),
    path("update/<int:pk>", UpdateMovie.as_view()),
    path("delete/<int:pk>", DeleteMoview.as_view()),
]
