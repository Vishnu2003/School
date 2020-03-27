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
print('1.add \n2.subtract \n3.multiply \n4.divide')
z=int(input('select the operator: '))

if z == 1:
    print(add(x,y))
if z == 2:
    print(sub(x,y))
if z == 3:
    print(mul(x,y))
if z == 4:
    print(div(x,y))

