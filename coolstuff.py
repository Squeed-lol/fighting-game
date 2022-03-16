import os
import sys
import time

# define our clear function
def clear():
  
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

# Scroll
def scroll(str, speed=0.03):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(speed)
  print()