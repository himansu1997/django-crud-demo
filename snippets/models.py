from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
import hashlib

class Vendor(models.Model):
    name = models.CharField(max_length=64)
    api_key = models.CharField(max_length=50)
    site_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['site_id',]

    def save(self, *args, **kwargs):
        key_string = self.name
        salt = "djangorestapi#123"
        self.api_key = hashlib.md5( salt + key_string ).hexdigest()
        super(Vendor, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(null=True)
    stock_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vendor = models.ForeignKey(Vendor, related_name="product_vendor")

    class Meta:
        ordering = ['category']

    def __unicode__(self):
        return self.name