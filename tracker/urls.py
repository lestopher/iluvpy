from django.conf.urls import patterns, url
from weighttracker import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index')
)
