class Animal():
  def __init__(self):
    print("Anminal Created")
  
  def who_am_i(self):
    print("I am an animal")

  def eat(self):
    print("I am eating")

class Dog(Animal):

  def __init__(self):
    Animal.__init__(self)
    print("dog created")
mydog = Dog()


myanimal = Animal()

myanimal.eat()
myanimal.who_am_i()