""" Whenever we need create objects based on conditions we use Factory"""

from abc import ABC, abstractmethod

# Step 1: Define an abstract base class or interface
class Pet(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

# Step 2: Create concrete classes that implement the interface
class Dog(Pet):
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class Cat(Pet):
    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"

# Step 3: Create a factory class to generate the objects
class PetFactory:
    @staticmethod
    def get_pet(pet_type: str) -> Pet:
        if pet_type == "dog":
            return Dog()
        elif pet_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown pet type: {pet_type}")

# Step 4: Client code
def main():
    pet_type = input("Enter the type of pet (dog/cat): ").lower()
    pet = PetFactory.get_pet(pet_type)
    print(f"Created a {pet}")
    print(f"The {pet} says: {pet.speak()}")

if __name__ == "__main__":
    main()
