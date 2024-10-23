"""
Child classes at same level has code duplicates
"""
class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print("Normal Drive")


class PassengerVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name)


class SportyVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
        print("special drive")


class OffRoadVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
        print("special drive")


passenger = PassengerVehicle("Passenger Vehicle")
passenger.drive()
sporty = SportyVehicle("Sports Vehicle")
sporty.drive()
OffRoad = OffRoadVehicle("OffRoad Vehicle")
OffRoad.drive()