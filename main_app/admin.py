from django.contrib import admin
from .models import Pet, Feed, Photo

# Register your models here.
admin.site.register(Pet)
admin.site.register(Feed)
admin.site.register(Photo)