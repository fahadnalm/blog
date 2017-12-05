from django.conf.urls import url, include
from django.contrib import admin
from posts import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include ('posts.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^google/', include('google_app.urls')),
    url(r'^gitty/', include('gitty.urls')),
    url(r'^twitty/', include('twitty.urls')),

]

if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)