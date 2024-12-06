def add(a,b):
    sum=x+y
    print("Sum=",sum)
def diff(a,b):
    difference=x-y
    print("Difference=",difference)
def prod(a,b):
    product=x*y
    print("Product=",product)
def div(a,b):
    division=x/y
    print("Division=",division)
for i in range(5):
    x=float(input("Enter the first number: "))
    y=float(input("Enter the second number: "))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        add(x,y)
    elif choice==2:
        diff(x,y)
    elif choice==3:
        prod(x,y)
    elif choice==4:
        if y!=0:
            div(x,y)
        else:
            print("Division by zero is not possible")
    elif choice==5:
        print("Exit")
        break
    else:
        print("Invalid operation")    