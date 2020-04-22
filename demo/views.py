from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from demo.models import Product
from demo.serializers import DemoSerializer
from django.shortcuts import get_list_or_404, get_object_or_404

# Rest API
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','PUT', 'DELETE'])
def product_detail(request, uid=None, com_sku=None,format=None):
	"""
	Retrieve, update or delete a product instance.
	"""
	print "ee"
	product = get_object_or_404(Product, com_sku=com_sku)
	if request.method == 'GET':
		serializer = DemoSerializer(product)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = DemoSerializer(product, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		product.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def product_list(request, uid=None,format=None):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET':
    	print "fffff"
        product_list = Product.objects.all()
        serializer = DemoSerializer(product_list, many=True)
        return Response(serializer.data)