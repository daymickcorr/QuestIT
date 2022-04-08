QuestIT
=======================

Description:
------------
The idea behind this project is to create a social game where
you get rewarded by ingame features trough real life quests.

Think of `Habitica`_ but with the rewards you would buy in the
store would be available inside a world for you and your freinds!

The goal of this is to stimulate social interaction through common
tasks.

An example of a task would be to end an arcade game like `volgarr`_
and the reward could be a viking sword inside `Evennia`_, you would 
be aware other ingame players that has this sword would of had played 
this game and you could share your experience, the ingame rewards are
there to motivate the group to perform common tasks.

How to contribute:
------------------
Currently this project is in developpment and not available in production.

This repository contains a vagrantfile allowing to create the servers needed
to work on this project this tool is used so we all share the same infrastructure

Requirements:
To work on this project you will need to install `git`_, `vagrant`_ and `virtualbox`_ virtualbox
was chosen because it does not have requirements

Getting Started:
- From `github.com`_ fork https://github.com/daymickcorr/QuestIT.git
- git clone https://github.com/myaccount/QuestIT.git
- cd QuestIT #change to the directory of the source code 
- vagrant up #create the servers
- vagrant ssh #connect to the servers 
- cd .. 
- evennia migrate #create intial database
- evennia start #start 

Server will be available at http://localhost:4001

What now ?:
- Look around the ui 
- Try the evennia `tutorial`_

typeclasses and web should be the 2 folders to start looking at for the code
`object-documentation`_
`web-documentation`_

QuestIT
       - mygame
            - commands #ingame actions
            - server #server settings and logs 
            - typeclasses #ingame objects
            - web #webui based on django
            - world #what does not seem to go in the other folders goes here
       - bootstrap.sh #post-process install for the system image based on debian 10
       - vagrantfile #creates and configures virtualbox vms for this project

Wokring on the code:
You can change code either on you localhost (QuestIT/mygame) or the virtualbox
vm (/home/vagrant/mygame) the mygame directory is shared between the 2 

Testing the code:
`Start-Stop-Reload-Evennia`_ 

Debugging:
Currently `pdb`_
Interrested in `ptvsd`_

Sharing your test code:
QuestIT >$ git commit -m "message" #send your code to your repo 
https://github.com/myaccount/QuestIT.git
QuestIT >$ git push
From `github.com`_ New pull request 

Tools I recommend to make your life easier:
`GitAhead`_ Manage git with a ui
`Visual-Studio-Code`_  Code editor 
`ngrok`_ share your web ui with QuestIT $> vagrant share --http 4001
`vagrant-vbguest`_ manages virtualbox guest additions
`vagrant-share`_ ngrok

.. _Habitica: https://habitica.com/
.. _volgarr: https://store.steampowered.com/app/247240/Volgarr_the_Viking/
.. _Evennia: https://www.evennia.com/docs/latest/Getting-Started.html
.. _git: https://git-scm.com/downloads
.. _vagrant: https://www.vagrantup.com/downloads
.. _virtualbox: https://www.virtualbox.org/wiki/Downloads
.. _github.com: https://github.com/
.. _tutorial: https://www.evennia.com/docs/0.9.5/Tutorial-World-Introduction.html
.. _object-documentation: https://www.evennia.com/docs/0.9.5/Objects.html
.. _web-documentation: https://www.evennia.com/docs/0.9.5/Add-a-simple-new-web-page.html
.. _Start-Stop-Reload-Evennia: https://www.evennia.com/docs/0.9.5/Start-Stop-Reload.html
.. _pdb: https://www.evennia.com/docs/1.0-dev/Coding/Debugging.html
.. _ptvsd: https://donjayamanne.github.io/pythonVSCodeDocs/docs/debugging_remote-debugging/
.. _GitAhead: https://github.com/gitahead/gitahead/releases
.. _Visual-Studio-Code: https://code.visualstudio.com/
.. _ngrok: https://ngrok.com/
.. _vagrant-vbguest: https://github.com/dotless-de/vagrant-vbguest
.. _vagrant-share: https://www.vagrantup.com/docs/share