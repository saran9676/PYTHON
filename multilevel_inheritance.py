class parent:
    def fun1(self):
        print("this is parent class")
class child(parent):
    def fun2(self):
        print("this is child class")
class grandchild(child):
    def fun3(self):
        print("this is grandchild class")
obj=grandchild()
obj.fun1()
obj.fun2()
obj.fun3()
