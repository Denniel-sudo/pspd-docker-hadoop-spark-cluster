#!/usr/bin/env python3

import sys

for line in sys.stdin:
  line = line.strip()
  words = line.split()
  for word in words:
    word = word.upper()
    letter = word[0]

    if letter == 'S' or letter == 'P' or letter == 'R':
      print('%s\t%s' % (letter, 1))