#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from evdev import InputDevice
from select import select
import conf

params = {}
webmoteurl = ''

while True:
    (r, w, x) = select([dev], [], [])
    for event in dev.read():
        print event.value

        # scroll wheel event is 8
        # buttons left 272, right 273

        if event.code == 8:
            print 'wheel'
            print event.value
            if event.value == -1:
                print 'vol down'
                params = {'command': 'volume-down'}
                webmoteurl = 'http://localhost:8080/command'
                myheaders = {'User-Agent': 'Mozilla/5.0'}
                r = requests.post(webmoteurl, data=params,
                                 headers=myheaders)
                print r.status_code
            elif event.value == 1:
                print 'vol up'
                params = {'command': 'volume-up'}
                webmoteurl = 'http://localhost:8080/command'
                myheaders = {'User-Agent': 'Mozilla/5.0'}
                r = requests.post(webmoteurl, data=params,
                                 headers=myheaders)
                print r.status_code
        elif event.code == 272:
            print 'left button'
            print event.value
            print 'play'
            params = {'command': 'play', 'target': leftclick_play_dir}
            webmoteurl = 'http://localhost:8080/play'
            myheaders = {'User-Agent': 'Mozilla/5.0'}
            r = requests.post(webmoteurl, data=params, headers=myheaders)
            print r.status_code
        elif event.code == 273:
            print 'right button'
            print event.value
            print 'stop'
            params = {'command': 'stop'}
            webmoteurl = 'http://localhost:8080/command'
            myheaders = {'User-Agent': 'Mozilla/5.0'}
            r = requests.post(webmoteurl, data=params, headers=myheaders)
            print r.status_code