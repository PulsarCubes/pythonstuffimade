#everybody loves defining functions
def addition(x,y):
    print(x+y)
def subtraction(x,y):
    print(x-y)
def multiplication(x,y):
    print(x*y)
def division(x,y):
    print(x/y)

print('what operation do you want, a, s, m, or d')
choice = input()
if choice == 'a':
    print('what are the two numbers you want to add?')
    x = float(input())
    y = float(input())
    addition(x,y)
elif choice == 's':
    print('what are the two numbers you want to subtract?')
    x = float(input())
    y = float(input())
    subtraction(x,y)
elif choice == 'm':
    print('what are the two numbers you want to multiply?')
    x = float(input())
    y = float(input())
    multiplication(x,y)
elif choice == 'd':
    print('what are the two numbers you want to divide')
    x = float(input())
    y = float(input())
    division(x,y)
else:
    print('that wasn\'t an option')
    
    
    
