class Dog():
  # Class object attribute
  # Same for any instance of a class
  species = 'mammal'

  def __init__(self, breed, name):
    self.breed = breed
    self.name = name


  def bark(self, number):
    print(f"Woof! My name is {self.name} my number is {number}")


my_dog = Dog('Lab','Sammy')
print (type(my_dog))

print(my_dog.breed) 
print(my_dog.name) 
print(my_dog.species)

my_dog.bark(10)

# self connects this method to the instance of the class
#

class Cat():
  def __init__(self, breed):
  # Attributes
  # We take in the argument
  # Assign it using self.attributename
    self.my_attribute = breed
  
my_cat = Cat(breed='Tiger')

print(my_cat.my_attribute)

class Circle():
  # Class object attribute
  pi = 3.14

  def __init__(self, radius=1):
    self.radius = radius
    self.area = radius*radius*self.pi
    # self.area = radius*radius*Circle.pi    Same as line above Circle

  # Method
  def get_circumference(self):
    return self.radius * self.pi * 2

my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)