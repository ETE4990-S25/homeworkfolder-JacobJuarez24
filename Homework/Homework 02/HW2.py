#Define animal class
class Animal:
    def __init__(self, name, age):
        self.name =name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"

#Define animal class subcategories    
class Pet(Animal):
    def __init__(self, name, age, friendly=True):
        super().__init__(name, age)
        self.friendly = friendly
        self.eat = False

    def __str__(self):
        return f"Pet - {self.name}, Age: {self.age}, Friendly: {self.friendly}"
        
class FarmAnimal(Animal):
    def __init__(self, name, age, eat=True, leather=True, helper=False):
        super().__init__(name, age)
        self.eat = eat 
        self.leather = leather
        self.helper = helper

    def __str__(self):
        return (f"Farm Animal - {self.name}, Age: {self.age}, Food: {self.eat}, Leather: {self.leather}, Helper: {self.helper}")

#Define types of pets
class Dog(Pet):
    def __init__(self, name, age, friendly=True, breed="Unknown"):
        super().__init__(name, age, friendly)
        self.breed = breed

    def __str__(self):
        return f"Dog - {self.name}, Age: {self.age}, Breed: {self.breed}, Friendly: {self.friendly}"
    
class Cat(Pet):
    def __init__(self, name, age, friendly=True, breed="Unknown"):
        super().__init__(name, age, friendly)
        self.breed = breed

    def __str__(self):
        return f"Cat - {self.name}, Age: {self.age}, Breed: {self.breed}, Friendly: {self.friendly}"

class Bird(Pet):
    def __init__(self, name, age, friendly=False, breed="Unknown"):
        super().__init__(name, age, friendly)
        self.breed = breed

    def __str__(self):
        return f"Bird - {self.name}, Age: {self.age}, Breed: {self.breed}, Friendly: {self.friendly}"

#Define types of farm animals
class Horse(FarmAnimal):
    def __init__(self, name, age, eat=False, leather=True, helper=True):
        super().__init__(name, age, eat, leather, helper)

    def __str__(self):
        return f"Horse - {self.name}, Age: {self.age}, Helper: {self.helper}, Food: {self.eat}"
    
class Sheep(FarmAnimal):
    def __init__(self, name, age, eat=True, leather=True, helper=False):
        super().__init__(name, age, eat, leather, helper)

    def __str__(self):
        return f"Horse - {self.name}, Age: {self.age}, Helper: {self.helper}, Food: {self.eat}"

class Pig(FarmAnimal):
    def __init__(self, name, age, eat=True, leather=True, helper=False):
        super().__init__(name, age, eat, leather, helper)

    def __str__(self):
        return f"Horse - {self.name}, Age: {self.age}, Helper: {self.helper}, Food: {self.eat}"
    
#Class for managing farm animals
class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to farm")
    
    def remove_animal(self, name):
        animal_to_remove = None
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                animal_to_remove = animal
                break
        if animal_to_remove:
            self.animal.remove(animal_to_remove)
            print(f"{name} has been removed from farm")
        else:
            print(f"Animal {name} not found on the farm")
        
        def show_animals(self):
            if not self.animals:
                print("No animals on the farm")
            else:
                print(f"Animals on the farm:")
                for animal in self.animals:
                    print(animal)
            
#Main Program loop
def main():
    farm = Farm()

    while True:
        print("\n1. Add Animal")
        print("2. Remove Animal")
        print("3. Show Animals")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4):").strip()

        #Choice 1
        if choice == "1":
            animal_type = input("Enter animal type (Dog, Cat, Bird, Horse, Sheep, Pig):").strip().lower()
            name = input("Enter the animals name: ").strip()
            age = int(input("Enter the animals age:").strip())

            if animal_type == "dog":
                breed = input("Enter the breed of the dog:").strip()
                dog = Dog(name, age, breed=breed)
                farm.add_animal(dog)
            elif animal_type == "cat":
                breed = input("Enter the breed of the cat:").strip()
                cat = Cat(name, age, breed=breed)
                farm.add_animal(cat)
            elif animal_type == "bird":
                breed = input("Enter the breed of the bird:").strip()
                bird = Bird(name, age, breed=breed)
                farm.add_animal(bird)
            elif animal_type == "horse":
                horse = Horse(name, age)
                farm.add_animal(horse)
            elif animal_type == "sheep":
                sheep = Sheep(name, age)
                farm.add_animal(sheep)
            elif animal_type == "pig":
                pig = Pig(name, age)
                farm.add_animal(pig)

            else:
                print("That animal is not an option")
        #Choice 2
        elif choice == "2":
            name = input("Enter the name of the animal you'd like to remove:").strip()
            farm.remove_animal(name)
        
        #Choice 3
        elif choice == "3":
            farm.show_animals()

        #Choice 4
        elif choice =="4":
            print("Ending Program")
            break

        else:
            print("Not an option, try again")
                
#Run program
if __name__ == "__main__":
    main()