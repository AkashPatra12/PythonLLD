"""
Python implementation of Immutable class
Asked in Microsoft HM interview
"""
class Immutable:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.frozen = True

    # @property
    # def name(self):
    #     print("executed")
    #     return self._name
    #
    # @property
    # def age(self):
    #     return self._age

    def __setattr__(self, key, value):
        print("executed")
        if getattr(self, "frozen", False):
            print("frozen")
            raise AttributeError("cant modify")
        super().__setattr__(key, value)

obj = Immutable("Akash", 30)
print(obj.name, obj.age)
try:
    obj._name = "ABC"
    print(obj.name, obj.age)
except Exception as e:
    print(e)
