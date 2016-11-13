from django.conf.urls.defaults import patterns
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'lists.views.home_page', name='home'),
)
