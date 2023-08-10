class parent1:
    def fun1(self):
        print("this is parent1 class")
class parent2:
    def fun2(self):
        print("this is parent2 class")
class child(parent1,parent2):
    def fun3(self):
        print("this is child class")
obj=child()

obj.fun1()
obj.fun2()
obj.fun3()
