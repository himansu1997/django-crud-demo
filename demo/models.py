from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=150)
	retail_sku = models.CharField(max_length=60)
	com_sku = models.CharField(max_length=30)
	offer_status = models.BooleanField(default=True)


class Customer(models.Model):
	name = models.CharField(max_length=60)
	email = models.CharField(max_length=60)
	cookie = models.CharField(max_length=60)
	country = models.CharField(max_length=60)
	state = models.CharField(max_length=60)
	city = models.CharField(max_length=60)
	ip = models.CharField(max_length=60)
