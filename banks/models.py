import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField
from programs.models import Program


class Bank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(unique=True)
    countries = ArrayField(models.TextField(), default=list, blank=True)


class Transaction(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    is_eligible = models.BooleanField(default=False)
    countries = models.CharField(max_length=50)