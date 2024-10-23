"""
Child classes at same level had code duplicates.

So created an interface with drive method
Inherited separate child strategy classes based on different strategies
In the main base Vehicle class added a has a relation for the interface
it will receive the required interface strategy object and call the method
"""

from abc import ABC, abstractmethod


class DriveStrategy(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def drive(self):
        pass


class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        print("Normal Drive")


class SpecialDriveStrategy(DriveStrategy):
    def drive(self):
        print("Special Drive")


class Vehicle:
    def __init__(self, name, drive_strategy):
        self.name = name
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()


class PassengerVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name, NormalDriveStrategy("Passenger"))


class SportyVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name, SpecialDriveStrategy("Sports"))


class OffRoadVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name, SpecialDriveStrategy("Off Road"))

passenger = PassengerVehicle("Passenger Vehicle")
passenger.drive()
sporty = SportyVehicle("Sports Vehicle")
sporty.drive()
OffRoad = OffRoadVehicle("OffRoad Vehicle")
OffRoad.drive()
