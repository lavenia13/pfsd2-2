#program1
#............
'''
n=int(input("enter a number:"))
if n==0:
    print("wrong input")
else:
    for i in range(n,n+1):
        val=n*(n*1)
        print(val)
'''

#--------------------
#example2
'''
x=0
str1="thisismycountryindia"
for i in str1:
    x=x+1
    print(str1[0:x])


x=0
str1="thisismycountryindia"
for i in str1:
    x=x-1
    print(str1[0:x])
    
'''
#example3
'''
rows=int(input("enter a row number"))
for i in range(rows):
    for j in range(i+1):
        print("* ",end=" ")
    print("\n")
'''
#example4
'''
a1=1045
a3="10100"
a2=int(format(int(a3,2),'d'))
print(a2)

a4=1045
a5=format(a4,'x')
print(a5)

a1=1045
a2=format(a1,'b')
print(a2)

a1=234
a2=format(a1,'o')
print(a2)
'''
#1st sum
num = [1, 2, 5, 6, 7]
avg = sum(num)/len(num)
print(avg)

#2nd sum
a=input("enter a string")
print(type(a))
a1=int(a)
print(type(a))

#3rd sum
print("Format for writing complex number: a+bj.\n")
c1 = complex(input("Enter First Complex Number: "))
c2 = complex(input("Enter second Complex Number: "))
print("Sum of both the Complex number is", c1 + c2)



f1 = float(input("Enter First float Number: "))
f2 = float(input("Enter second float Number: "))
print("Sum of both the float number is", f1 + f2)

d1 = int(input("Enter First integer Number: "))
d2 = int(input("Enter second integer Number: "))
print("Sum of both the integer number is", d1 + d2)

#4th sum
a=int(input("Enter the number:"))
b=float(a)
print(type(a))
print(type(b))

#5th sum
a=input("Enter a string")
b=int(input("Enter the integer:"))
result=int(a)+b
print(result)
