from rest_framework import serializers, viewsets
from programs import models


from programs.serializers import ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet,):
    queryset = models.Program.objects.all()
    serializer_class = ProgramSerializer