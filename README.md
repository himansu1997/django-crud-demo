# DjangoRestAPI
Django REST framework is a powerful and flexible toolkit for building Web APIs.
First API Project:
Build api for vendor. Vendor can browse their catalog by Stock status/produt_id/category/all default is  all and also he can insert,update and delete products using our api.
Ex:
# Get all products
http://127.0.0.1:8000/<api_key>/products/
Ref: first-api-all-products-by-vendor.png

# Insert product
http://127.0.0.1:8000/<api_key>/products/
Ref: first-api-insert-product.png

#################################################################################################
# Secound API Project
Build api for store offer products by user. We stored offer products and users in database by store. 
# List of offer products by User id
Ex:http://127.0.0.1:8000/products/<user_id>/

Ref:secound-api-all-offer-products-by-user_id.png


# offer products by User id and SKU
http://127.0.0.1:8000/products/<user_id>/<com_sku>/

Ref:secound-api-offer-prduct-sku-and-user-id.png

