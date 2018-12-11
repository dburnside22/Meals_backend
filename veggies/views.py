from rest_framework import viewsets
from .models import Veggie
from .serializers import VeggieSerializer


class VeggieViewSet(viewsets.ModelViewSet):
    queryset = Veggie.objects.all()
    serializer_class = VeggieSerializer