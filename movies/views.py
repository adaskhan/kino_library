from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movies


class MoviesView(ListView):
    ''' Список фильмов '''
    model = Movies
    queryset = Movies.objects.filter(draft=False)
    # template_name = 'movies/movies_list.html'
    context_object_name = 'movie_list'


class MovieDetailView(DetailView):
    """ Полное описание фильма """
    model = Movies
    slug_field = "url"
    context_object_name = 'movie'

