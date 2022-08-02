from django.contrib import admin
from .models import Category, Movies, MovieShots, RatingStar, Rating, Reviews, Genre, Actor
# Register your models here.


admin.site.register(Category)
admin.site.register(Movies)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(Genre)
admin.site.register(Actor)
