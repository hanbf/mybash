#!/usr/bin/env python

import sys
import os

# Configure your favorite diff program here.
# route to git ext merge tool
DIFF = "/Applications/Araxis Merge.app/Contents/Utilities/compare"
# Subversion provides the paths we need as the last two parameters.
LEFT  = sys.argv[-2]
RIGHT = sys.argv[-1]
# Call the diff command (change the following line to make sense for
# your diff program).
cmd = [DIFF, "-wait", LEFT, RIGHT]
os.execv(cmd[0], cmd)
# Return an errorcode of 0 if no differences were detected, 1 if some were.
# Any other errorcode will be treated as fatal.
