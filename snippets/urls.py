from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #url(r'^products/(?P<api_key>\w+)$', views.product_list),
    #url(r'^products/(?P<api_key>\w+)/(?P<id>[0-9]+)$', views.product_detail),
    url(r'^(?P<api_key>\w+)/products/(?P<id>[0-9]+)$', views.product_info),
    url(r'^(?P<api_key>\w+)/products/$', views.products_list),
]
urlpatterns = format_suffix_patterns(urlpatterns)