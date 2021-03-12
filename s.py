class Coche:
  def __init__(self,marca):
    self.marca=marca
  def getMarcaCoche(self):
    return self.marca

marca=input("Ingrese la marca: ")
x=Coche(marca)
print(x.getMarcaCoche())