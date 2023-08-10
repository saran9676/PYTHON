class parent:
    def fun1(self):
        print("this is parent class")
class child1(parent):
    def fun2(self):
        print("this is child1 class")
class child2(parent):
    def fun3(self):
        print("this is child2 class")
obj=child1()
obj=child2()
obj.fun1()
obj.fun2()
obj.fun3()
