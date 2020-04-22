from landing import views
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^landing/', views.landing, name='landing'),
    url(r'^$', views.home, name='home'),
    url(r'^info$', views.info, name='info'),
]







