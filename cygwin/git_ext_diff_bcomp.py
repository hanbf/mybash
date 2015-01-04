#!/usr/bin/env python
import sys
import os

CYGWIN_ROOT = "d:/cygwin64/"

def addCygwinRoot(path):
	if path.startswith("/"):
		path = CYGWIN_ROOT + path

	return path
	
# Configure your favorite diff program here.
# route to git ext merge tool
DIFF = "C:\Program Files (x86)\Beyond Compare 3\BComp.com"

LEFT  = sys.argv[1]
RIGHT = sys.argv[2]

LEFT = addCygwinRoot(LEFT)
RIGHT = addCygwinRoot(RIGHT)

# Call the diff command (change the following line to make sense for
# your diff program).
cmd = [DIFF, LEFT, RIGHT]
os.execv(cmd[0], cmd)
# Return an errorcode of 0 if no differences were detected, 1 if some were.
# Any other errorcode will be treated as fatal.
