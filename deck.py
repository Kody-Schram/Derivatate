import random
from sympy import *

NUM_FUNCTION_CARDS = 5
NUM_PLAYER_CARDS = 5
NUM_TRANSFORMATION_CARDS = 5
NUM_SOLVE_CARDS = 5
NUM_PLAYERS = 2

def newFunctionCard():
  functions = ["a*sin(b*x)", "a*cos(b*x)", "a*e^(b*x)", "a*log(b*x)", "a*log(x, b)", "a*x**2 + b*x + c", "b*a**(c*x)"]
  x, a, b, c, d = symbols('x a b c d')
  
  function = sympify(random.choice(functions))
  function = function.subs(a, random.randint(-10, 10))
  function = function.subs(b, random.randint(-10, 10))
  function = function.subs(c, random.randint(-10, 10))
  function = function.subs(d, random.randint(2, 10))
  
  return function

def newTransformationCard():
  return TransformationCard.newTransformationCard()

def newSolveCard():
  return SolveCard.newSolveCard()

def newPlayerCard():
  card = random.randint(-10, 10)
  if (random.randint(0, 9) == 0):
    card = "wildcard"
  return card

def setupCards(): 
  activeFuntions = [newFunctionCard() for _ in range(NUM_FUNCTION_CARDS)]
  activeTransformations = [newTransformationCard() for _ in range(NUM_TRANSFORMATION_CARDS)]
  playerCards = [[newPlayerCard() for _ in range(NUM_PLAYER_CARDS)] for _ in range(NUM_PLAYERS)]
  solveCards = [newSolveCard() for _ in range(NUM_SOLVE_CARDS)]

  return activeFuntions, activeTransformations, playerCards, solveCards