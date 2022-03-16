import coolstuff as sac
import time
import random

sac.scroll("welcome to beat up game!!!")
time.sleep(1)
sac.scroll("you fight")
time.sleep(1)
sac.clear()

p1name = input('Player 1, what is your name?: ')
p2name = input('Player 2, what is your name?: ')

p1hp = 100
p2hp = 100

gameplaying = True

# ------Gameloop------
while gameplaying:
  damagedonep1 = 0
  damageblockedp1 = 0
  damagehealedp1 = 0
  damagedonep2 = 0
  damageblockedp2 = 0
  damagehealedp2 = 0
  player1turn = True
  player2turn = False
  while player1turn == True:
      print(f'\n{p1name}\'s turn')
      pbr1 = input(f"{p1name}, would you like to block, punch, or rest? (p/b/r): ")
      #punch
      if pbr1.lower() in ["punch", "p"]:
          damagedonep1 = random.randint(5, 15)
          print('You punched \n')
          player1turn = False
      #block
      elif pbr1.lower() in ['block', 'b']:
          damageblockedp1 = random.randint(5, 10)
          print('You blocked \n')
          player1turn = False
      #rest
      elif pbr1.lower() in ['rest', 'r']:
          damagehealedp1 = random.randint(5, 10)
          print('You rested and healed \n')
          player1turn = False
      else:
          print('Please type a valid input \n')
          continue

  player1turn = False
  player2turn = True

  while player2turn == True:
      print(f'{p2name}\'s turn')
      pbr2 = input(f"{p2name}, would you like to block, punch, or rest? (p/b/r): ")
      #punch
      if pbr2.lower() in ["punch", "p"]:
          damagedonep2 = random.randint(5, 15)
          print('You punched! \n')
          player2turn = False
      #block
      elif pbr2.lower() in ['block', 'b']:
          damageblockedp2 = random.randint(5, 10)
          print('You blocked! \n')
          player2turn = False
      #rest
      elif pbr2.lower() in ['rest', 'r']:
          damagehealedp2 = random.randint(5, 10)
          print('You rested and healed! \n')
          player2turn = False
      else:
          print('Please type a valid input. \n')
          continue

  #Calculate damage
  p1hp = p1hp - damagedonep2

  if damagedonep2 <= damageblockedp1:
    damageblockedp1=damagedonep2
    p1hp = p1hp + damageblockedp1
  else:
    p1hp = p1hp + damageblockedp1

  p2hp = p2hp - damagedonep1

  if damagedonep1 <= damageblockedp2:
    damageblockedp2=damagedonep1
    p2hp = p2hp - damageblockedp2
  else:
    p2hp = p2hp + damageblockedp2
  
  p1hp = p1hp + damagehealedp1
  p2hp = p2hp + damagehealedp2

  sac.scroll(f'{p1name} has {p1hp}')
  sac.scroll(f'{p2name} has {p2hp} \n')

  if p1hp <= 0 or p2hp <= 0:
      gameplaying = False

print(f'Game ended, {p1name} had {p1hp} hp, {p2name} had {p2hp} hp')
