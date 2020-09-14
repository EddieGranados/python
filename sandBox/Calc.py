import sys



method = input("Pick a method, add, subtract, multiply, divide: " ).lower()



def Add():
    First = int(input("Enter the first number you want to add: "))

    Second = int(input("Enter second number: "))

    print("Your total is:", First + Second)

    Restart = input("Would you like something else? ").lower()
    
    if Restart == "yes":
        Restart()



def Subtract():
    First = int(input("Enter the first number you want to subtract: "))
    
    Second = int(input("Enter second number: "))
    
    print("Your total is:", First - Second)
    
    Restart = input("Would you like something else? ").lower()
    
    if Restart == "yes":
        Restart()  


def Multiply():
    First = int(input("Enter the first number you want to add: "))
    
    Second = int(input("Enter second number: "))
    
    print("Your total is:", First * Second)
    
    Restart = input("Would you like something else? ").lower()
    
    if Restart == "yes":
        Restart()


def Divide():
    First = int(input("Enter the first number you want to add: "))
    
    Second = int(input("Enter second number: "))
    
    print("Your total is:", First / Second)
    
    Restart = input("Would you like something else? ").lower()
    
    if Restart == "yes":
        Restart()


def Restart():  
    method = input("add, subtract, multiply, divide: ").lower()
    
    if method == "add":
	    Add()
    
    elif method == "subtract":
        Subtract()
	
    elif method == "multiply":
        Multiply()
	
    elif method == "divide":
        Divide()
    
    else:
        sys.exit()

if method == "add":
	Add()

elif method == "subtract":
	Subtract()

elif method == "multiply":
	Multiply()

elif method == "divide":
	Divide()