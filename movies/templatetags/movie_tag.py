from django import template
from movies.models import Category, Movies


register = template.Library()


@register.simple_tag()
def get_categories():
    ''' Вывод всех категории '''
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies():
    '''  '''
    movies = Movies.objects.order_by("id")[:5]
    return {"last_movies": movies}
