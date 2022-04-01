from rest_framework import serializers, viewsets

from programs import models


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Program
        fields = ("id", "name", "currency", "return_percentage",)


