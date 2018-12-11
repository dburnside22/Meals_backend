from rest_framework import viewsets
from .models import Meal
from .serializers import MealSerializer

# Create your views here.
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer