def addition(x,y):
    s=a+b
    return s

def subtraction(x,y):
    s=a-b
    return s

def multiplication(x,y):
    s=a*b
    return s

def division(x,y):
    s=a/b
    return s

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

