from rest_framework import viewsets
from .models import Dish
from .serializers import DishSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
