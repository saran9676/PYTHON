class Parent:
    def fun1(self):
        print("this is parent class")
class child(Parent):
    def fun2(self):
        print("this is child class")
obj=child()
obj.fun1()
obj.fun2()