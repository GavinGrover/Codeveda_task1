#Simple-Calculator Python

#Making functions of basic arithmetic functions Addition, subtraction, Multiplication, Division

def add(a,b):   #Addition function
    return a+b

def subtract(a,b):  #Subtraction function
    return a-b

def multiply(a,b):  #Multiplication Function
    return a*b

def divide(a,b):    #Division function
    if b == 0:
        print("Division with 0 is not allowed")
    else:
        return a/b 
    
def main(): #main function to take inputs and operations
    print("Welcome to the Calculator")
    
    try:    #taking inputs
        num1 = float(input("Enter Value of first number ="))
        num2 = float(input("Enter Value of second number ="))
        operation = input("Choose your operation (+,-,* and /) =").strip()
        
        #applying conditions
        if operation == "+":
            result = add(num1,num2)
        elif operation == "-":
            result = subtract(num1,num2)
        elif operation == "*":
            result = multiply(num1,num2)
        elif operation == "/":
            result = divide(num1,num2)
        else:
            print("Invalid Operation Choosen")
            return
        
        print(f"Result = {num1}{operation}{num2} = {result}")
    
    #Neglecting value input errors   
    except ValueError:
        print("Invalid. Please Enter numerals")
        
#executing main function        
if __name__ == "__main__":
    main()