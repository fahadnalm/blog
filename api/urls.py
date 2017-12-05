from django.conf.urls import url
from api.views import *


urlpatterns = [
    url(r'^api_list/$', PostListAPIView.as_view(), name="api_list"),
    url(r'^api_detail/(?P<post_slug>[-\w]+)/$', PostDetailAPIView.as_view(), name="api_detail"),
    url(r'^api_update/(?P<post_slug>[-\w]+)/$', PostUpdateAPIView.as_view(), name="api_update"),
    url(r'^api_delete/(?P<post_slug>[-\w]+)/$', PostDeleteAPIView.as_view(), name="api_delete"),
    url(r'^api_create/$', PostCreateAPIView.as_view(), name="api_create"),
    url(r'^comment/api_list/$', CommentListAPIView.as_view(), name="comment_list"),
	url(r'^comment/api_create/$', CommentCreateAPIView.as_view(), name="comment_create"),
	url(r'^register/$', UserCreateAPIView.as_view(), name="register"),
	url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
]
