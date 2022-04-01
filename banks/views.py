from rest_framework import mixins, serializers, viewsets

# from rest_framework.generics import GenericAPIView
from banks.serializers import BankSerializer, TransactionSerializer
from banks import models


class BankViewSet(viewsets.ModelViewSet):
    queryset = models.Bank.objects.all()
    serializer_class = BankSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = models.Transaction.objects.all()
