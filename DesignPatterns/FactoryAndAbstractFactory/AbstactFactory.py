""" Factory of Factories"""

from abc import ABC, abstractmethod


# Step 1: Abstract Product Interfaces
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass


# Step 2: Concrete Products (Modern Style)
class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a modern chair."


class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a modern sofa."


# Step 3: Concrete Products (Victorian Style)
class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair."


class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a Victorian sofa."


# Step 4: Abstract Factory Interface
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


# Step 5: Concrete Factories
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


# Step 6: Client Code
class FurnitureStore:
    def __init__(self, factory: FurnitureFactory):
        self.factory = factory

    def order_furniture(self):
        chair = self.factory.create_chair()
        sofa = self.factory.create_sofa()

        print(chair.sit_on())
        print(sofa.lie_on())


# Step 7: Using the Abstract Factory Pattern
if __name__ == "__main__":
    # Client can decide which factory to use at runtime
    style = input("Choose furniture style (modern/victorian): ").lower()

    if style == "modern":
        factory = ModernFurnitureFactory()
    elif style == "victorian":
        factory = VictorianFurnitureFactory()
    else:
        raise ValueError("Unknown style.")

    store = FurnitureStore(factory)
    store.order_furniture()
