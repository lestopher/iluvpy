from django.conf.urls import patterns, url
from tracker import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^/createUser/$', views.createUser, name='createUser'),
    url(r'^/dashboard/$', views.dashboard, name='dashboard'),
    url(r'^/auth/$', views.auth, name='auth'),
    url(r'^/logout/$', views.userLogout, name='userLogout'),
    url(r'^/setGoalWeight/$', views.setGoalWeight, name='setGoalWeight'),
)
