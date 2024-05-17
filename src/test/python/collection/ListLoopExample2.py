class ListDemo2:
    def __init__(self, list_a):
        self.list_a = list_a

    def list_comparision_type1(self):
        list_b = []
        for i in range(len(self.list_a)):
            if "a" in self.list_a[i]:
                list_b.append(self.list_a[i])
        return list_b

    def list_comparision_type2(self):
        list_b = []
        for x in self.list_a:
            if "a" in x:
                list_b.append(x)
        return list_b

    def list_comparision_type3(self):
        list_b = [x for x in self.list_a if "a" in x]
        return list_b


l = ListDemo2(["apple", "banana", "mango"])
print(l.list_comparision_type1())
l.list_comparision_type2()
l.list_comparision_type2()
