from rest_framework import serializers

from .models import Veggie

class VeggieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Veggie
        fields = '__all__'