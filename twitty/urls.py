from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^twitter_test/$', views.test, name="twitter_test"),
]