from django.conf import settings
from django.conf.urls.defaults import patterns, url

from nc_viewer.views import MainPageView

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

    url(r'^$', MainPageView.as_view(), name="home"),
    url(r"^static/(?P.*)$", "django.views.static.serve",
    		{"document_root": settings.STATIC_ROOT}),
)
