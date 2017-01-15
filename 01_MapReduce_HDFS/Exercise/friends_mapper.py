#!/usr/bin/env python2.7

import sys
import json

# input comes from STDIN (standard input)
for line in sys.stdin:
    jj = json.loads(line)
    for h in jj['friends']:
        #print '%s\t%s' % (u, h["text"])
        print '%s\t%s\t%i\t%i' % (jj['name'],jj['review_count'], 1)