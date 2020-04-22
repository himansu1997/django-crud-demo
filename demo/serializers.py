from rest_framework import serializers
from demo.models import Product

class DemoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'retail_sku', 'com_sku')