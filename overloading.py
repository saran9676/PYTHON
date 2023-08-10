# overloading(compile time)
# same class,same method,different parameters
# it can be overcome by default parameter
class a:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=1):
        return a+b+c 
obj=a()
print(obj.sum(1,2,3))
print(obj.sum(1,2))