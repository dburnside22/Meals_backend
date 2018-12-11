from rest_framework import serializers

from .models import Meat

class MeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meat
        fields = '__all__'