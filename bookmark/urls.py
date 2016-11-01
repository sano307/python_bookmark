from django.conf.urls import url
from bookmark.views import *

urlpatterns = [
    # Class-based views
    url(r'^$', BookmarkLV.as_view(), name='index'),
    url(r'^(?P<ph>\d+)/$', BookmarkDV.as_view, name='detail'),
]