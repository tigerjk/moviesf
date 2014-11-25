from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfmovie.views.home', name='home'),
    url(r'^movies/', include('movies.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
