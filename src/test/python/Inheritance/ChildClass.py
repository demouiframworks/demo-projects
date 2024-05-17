from test.python.Inheritance.ParentClass import Person


# class Child(Person):
#     pass


class Child2(Person):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


if __name__ == "main":
    c2 = Child2("hi", "Chintu")
    c2.printname()
