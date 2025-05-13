from enum import Enum
from sympy import symbols, integrate, diff, series

class TransformationTypes(Enum):
  INTEGRAL = 0 #takes 1 function as an argument
  DERIVATIVE = 1 #takes 1 function as an argument
  TAYLOR_SERIES = 2 #takes 1 function and 1 postive player card as an argument
  ADDITION = 3 #2 cards or functions
  SUBTRACTION = 4 #2 cards or functions
  MULTIPLICATION = 5 #2 cards or functions
  DIVISION = 6 #2 cards or functions (nonzero denominator)
  NATURAL_LOG = 7 #1 positive card or function
  EXPONENTIATION = 8 #2 cards or functions (nonzero base)

class argTypes(Enum):
  FUNCTION = 0
  PLAYER_CARD = 1
  NONZERO_PLAYER_CARD = 2
  POSITIVE_PLAYER_CARD = 3

class evalRetTypes(Enum):
  ERROR = 0
  FUNCTION = 1
  PLAYER_CARD = 2

class Card:
  def __init__(self, transformationType):
    self.transformationType = transformationType
    
    match transformationType: #establish possible arguments for each
      case TransformationTypes.INTEGRAL:
        self.arguments = [[argTypes.FUNCTION]]
      case TransformationTypes.DERIVATIVE:
        self.arguments = [[argTypes.FUNCTION]]
      case TransformationTypes.TAYLOR_SERIES:
        self.arguments = [[argTypes.FUNCTION, argTypes.POSITIVE_PLAYER_CARD]]
      case TransformationTypes.ADDITION | TransformationTypes.SUBTRACTION | TransformationTypes.MULTIPLICATION:
        self.arguments = [[argTypes.FUNCTION, argTypes.FUNCTION], [argTypes.FUNCTION, argTypes.PLAYER_CARD], [argTypes.PLAYER_CARD, argTypes.FUNCTION], [argTypes.PLAYER_CARD, argTypes.PLAYER_CARD]]
      case TransformationTypes.DIVISION:
        self.arguments = [[argTypes.FUNCTION, argTypes.FUNCTION], [argTypes.FUNCTION, argTypes.NONZERO_PLAYER_CARD], [argTypes.PLAYER_CARD, argTypes.FUNCTION], [argTypes.PLAYER_CARD, argTypes.NONZERO_PLAYER_CARD]]
      case TransformationTypes.NATURAL_LOG:
        self.arguments = [[argTypes.FUNCTION], [argTypes.POSITIVE_PLAYER_CARD]]
      case TransformationTypes.EXPONENTIATION:
        self.arguments = [[argTypes.FUNCTION, argTypes.PLAYER_CARD], [argTypes.NONZERO_PLAYER_CARD, argTypes.FUNCTION], [argTypes.NONZERO_PLAYER_CARD, argTypes.PLAYER_CARD]]

  def evaluate(self, args):
    if args not in self.arguments:
      print("Invalid arguments for transformation card. Consult rules for more information.")
      return evalRetTypes.ERROR, None
    match self.transformationType:
      case TransformationTypes.INTEGRAL:
        return evalRetTypes.FUNCTION, integrate(args[0], symbols('x'))
      case TransformationTypes.DERIVATIVE:
        return evalRetTypes.FUNCTION, diff(args[0], symbols('x'))
      case TransformationTypes.TAYLOR_SERIES:
        return evalRetTypes.FUNCTION, series(args[0], symbols('x'), 0, args[1])
      case TransformationTypes.ADDITION:
          if (args == [argTypes.PLAYER_CARD, argTypes.PLAYER_CARD])
        return args[0] + args[1]
      case TransformationTypes.SUBTRACTION:
        return args[0] - args[1]
      case TransformationTypes.MULTIPLICATION:
        return args[0] * args[1]
      case TransformationTypes.DIVISION:
        return args[0] / args[1]
      case TransformationTypes.NATURAL_LOG:
        return log(args[0])