#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip()
  words = line.split()
  for word in words:
    if len(word) == 6 or len(word) == 8 or len(word) == 11:
      print('%s\t%s' % (len(word), 1))