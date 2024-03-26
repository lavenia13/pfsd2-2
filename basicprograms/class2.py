#Nested  if statement
a=40
b=60
c=10
if(a>b):
    if(a>c):
        print("a is greater")
    else:
        print("c is big")
elif(b>c):
    print("b is big")
else:
    print("c is big")

#biggest three numbers
a=10
b=2
c=3
if(a>b and a>c):
    print("A is big")
elif(b>c):
    print("b is big")
else:
    print("c is big")

#looping statement
i=1
n=10
sum1=0
while(i<=10):
    print(i)
    sum1=sum1+i
    i+=1
    print(sum1)