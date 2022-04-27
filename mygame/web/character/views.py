# Views for our character app

from io import IncrementalNewlineDecoder
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from urllib3 import HTTPResponse, Retry

from evennia.utils.search import object_search
from evennia.utils.utils import inherits_from
from evennia.objects.models import ObjectDB
from evennia.utils.create import create_object
from evennia.accounts.models import AccountDB

from .forms import CharacterCreate

#create
def create(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CharacterCreate(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            user = request.user

            # Create the actual character object
            typeclass = settings.BASE_CHARACTER_TYPECLASS
            home = ObjectDB.objects.get_id(settings.GUEST_HOME)
            # turn the permissionhandler to a string
            perms = str(user.permissions)
            # https://www.evennia.com/docs/0.9.5/api/evennia.accounts.accounts.html create_character
            # create the character
            char = create_object(typeclass=typeclass, key=name,
                home=home, permissions=perms)
            user.db._playable_characters.append(char)
            # add the right locks for the character so the account can
            #  puppet it
            char.locks.add("puppet:id(%i) or pid(%i) or perm(Developers) "
                "or pperm(Developers)" % (char.id, user.id))            
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CharacterCreate()

    return render(request, 'character/create.html', { 
        'character' : request ,
        'form' : form,
        })

#read
#characterList
def read(request):
    account = AccountDB.objects.get_id(request.user.id)
    characters = account.characters
    return render(request, 'character/read.html', {'characters' : characters})

#update
def update(request):
    pass

#delete
def delete(request):
    pass

#characterDetail
def sheet(request, object_id):
    object_id = '#' + object_id
    try:
        character = object_search(object_id)[0]
    except IndexError:
        raise Http404("I couldn't find a character with that ID.")
    if not inherits_from(character, settings.BASE_CHARACTER_TYPECLASS):
        raise Http404("I couldn't find a character with that ID. "
                      "Found something else instead.")
    return render(request, 'character/sheet.html', {'character': character})

class CharacterListView(ListView, LoginRequiredMixin):
    #def get_queryset(self):
    #    queryset =  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        login_user_id = self.request.user.pk
        return context
    pass

class CharacterDetailView(DetailView):
    pass