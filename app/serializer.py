# serializer.py
from rest_framework import serializers

from app.models import Person

# convert from/to json
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'