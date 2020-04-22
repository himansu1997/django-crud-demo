from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Product, Vendor
from snippets.serializers import SnippetSerializer
from django.shortcuts import get_list_or_404, get_object_or_404

# Rest API
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


#  Normal API
class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def product_list(request,id=None,api_key=None):
	"""
	List all code products, or create a new product.
	"""
	vendor = get_object_or_404(Vendor, api_key=api_key)
	if request.method == 'GET':
		products = Product.objects.filter(vendor=vendor)
		serializer = SnippetSerializer(products, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)



@csrf_exempt
def product_detail(request,id=None,api_key=None):
	"""
	Retrieve, update or delete a code product.
	"""
	vendor = get_object_or_404(Vendor, api_key=api_key)
	product = Product.objects.filter(id=id,vendor=vendor)
	product = product[0]

	if request.method == 'GET':
		serializer = SnippetSerializer(product)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(product, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		product.delete()
		return HttpResponse(status=204)


# Rest API

@api_view(['GET', 'PUT', 'DELETE'])
def product_info(request, id=None, api_key=None,format=None):
	"""
	Retrieve, update or delete a product instance.
	"""
	vendor = get_object_or_404(Vendor, api_key=api_key)
	product = Product.objects.filter(id=id,vendor=vendor)
	if product:
		product = product[0]
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SnippetSerializer(product)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SnippetSerializer(product, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		product.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def products_list(request, api_key=None,format=None):
    """
    List all products, or create a new product.
    """
    vendor = get_object_or_404(Vendor, api_key=api_key)
    if request.method == 'GET':
        products = Product.objects.filter(vendor=vendor)
        serializer = SnippetSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)