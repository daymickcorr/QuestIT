# URL patterns for the quest app

from django.conf.urls import url
from .views import QuestDetailView, create, read, QuestListView
from django.urls import path 

urlpatterns = [
    url('create/', create),
    url('read/', read),
    #url('quest/', QuestListView.as_view()), #same as read but object based /quest/quest/ #/quest/quest/*
    path('', QuestListView.as_view()),
    path('<int:pk>', QuestDetailView.as_view(), name='questDetailView'),
]

