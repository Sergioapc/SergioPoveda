import abc
from abc import ABC, abstractmethod 
class Coche(ABC):
  @abc.abstractproperty 
  def precioMedioCoche(self):
    pass

class Renault(Coche):
  @property
  def precioMedioCoche(self):
    return 18000

class Audi(Coche):
  @property
  def precioMedioCoche(self):
    return 25000

class Mercedes(Coche):
  @property
  def precioMedioCoche(self):
    return 27000

arrayCoches=[Renault(), Audi(), Mercedes()]

def imprimirPrecioMedioCoches (arrayCoches):
  for i in arrayCoches:
    print(i.precioMedioCoche)

imprimirPrecioMedioCoches(arrayCoches)