"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""
from django.conf.urls import url, include
from django.urls import path

# default evennia patterns
from evennia.web.urls import urlpatterns

# eventual custom patterns
custom_patterns = [
    # url(r'/desired/url/', view, name='example'),
    path('character/', include('web.character.urls')),
    path('quest/', include('web.quest.urls')),
]

# this is required by Django.
urlpatterns = custom_patterns + urlpatterns
