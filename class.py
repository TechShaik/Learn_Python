class Shaik:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def home(self):
        return "Welcome " + self.name + " your age is " + str(self.age)

p1=Shaik()
print(p1.home())


class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

a = Animal()
d = Dog()
print(a.speak())       # Animal sound
print(d.speak())