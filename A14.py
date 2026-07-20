#Q1

from re import match
'''

n=int(input("Enter a number: "))
match n:
    case n if n>99 and n<1000:
        print("The number is a three-digit number.")
    case _:
        print("The number is not a three-digit number.")

#Q2
n =int(input("Enter a number: "))
match n:
    case n if n>0:
        print("The number is positive.")
    case n if n<0:
        print("The number is negative.")
    case _:
        print("The number is zero.")

#Q3
c =int(input("Enter the choice:"))
print("1. check odd or even")
print("2. check positive or negative")
print("3. calculate simple interest")
print("4. find quadratic equation roots")
match c:
    case 1:
        n=int(input("Enter a number: "))
        if n%2==0:
            print("The number is even.")
        else:
            print("The number is odd.")
    case 2:
        n=int(input("Enter a number:"))
        if n>0:
            print("The number is positive.")
        elif n<0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    case 3:
        p=int(input("Enter the principal amount:"))
        r=int(input("Enter the rate of interest:"))
        t=int(input("Enter the time:"))
        si=(p*r*t)/100
        print("The simple interest is:",si)
    case 4:
        a=int(input("Enter the coefficient of x^2:"))
        b=int(input("Enter the coefficient of x:"))
        c=int(input("Enter the constant term:"))
        d=b**2-4*a*c
        if d>0:
            root1=(-b+d**0.5)/(2*a)
            root2=(-b-d**0.5)/(2*a)
            print("The roots are real and distinct.")
            print("The roots are:",root1,"and",root2)
        elif d==0:
            root=-b/(2*a)
            print("The roots are real and equal.")
            print("The root is:",root)
        else:
            print("The roots are complex.")
#Q4
'''
x =eval(input("Enter some Data"))
match x:
    case  x if type(x) == int:
        print("Monday.")
    case x if type(x) == float:
        print("Tuesday.")
    case x if type(x) == complex:
        print("Wednesday")
    case x if type(x)== bool:
        print("Thursday")


#Q5
x = input("Entr some string:")
match x:
    case x if x in "mysirg":
        print("One")
    case x if x in "education":
        print("two")
    case x if x in "services":
        print("three")
    

        