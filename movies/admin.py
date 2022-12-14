from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Category, Movies, MovieShots, RatingStar, Rating, Reviews, Genre, Actor
# Register your models here.

from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from modeltranslation.admin import TranslationAdmin


class MovieAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movies
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    list_display_links = ("name", )


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="100"')

    get_image.short_description = "Изображение"


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft", "get_poster")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft", )
    actions = ["publish", "unpublish"]
    form = MovieAdminForm
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"), )
        }),
        (None, {
            "fields": (("description", "poster", "get_poster"),)
        }),
        (None, {
            "fields": (("year", "world_primier", "country"),)
        }),
        (None, {
            "fields": (("actors", "directors", "genre", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        (None, {
            "fields": (("url", "draft"),)
        }),
    )

    readonly_fields = ("get_poster",)

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="120"')

    get_poster.short_description = "Постер"

    def unpublish(self, request, queryset):
        """ Снять с публикации """
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        """ Oпубликовать """
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Oпубликовать'
    publish.allowed_permission = ('change', )

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permission = ('change',)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Rating)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ("star", "movie", "ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Movies)
# admin.site.register(MovieShots)
admin.site.register(RatingStar)
# admin.site.register(Rating)
# admin.site.register(Reviews)
# admin.site.register(Genre)
# admin.site.register(Actor)

admin.site.site_title = 'Кинобиблиотека'
admin.site.site_header = 'Кинобиблиотека'
