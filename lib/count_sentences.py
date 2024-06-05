#!/usr/bin/env python3

class MyString:
  
  # initializing the attributes
  def __init__(self, value=''):
    self.value = value

  @property
  def value(self):
    """This is a value property"""
    return self._value

  @value.setter
  def value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  # methos to check if the value is a sentence or not
  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False

  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
    
  def count_sentences(self):
    import re
    sentences = re.split(r'[.!?]', self.value)
    sentence_count = len([s for s in sentences if s.strip()])
    return sentence_count
    
    