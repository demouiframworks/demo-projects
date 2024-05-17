class ListDemo:
    def __init__(self, list_a):
        self.list_a = list_a

    def looplisttype1(self):
        for i in range(len(self.list_a)):
            print(self.list_a[i])

    def looplisttype2(self):
        for x in self.list_a:
            print(x)

    def list_sort(self):
        self.list_a.sort()
        print(self.list_a)


l = ListDemo(["apple", "banana", "mango"])
l.looplisttype1()
sorted_list = ListDemo([100, 1, 20, 9])
sorted_list.list_sort()
