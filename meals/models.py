from django.db import models

class Meal(models.Model):
    day = models.CharField(max_length=200)
    breakfast = models.CharField(max_length=200, null=True, blank=True)
    lunch = models.CharField(max_length=200, null=True, blank=True)
    dinner = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
      return self.day