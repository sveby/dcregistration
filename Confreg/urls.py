from django.conf.urls import patterns, include, url
from Confreg import views

urlpatterns = patterns('',
    #forms
    url(r'^$', views.index, name="index"), 
    url(r'^(?P<conference_id>\d+)/$', views.show_registration, name='show_registration'),
    url(r'^(?P<conference_id>\d+)/company/$', views.register_company, name='register_company'),
    url(r'^(?P<conference_id>\d+)/person/$', views.register_person, name='register_person'),
)