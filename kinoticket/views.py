from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from kinoticket.models import History, Session
from movies.models import Movies


def session(request, pk):
    film = Movies.objects.get(pk=pk)
    sessions = Session.objects.filter(film=film).order_by('start_time')
    return render(request, 'kinoticket\sessions.html', {'sessions': sessions, 'film': film})


def sort(request, pk):
    film = Movies.objects.get(pk=pk)
    sessions = Session.objects.filter(film=film).order_by('kino_teatre')
    return render(request, 'kinoticket/sessions.html', {'sessions': sessions, 'film': film})


def history(request):
    his = History.objects.filter(owner=request.user)
    time = timezone.now()
    return render(request, 'kinoticket/history.html', {'his': his, 'time': time})


def deleteticket(request, pk):
    History.objects.get(pk=pk).delete()
    his = History.objects.filter(owner=request.user)
    return render(request, 'kinoticket/history.html', {'his': his})


def seats(request, pk):
    return render(request, 'kinoticket/cinema.html', {'pk': pk})


def pay_with_robokassa(request, pk):
    order = get_object_or_404(Session, pk=pk)
    # History.objects.create(date=timezone.now(), owner=request.user, ticket=order)
    # form = forms(initial={
    #            'OutSum': order.tic_price,
    #            'InvId': order.pk,
    #            'Desc': order.film.name,
    #            'Email': request.user.email,
    #            # 'IncCurrLabel': '',
    #            # 'Culture': 'ru'
    #        })

    return render(request, 'kinoticket/pay.html', {'order': order})
