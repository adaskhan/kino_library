from django.urls import path, include
from kinoticket.views import session, seats, pay_with_robokassa

from . import views

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("json-filter/", views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
    path("session/<int:pk>/", session, name='session'),
    path("seat/<int:pk>/", seats, name='seat'),
    path("pay/<int:pk>/", pay_with_robokassa, name='pay'),
]
