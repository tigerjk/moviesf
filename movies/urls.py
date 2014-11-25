from django.conf.urls import url, patterns, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from movies import views
from sfmovie import settings
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^search', views.get_movies, name='get_movies'),
	url(r'^find', views.find_movies, name='find_movies'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
