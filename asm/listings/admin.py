from django.contrib import admin
from .models import Anime, Series, Movies

# Register your models here.

class AsmAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slugs": ("title",)}

admin.site.register(Anime)
admin.site.register(Movies)
admin.site.register(Series)