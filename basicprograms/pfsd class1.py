#decision statement
#a=20
#b=20
a=int(input("enter the a value\n"))
b=int(input("enter the b value0\n"))
if(a>b):
    print("true")
else:
    print("false")

#elif statement
a=int(input("enter a value\n"))
b=int(input("enter b value\n"))
op=input("enter the operator(+,-,*,/,%,//,**)\n")
if(op=='+'):
    print("add=",a+b)
elif(op=='-'):
    print("sub=",a-b)
elif(op=='*'):
    print("Mul=",a*b)
elif(op=='/'):
    print("Div=",a/b)
elif(op=='%'):
    print("mod=",a%b)
elif(op=='//'):
    print("floor=",a//b)
elif(op=='**'):
    print("exponent=",a**b)
else:
    print("none")

