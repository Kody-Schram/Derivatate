from deck import newTransformationCard, setupCards
from sympy import *

WINNING_SCORE = 50
STARTING_CARDS = 5

#active cards
activeFuntions, activeTransformations, playerCards, solveCards = setupCards()

def initCards():
  cards = []
  for i in range(STARTING_CARDS):
    cards.append(newTransformationCard())

  return cards


class Player:
  def __init__(self, cards):
    self.cards = initCards()
    self.score = 0

  def __repr__(self):
    str = ""
    for card in self.cards:
      str += f"{card}\n"
    
    return str


p1 = Player([])
p2 = Player([])
activePlayer = p1

while (p1.score < WINNING_SCORE) and (p2.score < WINNING_SCORE):
  print("Functions")

  
  if activePlayer == p1:
    activePlayer = p2
  else:
    ativePlayer = p1