from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dproject.views.home', name='home'),
    # url(r'^dproject/', include('dproject.foo.urls')),
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
