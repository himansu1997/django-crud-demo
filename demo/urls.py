from django.conf.urls import url
from demo import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^products/$', views.product_list),
    url(r'^products/(?P<uid>\w+)/$', views.product_list),
    url(r'^products/(?P<uid>\w+)/(?P<com_sku>\w+)/$', views.product_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)