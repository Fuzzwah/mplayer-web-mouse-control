#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list of directories which contain things we might want to play
root = ["/home/pi/music"]

# the directory where the mp3s which should be played on left mouse button click
leftclick_play_dir = "/home/pi/music/World Lullabies"

# the input/event# of your mouse, confirm with evtest
mouse = "/dev/input/event2"

## what port do you want the HTTP server to listen on
httpport = 8080
