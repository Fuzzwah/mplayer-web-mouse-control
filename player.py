from subprocess import Popen, PIPE, call
from threading import Thread
import sys
is_py2 = sys.version[0] == '2'
if is_py2:
    import queue as queue
else:
    import queue as queue
import os
import util, conf
from main import ServerStatus

############################################################
### MASSIVE AMOUNTS OF CONFIG (this should probably be in a DB somewhere)
############################################################
defaultPlayer = ["mplayer"]

### If `omxplayer` is available, use it for `mp4`s and `ogv`s (with audio output to the HDMI port)
### If not, use the default player for everything
playerTable = {}

commandTable = {
    'mplayer':
        {'step-backward': "\x1B[B", 'backward': "\x1B[D", 'forward': "\x1B[C", 'step-forward': "\x1B[A",
         ## down | left | right | up
         'volume-down': "9", 'volume-off': "m", 'volume-up': "0",
         'stop': "q", 'pause': " ", 'play': " "},
    }
### END THE MASSIVE CONFIG
############################################################
try:
    commandqueue ## Global multi-process queue to accept player commands
    playQ        ## Global multi-process queue to accept files to play
except:
    commandqueue = queue()
    playQ = queue()

def listen():
    while True:
        aFile = playQ.get()
        if util.isInRoot(aFile):
            ServerStatus.send(util.nameToTitle(aFile), event='playing')
            playerCmd = __getPlayerCommand(aFile)
            cmdTable = commandTable[playerCmd[0]]
            playFile(playerCmd, aFile, cmdTable)

def playFile(playerCmd, fileName, cmdTable):
    __clearqueue(commandqueue)
    activePlayer = Popen(playerCmd + [fileName], stdin=PIPE)
    while activePlayer.poll() == None:
        try:
            res = commandqueue.get(timeout=1)
            activePlayer.stdin.write(cmdTable[res])
            if unicode(res) == unicode("stop"):
                ServerStatus.send(util.nameToTitle(fileName), event="stopped")
                __clearqueue(playQ)
                activePlayer.terminate()
                return False
        except:
            None
    ServerStatus.send(util.nameToTitle(fileName), event="finished")
    return True

### Local Utility
def __getPlayerCommand(filename):
    global playerTable, defaultPlayer
    name, ext = os.path.splitext(filename)
    return playerTable.get(ext[1:], defaultPlayer)

def __clearqueue(q):
    while not q.empty():
        q.get()
    return True

### Start the player process
playerThread = Thread(target=listen, args=())
playerThread.daemon = True
playerThread.start()
