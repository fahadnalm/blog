from . import views
from django.conf.urls import url 

urlpatterns = [

    url(r'^text/$', views.text_search,name="text"),
    url(r'^location/$', views.place_detail, name="location"),
]