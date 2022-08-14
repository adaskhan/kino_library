from django.db import models


class Contact(models.Model):
    ''' Подписка по емайл '''
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
