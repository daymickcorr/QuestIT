"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""
from django.conf.urls import url, include
from django.urls import path

#add web directory to pythonpath to support standard django
import sys
sys.path.append('/home/vagrant/mygame/web')

# default evennia patterns
from evennia.web.urls import urlpatterns

# eventual custom patterns
custom_patterns = [
    # url(r'/desired/url/', view, name='example'),
]

# this is required by Django.
urlpatterns = custom_patterns + urlpatterns
