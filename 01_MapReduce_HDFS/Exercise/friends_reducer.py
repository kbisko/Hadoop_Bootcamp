#!/usr/bin/env

from operator import itemgetter
import sys

current_name = None
current_count = 0
current_reviews = None
name = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    name, reviews, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_name == name:
        current_count += count
        current_reviews == reviews
    else:
        if current_name:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_name, current_reviews, current_count)
        current_count = count
        current_name = word
        current_reviews = reviews

# do not forget to output the last word if needed!
if current_name == name:
    print '%s\t%s\t%s' % (current_name, current_reviews, current_count)