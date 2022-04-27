from django.shortcuts import render
from .models import Quest

from django.views.generic import ListView, DetailView #for QuestListView
# Create your views here.

#create
def create(request):
    #create quests
    pass
#read 
def read(request):
    #get all public quests 
    quests = Quest.objects.all(); #all returns queryset get returns object
    return render(request, 'quest/read.html', {'quests' : quests })
#update 
def update(request):
    #update existing quest 
    pass
#delete
def delete(request):
    #delete exiting quest
    pass

#same as read but object based 
class QuestListView(ListView): 
    model = Quest

class QuestDetailView(DetailView):
    model = Quest
    #handles error 400 if id not found and stuff like that 