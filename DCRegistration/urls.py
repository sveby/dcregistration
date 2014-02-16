from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'DCRegistration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    #Conferences namespace:
    #url(r'^conference/', include('Conference.urls', namespace='conf')),
    
    #Registrations namespace:
    #url(r'^register/', include('Confreg.urls', namespace='reg')),
)
