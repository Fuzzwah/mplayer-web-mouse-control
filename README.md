## Web-Mote

A web-based interface for MPlayer written in Python.

It is a fork of https://github.com/Inaimathi/web-mote which was created with an interface suited to an iPod touch. I have modified the style sheet to make it suitable for use on an Android phone.

Note: the page will not work in Chrome for Android. It will work in Dolphin Browser with out issue.

#### Usage

1. install the dependencies
2. run `python main.py`
3. navigate to `http://[machine ip]:8080` to use the remote menu

You can run it in the background using GNU Screen. Assuming you have it installed, you start a background server with `screen -dmS web-mote python main.py`, attach to it using `screen -r web-mote` and detach with `Ctrl+a Ctrl+d`.

#### Dependencies

- [Python 2.7](http://python.org/download/releases/2.7/)
- [mplayer](http://www.mplayerhq.hu/design7/news.html)
- OPTIONALLY [omxplayer](https://github.com/huceke/omxplayer) *if you're on [Raspbian](http://www.raspbian.org/), you already have this. If you're not, you probably don't need it.*
- OPTIONALLY [GNU Screen](http://www.gnu.org/software/screen/) *you'll need this or similar to run web-mote in the background*
- Python [tornado](http://www.tornadoweb.org/) module

If you're on Debian or Raspbian, you can install everything you need by running the following as `root`:

    sudo apt-get install mplayer screen python-setuptools
    sudo easy_install tornado

#### Licensing/Components
This program is released under the GNU AGPL (check the `LICENSE` file for details).

The favicon is a remote control icon designed by [FatCow - Udderly Fantastic Hosting](http://www.fatcow.com/) and released under [CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/us/)

The front-end uses [Twitter Bootstrap](https://github.com/twitter/bootstrap) for styling, which is released under the [Apache License](https://github.com/twitter/bootstrap/blob/master/LICENSE)

I've added [Font Awesome](http://fortawesome.github.io/Font-Awesome/) for the icons. It is released under a [SIL OFL 1.1 / MIT License](http://fortawesome.github.io/Font-Awesome/license/)

A copy of the fantastic [Angular.js](http://angularjs.org/) is included for ease of use. It's released under an [MIT-style expat license](https://github.com/angular/angular.js/blob/master/LICENSE)
