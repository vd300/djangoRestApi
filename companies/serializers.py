from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock        #what model you want to serialize=Stock
        #fields=('ticker','volume')   #what request you want to send back
        fields = '__all__'  #dont usethis if there is an id or pk to dont want to show
