from django.contrib import admin

from banks import models


@admin.register(models.Bank)
class BankAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
