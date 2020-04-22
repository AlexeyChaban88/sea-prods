from landing import views
from django.conf.urls import url
from django.contrib import admin
from products import views


urlpatterns = [
    #url(r'^', views.landing, name='landing')
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]