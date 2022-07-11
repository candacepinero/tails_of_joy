from operator import mod
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    lives_in = models.CharField(max_length=100)
    personality = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pet_id': self.id})

    def fed_for_today(self):
        return self.feed_set.filter(date=date.today()).count()
    

class Feed(models.Model):
    date = models.DateField()

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return self.date

    class Meta:
        ordering = ['-date']