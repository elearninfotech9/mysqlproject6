class abc:
    def m(self):
        print('parent1')

class qwe:
    def m3(self):
        print('parent2')

class xyz(abc,qwe):
    def m2(self):
        print('child')

obj=xyz()
obj.m2()

obj.m()
obj.m3()

