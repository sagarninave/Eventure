from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.views import index

urlpatterns = [
	url(r'^$', index),
	url(r'^admin/', admin.site.urls),
 	url(r'^home/', include('home.urls')),
 	url(r'^events/', include('events.urls')),
 	url(r'^gallery/', include('gallery.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
