x=float(input("Enter the first number: "))
y=float(input("Enter the second number: "))
def add():
    sum=x+y
    print("Sum=",sum)
def diff():
    difference=x-y
    print("Difference=",difference)
def prod():
    product=x*y
    print("Product=",product)
def div():
    division=x/y
    print("Division=",division)
for i in range(5):
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        add()
    elif choice==2:
        diff()
    elif choice==3:
        prod()
    elif choice==4:
        if y!=0:
            div()
        else:
            print("Division by zero is not possible")
    elif choice==5:
        print("Exit")
        break
    else:
        print("Invalid operation")    