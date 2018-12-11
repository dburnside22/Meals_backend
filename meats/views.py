from rest_framework import viewsets
from .models import Meat
from .serializers import MeatSerializer


class MeatViewSet(viewsets.ModelViewSet):
    queryset = Meat.objects.all()
    serializer_class = MeatSerializer
