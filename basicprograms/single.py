class Parent:
    def function1(self):
        print("this is function one")

class Child(Parent):
    def function2(self,a):
        print("this is function two")
        print(a)
    b=20

y=Child()
y.function1()
y.function2(10)
print(y.b)
