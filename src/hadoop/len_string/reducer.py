#!/usr/bin/env python3
import sys

curr_len_word = None
curr_count = 0
len_word = None

for line in sys.stdin:
  line = line.strip()
  
  len_word, count = line.split('\t', 1)
  try:
    count = int(count)
  except ValueError:
    continue
  if curr_len_word == len_word:
    curr_count += count
  else:
    if curr_len_word:
      print('%s\t%s' % (curr_len_word, curr_count))
    curr_count = count 
    curr_len_word = len_word

if curr_len_word == len_word:
  print('%s\t%s' % (curr_len_word, curr_count))
