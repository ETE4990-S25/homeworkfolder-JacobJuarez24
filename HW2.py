class Animal:
    def __init__(self, name, age):
        self.name =name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"
    
class Pet(Animal):
    def __init__(self, name, age, friendly=True):
        super().__init__(name, age)
        self.friendly = friendly
        self.eat = False

    def __str__(delf):
        return f"Pet - {self.name}, Age: {self.age}, Friendly: {self.friendly}"
        
class FarmAnimal(Animal):
    def __init__(self, name, age, eat=True, leather=True, helper=False):
        super().__init__(name, age)
        self.eat = eat 
        self.leather = leather
        self.helper = helper

    def __str__(self):
        return (f"Farm Animal - {self.name}, Age: {self.age}, Food: {self.eat}, Leather: {self.leather}, Helper: {self.helper}")

class Dog(Pet):
    def __init__(self, name, age, friendly=True, breed="Unknown"):
        super().__init__(name, age, friendly)
        self.breed = breed

    def __str__(self):
        return f"Dog - {self.name}, Age: {self.age}, Breed: {self.breed}, Friendly: {self.friendly}"
    

class