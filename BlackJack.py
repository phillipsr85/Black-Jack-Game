import os
import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

run= True
clear = lambda: os.system('cls')

def calculate_total(hand):
  running_total= 0
  for card in hand:
    running_total += card
    return running_total

def draw():
  x=random.choice(cards)
  return(x)

def total(hand):
  score = 0
  for card in hand:
    if card == 11 and score > 10:
      card = 1
      score += card
    else:
      score += card
  return score

def hit(hand):
  hit_internal = input("Would you like to Hit or Pass? Press 'h' for hit and 'p' for pass\n")
  clear()

  if hit_internal.lower() == 'h':
    player.append(draw())
  elif hit_internal.lower() =='p':
    return hand
  holder =total(player)
  if holder > 21:
    print(f'Players Hand {player}\n')
    print(f"You bust with {holder}, Dealer wins") 
    again =input("Would you like to play again, 'y' for yes or 'n' for no\n")
  elif holder <= 21 and len(hand)> 4:
    print("You win 5 cards under 21")
    again =input("Would you like to play again, 'y' for yes or 'n' for no\n")
    if again.lower() == 'n':
      run= False
    elif again.lower() == 'y':
      run= True  
  elif holder <= 21:
    print(f'Dealers Hand {dealer}\n')
    print(f'Players Hand {player}\n')
    hit(hand)
  

while run == True:
  again=""
  run_dealer =True
  dealer =[]
  player=[]
  
  print(logo)

  dealer.append(draw())
  player.append(draw())
  player.append(draw())

  print(f'Dealers Hand {dealer}\n')
  print(f'Players Hand {player}\n')
  
  player_hand = hit(player)
  clear()

  dealer.append(draw())
  
  while run_dealer == True:
    holder =total(dealer)
    if holder > 21:
      print(f'Players Hand {player}\n')
      print(f'Dealers Hand {dealer}\n')
      print(f"Dealer bust with {holder}, You Win") 
      run_dealer = False
    elif holder <= 21 and len(dealer)> 4:
      print("Dealer wins 5 cards under 21")
    elif holder <17:
      dealer.append(draw())
    else:
      player_total= calculate_total(player_hand)
      dealer_total= calculate_total(dealer)
      if player_total > dealer_total:
        print(f"You Win with a total of {player_total}")
      else:
        print(f"Dealer Wins with a total of {dealer_total}") 
        run_dealer= False

    print(f'Dealers Hand {dealer}\n')  

  again =input("Would you like to play again, 'y' for yes or 'n' for no\n")
  if again.lower() == 'n':
    run= False
  elif again.lower() == 'y':
    run= True
    clear()

  

again =input("Would you like to play again, 'y' for yes or 'n' for no\n")
if again.lower() == 'n':
  run= False
elif again.lower() == 'y':
  run= True
  clear()
