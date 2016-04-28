## MPlayer Web and Mouse Remote Control

A Python based HTTP server which passes commands to mplayer from a website and mouse buttons.

#### Purpose

I've rigged this system up to run on a headless raspberry pi (running raspbian) in my baby's bedroom. It allows us to trigger playback of a music play list which we call our 'sleepy baby bedtime megamix'. Playback can be controlled either by clicking buttons on a wireless mouse which sits on the change table or via a webpage accessed from either a computer or our Android phones. The intial idea was to allow me to kick off playback in the middle of the night with out getting out of bed, if we heard our baby stirring.

The mouse controls are: left button starts playback, right button stops playback, mouse wheel to control volume up or down.

It is a fork of https://github.com/Inaimathi/web-mote which was created with an interface suited to an iPod touch. I have modified the style sheet to make it suitable for use on an Android phone. I then added all the mouse control functions.

Note: the page will not work in Chrome for Android. It will work in standard Android Browser with out issue.

#### Installation

1) Download the zip or clone the repo into a directory in your home directory.

2) If you're on Raspbian, Debian or Ubuntu, you can install everything else you need by running the following commands:

    sudo apt-get install git mplayer python-setuptools python-pip build-essential python-dev evtest 
    sudo easy_install tornado
    sudo pip install --upgrade pip 
    sudo pip install requests evdev

3) Configure a few things, open each of the following files in a text editor and find the config section to get things set up:

    nano mplayer-web-mouse-remote-control
    nano conf.py

4a) If you want to run the system as a service do the following:

    sudo chmod 755 main.py
    sudo chmod 755 mouse-ctrl.py    
    sudo cp mplayer-web-mouse-remote-control /etc/init.d/
    sudo chmod 755 /etc/init.d/mplayer-web-mouse-remote-control
    sudo update-rc.d mplayer-web-mouse-remote-control defaults

4b) Or you can fire the two python scripts and stick them into the background using screen:

    sudo apt-get install screen
    screen -dmS mplayer-web sudo python main.py
    screen -dmS mplayer-mouse sudo python mouse-ctrl.py

Then you can attach to each screen using `screen -r mplayer-web` or `screen -r mplayer-mouse` and detach with `Ctrl+a Ctrl+d`.

#### Usage

1. navigate to `http://[machine ip]` to use the remote web menu
2. click the left mouse button to trigger playback
3. click the right mouse button to stop playback
4. use the mouse wheel to control the volume

#### Dependencies

- [Python 2.7](http://python.org/download/releases/2.7/)
- [mplayer](http://www.mplayerhq.hu/design7/news.html)
- [GNU Screen](http://www.gnu.org/software/screen/)
- Python [tornado](http://www.tornadoweb.org/) module

#### Licensing/Components
This program is released under the GNU AGPL (check the `LICENSE` file for details).

The favicon is a remote control icon designed by [FatCow - Udderly Fantastic Hosting](http://www.fatcow.com/) and released under [CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/us/)

The front-end uses [Twitter Bootstrap](https://github.com/twitter/bootstrap) for styling, which is released under the [Apache License](https://github.com/twitter/bootstrap/blob/master/LICENSE)

I've added [Font Awesome](http://fortawesome.github.io/Font-Awesome/) for the icons. It is released under a [SIL OFL 1.1 / MIT License](http://fortawesome.github.io/Font-Awesome/license/)

A copy of the fantastic [Angular.js](http://angularjs.org/) is included for ease of use. It's released under an [MIT-style expat license](https://github.com/angular/angular.js/blob/master/LICENSE)
