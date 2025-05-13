import random
from sympy import symbols, sympify
from transformationCard import newTransformationCard
from solveCard import newSolveCard

def newFunctionCard():
  functions = ["a*sin(b*x)", "a*cos(b*x)", "a*e^(b*x)", "a*log(b*x)", "a*log(x, b)", "a*x**2 + b*x + c", "b*a**(c*x)"]
  x, a, b, c, d = symbols('x a b c d')
  
  function = sympify(random.choice(functions))
  function = function.subs(a, random.randint(-10, 10))
  function = function.subs(b, random.randint(-10, 10))
  function = function.subs(c, random.randint(-10, 10))
  function = function.subs(d, random.randint(2, 10))
  return function

def newPlayerCard():
  card = random.randint(-10, 10)
  if (random.randint(0, 9) == 0):
    card = "wildcard"
  return card

def setupCards(MAX_FUNCTION_CARDS, MAX_TRANSFORMATION_CARDS, MAX_SOLVE_CARDS, MAX_PLAYER_CARDS, NUM_PLAYERS):
  functionCards = [newFunctionCard() for _ in range(MAX_FUNCTION_CARDS)]
  transformationCards = [newTransformationCard() for _ in range(MAX_TRANSFORMATION_CARDS)]
  solveCards = [newSolveCard() for _ in range(MAX_SOLVE_CARDS)]
  playerCards = [[newPlayerCard() for _ in range(MAX_PLAYER_CARDS)] for _ in range(NUM_PLAYERS)]
  
  return functionCards, transformationCards, solveCards, playerCards