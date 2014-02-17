from django.conf.urls import patterns, include, url
from Confreg import views

urlpatterns = patterns('',
    #forms
    url(r'^$', views.index, name="index"), 
    url(r'^(?P<conference_id>\d+)/$', views.show_registration, name='show_registration'),
)