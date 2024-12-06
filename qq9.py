def add(a,b):
    sum=x+y
    return sum
def diff(a,b):
    difference=x-y
    return difference
def prod(a,b):
    product=x*y
    return product
def div(a,b):
    division=x/y
    return division
for i in range(5):
    x=float(input("Enter the first number: "))
    y=float(input("Enter the second number: "))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        a=add(x,y)
        print(a)
    elif choice==2:
        a=diff(x,y)
        print(a)
    elif choice==3:
        a=prod(x,y)
        print(a)
    elif choice==4:
        if y!=0:
            a=div(x,y)
            print(a)
        else:
            print("Division by zero is not possible")
    elif choice==5:
        print("Exit")
        break
    else:
        print("Invalid operation")    