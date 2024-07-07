import converters
from converters import kg_to_lbs, lbs_to_kg
from utils import find_max
from ecommerce.shipping import shipping_cost
from pathlib import Path


#DEFINING A CLASS
class Person:
    def __init__ (self, name):
        self.name = name
    
    def talk(self):
        print("talked")

first_person = Person("Qiniso")
first_person.talk()

#INHERITANCE

class Mammal:
    def walk(self):
        print("walking")

class Dog(Mammal):
    def bark(self):
        print("barking")

class German_Sherpard(Dog):
    pass

class Favourate_Pet():
    def myPet(self):
        print("Pet")
class Cat(Mammal, Favourate_Pet):
    def mow(self):
        print("miyyaw")

sherpard = German_Sherpard()
sherpard.walk()
cat = Cat() 
cat.walk()
cat.mow()
cat.myPet()


#MODULES
#print(converters.lbs_to_kg(70))

print(kg_to_lbs(50))
print(lbs_to_kg(50))

numbers = [2, 3, "1"]

print(find_max(numbers))


print(shipping_cost())

path = Path('C:/Users/Qiniso Xulu')
print(path.exists())


for file in path.glob('*'):
    print(file)