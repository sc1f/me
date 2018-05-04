from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', homepage),
    url(r'^about/$', about),
    url(r'^posts/(?P<post_slug>[-\w]+)/$', post),
    url(r'^posts/$', archive),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^(?P<category>.+)/$', landing),
    ]