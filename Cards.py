
"""
This method will shuffle all the 52 cards in a deck 
"""

from random import shuffle

def shuffle_cards():
  values = ['2','3','4','5','6','7','8','9','10', 'Jack', 'Queen', 'King', 'Ace']
  suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
  deck_of_cards = ["%s of %s" % (v, s) for v in values for s in suits]
  shuffle(deck_of_cards)
  return deck_of_cards


deck_of_cards = shuffle_cards()

#no_of_players = 5
#no_of_cards = 3
"""
This method will distribute the given number of cards to the given number of players 
"""
def deal(deck_of_cards, no_of_players, no_of_cards):
    hands = [[] for i in range(no_of_players)] #initialising empty lists for all players  
    i = 0
    for j in range(no_of_cards):                #Number of times each player is getting a card
        for h in hands:                         #distributing one card to every player at one time
            h.append(deck_of_cards[i])
            i+=1
    return hands

