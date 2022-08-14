from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models import ForeignKey

import movies.models


class Session(models.Model):
    film = models.ForeignKey(movies.models.Movies, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    kino_teatre = models.CharField(max_length=200)
    tic_price = models.IntegerField()

    @property
    def is_past_due(self):
        return date.today() < self.start_time


class History(models.Model):
    date = models.DateTimeField()
    owner = ForeignKey(User, on_delete=models.CASCADE)
    ticket = ForeignKey(Session, on_delete=models.CASCADE)

    @property
    def is_past_due(self):
        return date.today() > self.date