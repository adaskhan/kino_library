from django.contrib import admin

from .models import Session, History


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("film", "start_time", "end_time", "kino_teatre", "tic_price")


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ("date", "owner", "ticket")
