from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

#Add dajaxice
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'DCRegistration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    #Conferences namespace:
    #url(r'^conference/', include('Conference.urls', namespace='conf')),
    
    #Registrations namespace:
    url(r'^register/', include('Confreg.urls', namespace='reg')),
    
    #Django Ajax URLs:
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

#Added because Dajaxice needs it:
urlpatterns += staticfiles_urlpatterns()
