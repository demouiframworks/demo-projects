class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunction(self):
        print(f'{self.name}{self.age}')


p = Person("John", 24)
del p
