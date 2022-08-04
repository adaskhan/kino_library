from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movies, Category, Actor
from .forms import ReviewForm


class MoviesView(ListView):
    ''' Список фильмов '''
    model = Movies
    queryset = Movies.objects.filter(draft=False)
    # template_name = 'movies/movies_list.html'
    context_object_name = 'movie_list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context


class MovieDetailView(DetailView):
    """ Полное описание фильма """
    model = Movies
    slug_field = "url"
    context_object_name = 'movie'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        return context


class AddReview(View):
    ''' Отзывы '''
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movies.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(DetailView):
    ''' Вывод информации о актера '''
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = "name"
