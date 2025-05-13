from setup import setupCards, newPlayerCard, newFunctionCard
from sympy import *

WINNING_SCORE = 50
MAX_FUNCTION_CARDS = 5
MAX_PLAYER_CARDS = 5
MAX_TRANSFORMATION_CARDS = 5
MAX_SOLVE_CARDS = 5
NUM_PLAYERS = 2

#active cards
activeFuntions, activeTransformations, playerCards, solveCards = setupCards(MAX_FUNCTION_CARDS, MAX_TRANSFORMATION_CARDS, MAX_SOLVE_CARDS, MAX_PLAYER_CARDS, NUM_PLAYERS)

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