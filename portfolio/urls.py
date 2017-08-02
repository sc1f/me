from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', homepage),
    url(r'^about/$', about),
    url(r'^posts/(?P<post_slug>[-\w]+)/$', post),
    url(r'^archive/$', archive)
    ]