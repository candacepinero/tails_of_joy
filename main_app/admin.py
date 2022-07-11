from django.contrib import admin
from .models import Pet, Feed

# Register your models here.
admin.site.register(Pet)
admin.site.register(Feed)