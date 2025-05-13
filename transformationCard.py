from enum import Enum

#transformations
'''
- indefinate integral
- derivative
- convert to n term taylor series
- addition
- subtraction
- multiplication
- division
- log base n
- exponentiation
'''

class CardTypes(Enum):
  FUNCTION = 0
  TRANSFORMATION = 1
  EVALCARD = 2

class Card:
  def __init__(self, string, value, type=CardTypes.FUNCTION):
    self.string = string
    self.value = value
    self.type = type

  def __repr__(self):
    return f"{self.string}"

  def eval(self):
    ...