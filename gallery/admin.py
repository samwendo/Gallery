from django.contrib import admin
from .models import Location, Category, Photographer, Image


# Register your models here.

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Photographer)
admin.site.register(Image)

