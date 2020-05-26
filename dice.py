#!/usr/bin/env python3
import random
import sys

#if no args roll a normal 6-sided die
if (len(sys.argv) < 2):
  print ("Rolling die: ")
  print (random.randint(1,6))
#else for rach arg roll a die of arg[i] sides if the arg is a number else skip it.
else:
  for sidedDie in sys.argv:
    if (sidedDie == "dice.py"):
      print (" ")
      #Don't want to try to turn "dice.py" into an integer.
    else:
      print ("Rolling %s sided die: " % sidedDie)
      sides = int(sidedDie)
      print (random.randint(1,sides))
      print " "

