from django.contrib import admin
from .models import Chapter, Series, Genre

# Register your models here.
admin.site.register(Chapter)
admin.site.register(Series)
admin.site.register(Genre)