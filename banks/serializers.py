from rest_framework import serializers
from banks import models
from programs.models import Program
# from country_currencies import get_by_country
import pycountry


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bank
        fields = ["id", "name", "countries"]

class TransactionSerializer(serializers.ModelSerializer):
    countries = serializers.CharField(max_length=50, write_only=True)
    currency = serializers.CharField(max_length=3, write_only=True)

    class Meta:
        model = models.Transaction
        fields = ["id", "bank", "program", "is_eligible", "countries", "currency"]

    def create(self, validated_data):
        bank = validated_data.get('bank')
        program = validated_data.get('program')
        countries = validated_data.get('countries')
        currency = validated_data.get('currency')
        
        bank =models.Bank.objects.get(pk = bank.pk)
        program =Program.objects.get(pk = program.pk)

        is_valid = False
            
        for country in bank.countries:
            country = pycountry.countries.get(name=country)
            currency = pycountry.currencies.get(numeric=country.numeric)
            if currency.alpha_3 == program.currency:
                is_valid = True
                break
        if not is_valid: 
            raise serializers.ValidationError("currency with associated country not founrd")
        
        
        is_valid = False

        bank_obj = models.Bank.objects.all()
        is_valid = False
        for bank in bank_obj:
            if str(countries) in bank.countries:
                is_valid = True
                break
        
        if not is_valid:
            raise serializers.ValidationError("Country not matches")
        if is_valid:
            validated_data["is_eligible"] = True
        
        program_obj = Program.objects.filter(currency = currency).first()
        if program_obj is None:
            raise serializers.ValidationError("Currency not found")

        validated_data.pop('currency')
        return models.Transaction.objects.create(**validated_data)
