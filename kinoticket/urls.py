from django.urls import path
from kinoticket import views


urlpatterns = [
    path('', views.session),
    path('sort/', views.sort, name='sort'),
    path('seat/', views.seats, name='seat'),
    path('pay/<int:pk>', views.pay_with_robokassa, name='pay'),
]
