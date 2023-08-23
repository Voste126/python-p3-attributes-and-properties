#!/usr/bin/env python3

APPROVED_BREEDS = [
  "Mastiff", 
  "Chihuahua",
  "Corgi",
  "Shar Pei",
  "Beagle",
  "French Bulldog",
  "Pug",
  "Pointer"
]

class Dog:

  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    if not isinstance(value, str):
      raise TypeError("Name must be a string")
    elif len(value) < 1 or len(value) > 25:  
      print("Name must be string between 1 and 25 characters.")
    else:
      self._name = value
  
  @property
  def breed(self):
    return self._breed

  @breed.setter
  def breed(self, value):
    if value not in APPROVED_BREEDS:  
      print("Breed must be in list of approved breeds.")
    else:
      self._breed = value