def addition(x,y):
    ans=x+y
    return ans

def subtraction(x,y):
    ans=x-y
    return ans

def multiplication(x,y):
    ans=x*y
    return ans

def division(x,y):
    ans=x/y
    return ans

a=int(input('Enter the first number: '))
b=int(input('enter the second number: '))
op=input('select the operator(+,-,*,/): ')

if op == '+':
    print(addition(a,b))
if op == '-':
    print(subtraction(a,b))
if op == '*':
    print(multiplication(a,b))
if op == '/':
    print(division(a,b))

