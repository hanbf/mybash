#!/usr/bin/env python

import sys
import os

# Configure your favorite diff program here.
MERGE = "/Applications/Araxis Merge.app/Contents/Utilities/compare"
# Get the paths provided by Subversion.
BASE   = sys.argv[1]
MINE   = sys.argv[2]
THEIRS = sys.argv[3]
MERGED = sys.argv[4]
# Call the merge command (change the following line to make sense for
# your merge program).
cmd = [MERGE, "-wait", "-a1", "-3", BASE, THEIRS, MINE, MERGED];

os.execv(cmd[0], cmd)
# Return an errorcode of 0 if the conflict was resolved; 1 otherwise.
# Any other errorcode will be treated as fatal.

