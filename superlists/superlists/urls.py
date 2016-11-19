from django.conf.urls import patterns, include, url
from lists import views
from lists import urls

urlpatterns = patterns('',
    url(r'^$', 'views.home_page', name='home'),
    url(r'^lists/', include(urls)),
)
