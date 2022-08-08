#!/usr/bin/env python3
import sys

curr_letter = None
curr_count = 0
letter = None

for line in sys.stdin:
  line = line.strip()
  
  letter, count = line.split('\t', 1)
  try:
    count = int(count)
  except ValueError:
    continue
  if curr_letter == letter:
    curr_count += count
  else:
    if curr_letter:
      print('%s\t%s' % (curr_letter, curr_count))
    curr_count = count 
    curr_letter = letter

if curr_letter == letter:
  print('%s\t%s' % (curr_letter, curr_count))
