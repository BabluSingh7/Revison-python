#q1
n=int(input("Enter a number: "))
if n>99 and n<1000:
    print("The number is a three-digit number.")
else:
    print("The number is not a three-digit number.")

#Q2
n=int(input("Enter a number: "))
if n>0:
    print("The number is positive.")
elif n<0:
    print("The number is negative.")
else:  
    print("The number is zero.")

#Q3
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=b**2-4*a*c
if d>0:
    print("The roots are real and different.")
elif d==0:
    print("The roots are real and same.")
else:
    print("The roots are complex.")

#Q4
y=int(input("Enter the year: "))
if (y%4==0 and y%100!=0) or (y%400==0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

#Q5
a,b,c=int(input("Enter three numbers: ")),int(input()),int(input())
if a>b and a>c:
    print("The largest number is:",a)
elif b>a and b>c:
    print("The largest number is:",b)
else:
    print("The largest number is:",c)