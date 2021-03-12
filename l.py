import abc
from abc import ABC, abstractmethod 
class Coche(ABC):
  @abc.abstractproperty 
  def numAsientos(self):
    pass

class Renault(Coche):
  @property
  def numAsientos(self):
    return 5

class Audi(Coche):
  @property
  def numAsientos(self):
    return 4

class Mercedes(Coche):
  @property
  def numAsientos(self):
    return 2

arrayCoches=[Renault(), Audi(), Mercedes()]

def imprimirNumAsientos (arrayCoches):
  for i in arrayCoches:
    print(i.numAsientos)

imprimirNumAsientos(arrayCoches)