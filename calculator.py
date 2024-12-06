x=int(input("Enter the number: "))
y=int(input("Enter the number: "))
def calculator():
    print("1.Aaddition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    choice=input("Enter the choice: ")
    if choice=='1':
        sum=x+y
        print("sum is",sum)
    elif choice=='2':
        difference=x-y
        print("difference is",difference)
    elif choice=='3':
        product=x*y
        print("product is",product)
    elif choice=='4':
        
        if y!=0:
            division=x/y
            print("division is",division)
        else:
            print("Cant do division")
    elif choice=='5':
        exit()
    else:
        print("invalid operation")
calculator()