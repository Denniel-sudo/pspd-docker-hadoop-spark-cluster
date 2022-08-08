#!/usr/bin/env python3

import random

file1 = open("../hello.txt","a") 
file2 = open("./words.txt", "r")

PsudoRandomWords = []

for word in file2.read().split():
   PsudoRandomWords.append(f'{word} ')

index = 0
for x in range(150000000):

   index = random.randint(0,len(PsudoRandomWords) - 1)
   file1.write(PsudoRandomWords[index])

   if x % 20 == 0:
      file1.write('\n')