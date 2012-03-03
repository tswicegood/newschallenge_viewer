from django.conf.urls.defaults import patterns, include, url
from django.views.generic.list import ListView

from project.nc_viewer.models import Entry

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newschallenge_viewer.views.home', name='home'),
    # url(r'^newschallenge_viewer/', include('newschallenge_viewer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', ListView.as_view(queryset=Entry.objects.filter(invalid=False)), name="home")
)
