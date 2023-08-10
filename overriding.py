class a:
    def display(self):
        print("this is class A")
class b(a):
    def display(self):
        print("this is class B")
        super().display()
obj=b()
obj.display()