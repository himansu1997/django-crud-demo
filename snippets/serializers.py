from rest_framework import serializers
from snippets.models import Vendor, Product

class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'quantity', 'stock_status','vendor')