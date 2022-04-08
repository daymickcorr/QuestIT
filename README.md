QuestIT
=======================

Description:
------------
The idea behind this project is to create a social game where
you get rewarded by ingame features trough real life quests.

Think of [Habitica](https://habitica.com/) but with the rewards you would buy in the
store would be available inside a world for you and your freinds!

The goal of this is to stimulate social interaction through common
tasks.

An example of a task would be to end an arcade game like [volgarr](https://store.steampowered.com/app/247240/Volgarr_the_Viking/)
and the reward could be a viking sword inside [Evennia](https://www.evennia.com/docs/latest/Getting-Started.html), you would 
be aware other ingame players that has this sword would of had played 
this game and you could share your experience, the ingame rewards are
there to motivate the group to perform common tasks.

How to contribute:
------------------
Currently this project is in developpment and not available in production.

This repository contains a vagrantfile allowing to create the servers needed
to work on this project this tool is used so we all share the same infrastructure

**Requirements:**

To work on this project you will need to install [git](https://git-scm.com/downloads), [vagrant](https://www.vagrantup.com/downloads) and [virtualbox](https://www.virtualbox.org/wiki/Downloads) virtualbox
was chosen because it does not have requirements

**Getting Started:**

- From https://github.com/ fork https://github.com/daymickcorr/QuestIT.git
- git clone https://github.com/myaccount/QuestIT.git
- cd QuestIT #change to the directory of the source code
- vagrant up #create the servers
- vagrant ssh #connect to the servers 
- cd ..
- evennia migrate #create intial database
- evennia start #start

Server will be available at http://localhost:4001

**What now ?:**

Look around the ui <br/>
Try the evennia [tutorial](https://www.evennia.com/docs/0.9.5/Tutorial-World-Introduction.html)

typeclasses and web should be the 2 folders to start looking at for the code

[object-documentation](https://www.evennia.com/docs/0.9.5/Objects.html)<br/>
[web-documentation](https://www.evennia.com/docs/0.9.5/Add-a-simple-new-web-page.html) 

```console
├── mygame
│   ├── commands #ingame actions 
│   ├── server #server settings and logs
│   ├── typeclasses #ingame objects
│   ├── web #webui based on django
│   └── world #what does not seem to go in the other folders goes here
├── Vagrantfile #creates and configures virtualbox vms for this project
└── bootstrap.sh #post-process install for the system image based on debian 10
```

**Wokring on the code:**

You can change code either on you localhost (QuestIT/mygame) or the virtualbox
vm (/home/vagrant/mygame) the mygame directory is shared between the 2 

**Testing the code:**

[Start-Stop-Reload-Evennia](https://www.evennia.com/docs/0.9.5/Start-Stop-Reload.html)  

**Debugging:**

Currently [pdb](https://www.evennia.com/docs/1.0-dev/Coding/Debugging.html)<br/>
Interrested in [ptvsd](https://donjayamanne.github.io/pythonVSCodeDocs/docs/debugging_remote-debugging/)

**Sharing your test code:**

QuestIT >$ git commit -m "message" #send your code to your repo https://github.com/myaccount/QuestIT.git <br/>
QuestIT >$ git push<br/>
From [github.com](https://github.com/) New pull request <br/>

**Tools I recommend to make your life easier:**

[GitAhead](https://github.com/gitahead/gitahead/releases) Manage git with a ui <br/>
[Visual-Studio-Code](https://code.visualstudio.com/)  Code editor <br/>
[ngrok](https://ngrok.com/) share your web ui with QuestIT $> vagrant share --http 4001 <br/>
[vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest) manages virtualbox guest additions <br/>
[vagrant-share](https://www.vagrantup.com/docs/share) ngrok <br/>
