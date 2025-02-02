from os import name
from django.urls import path, include
from django.conf.urls import url
from rest_framework import views
from rest_framework.urlpatterns import format_suffix_patterns
from countries import views
#from countries.views import countries_list, countries_detail
#from .views import countries_list, countries_detail

urlpatterns = [
    url(r'^api/countries$', views.countries_list),
    url(r'^api/countries/(?P<pk>[0-9]+)$', views.countries_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)