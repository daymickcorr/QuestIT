# URL patterns for the character app

from django.conf.urls import url
from .views import sheet

#sheet/123/
urlpatterns = [
    url(r'^sheet/(?P<object_id>\d+)/$', sheet, name="sheet")
]

