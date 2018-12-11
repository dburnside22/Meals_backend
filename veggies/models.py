from django.db import models

# Create your models here.
class Veggie(models.Model):
    name = models.CharField(max_length=200)
    breakfast_food = models.BooleanField(default=False)
    lunch_food = models.BooleanField(default=False)
    dinner_food = models.BooleanField(default=False)


    def __str__(self):
        return self.name