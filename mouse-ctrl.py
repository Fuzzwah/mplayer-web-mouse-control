#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
from evdev import InputDevice
from select import select
import conf 

params = {}
webmoteurl = ''
dev = InputDevice(conf.mouse)

while True:
    (r, w, x) = select([dev], [], [])
    for event in dev.read():

        # scroll wheel event is 8
        # buttons left 272, right 273

        if event.code == 8:
            if event.value == -1:
                params = {'command': 'volume-down'}
                webmoteurl = 'http://localhost:{}/command'.format(conf.httpport)
                myheaders = {'User-Agent': 'Mozilla/5.0'}
                r = requests.post(webmoteurl, data=params,
                                 headers=myheaders)
            elif event.value == 1:
                params = {'command': 'volume-up'}
                webmoteurl = 'http://localhost:{}/command'.format(conf.httpport)
                myheaders = {'User-Agent': 'Mozilla/5.0'}
                r = requests.post(webmoteurl, data=params,
                                 headers=myheaders)
        elif event.code == 272:
            params = {'command': 'play', 'target': conf.leftclick_play_dir}
            webmoteurl = 'http://localhost:{}/play'.format(conf.httpport)
            myheaders = {'User-Agent': 'Mozilla/5.0'}
            r = requests.post(webmoteurl, data=params, headers=myheaders)
        elif event.code == 273:
            params = {'command': 'stop'}
            webmoteurl = 'http://localhost:{}/command'.format(conf.httpport)
            myheaders = {'User-Agent': 'Mozilla/5.0'}
            r = requests.post(webmoteurl, data=params, headers=myheaders)
