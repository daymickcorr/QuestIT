# URL patterns for the character app

from django.conf.urls import url
from .views import CharacterListView, sheet, create, read
from django.urls import path, re_path 

#sheet/123/
urlpatterns = [
    url('create/', create),
    #url('read/', read), 
    #url(r'^sheet/(?P<object_id>\d+)/$', sheet, name="sheet"),
    path('', read, name="characterListView"), 
    re_path(r'^(?P<object_id>\d+)/$', sheet, name="characterDetailView"),

]

