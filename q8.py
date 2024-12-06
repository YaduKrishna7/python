def calculator():
    
    x=float(input("Enter the first number: "))
    y=float(input("Enter the second number: "))
    print("Select operators")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    operation=int(input("Enter the operation: "))
    if operation==1:
        return(f"{x+y}")
    elif operation==2:
        return(f"{x-y}")
    elif operation==3:
        return(f"{x*y}")
    elif operation==4:
        if y!=0:
            return(f"{x/y}")
        else:
            return("division by zero is not allowed")
    elif operation==5:
        exit()
    else:
        print("Invalid choice")
for i in range(6):            
    result=calculator()
    print(result)