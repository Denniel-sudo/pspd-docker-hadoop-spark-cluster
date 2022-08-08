#!/usr/bin/env python3
import sys

curr_word = None
curr_count = 0
word = None

for line in sys.stdin:
  line = line.strip()
  
  word, count = line.split('\t', 1)
  try:
    count = int(count)
  except ValueError:
    continue
  if curr_word == word:
    curr_count += count
  else:
    if curr_word:
      print('%s\t%s' % (curr_word, curr_count))
    curr_count = count 
    curr_word = word

if curr_word == word:
  print('%s\t%s' % (curr_word, curr_count))
