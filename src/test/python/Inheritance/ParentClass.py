from test.python.ExampleForMainFunction import x


class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(x)
        print(self.firstname, self.lastname)


p = Person("my", "name")
p.printname()
