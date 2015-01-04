#!/usr/bin/env python

import sys
import os

CYGWIN_ROOT = "d:/cygwin64/"

def addCygwinRoot(path):
	if path.startswith("/"):
		path = CYGWIN_ROOT + path

	return path

# Configure your favorite diff program here.
MERGE = "C:\Program Files (x86)\Beyond Compare 3\BComp.com"

# Get the paths provided by Subversion.
BASE   = addCygwinRoot(sys.argv[1])
MINE   = addCygwinRoot(sys.argv[2])
THEIRS = addCygwinRoot(sys.argv[3])
MERGED = addCygwinRoot(sys.argv[4])
# Call the merge command (change the following line to make sense for
# your merge program).
cmd = [MERGE, BASE, THEIRS, MINE, MERGED];

os.execv(cmd[0], cmd)
# Return an errorcode of 0 if the conflict was resolved; 1 otherwise.
# Any other errorcode will be treated as fatal.

