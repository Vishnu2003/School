def add(a,b):
    s=a+b
    return s

def sub(a,b):
    s=a-b
    return s

def mul(a,b):
    s=a*b
    return s

def div(a,b):
    s=a/b
    return s

x=int(input('Enter the first number: '))
y=int(input('enter the second number: '))
z=input('select the operator(+,-,*,/): ')

if z == '+':
    print(add(x,y))
if z == '-':
    print(sub(x,y))
if z == '*':
    print(mul(x,y))
if z == '/':
    print(div(x,y))

