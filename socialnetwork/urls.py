from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *


urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^index', index, name='index'),
)


