while True:
    print ("Options:")
    print ("Enter 'add' to add two numbers")
    print ("Enter 'subtract' to subtract two numbers")
    print ("Enter 'multiply' to multiply two numbers")
    print ("Enter 'divide' to divide two numbers")
    print ("Enter 'exponent' to raise a number to the power of another number")
    print ("Enter 'quotient' to determine the quotient of division")
    print ("Enter 'remainder' to determine the remainder of division")
    print ("Enter 'quit' to end the program")
    user_input=input(":")

    if user_input=="quit":
        break
    elif user_input=="add":
        num1=float(input("Enter a number:"))
        num2=float(input("\nEnter another number:"))
        result=str(num1+num2)
        print ("\nThe answer is " + result)
    elif user_input=="subtract":
        num1=float(input("Enter a number:"))
        num2=float(input("\nEnter another number:"))
        result=str(num1-num2)
        print ("\nThe answer is " + result)
    elif user_input=="multiply":
        num1=float(input("Enter a number:"))
        num2=float(input("\nEnter another number:"))
        result=str(num1*num2)
        print ("\nThe answer is " + result)
    elif user_input=="divide":
        num1=float(input("Enter a number:"))
        num2=float(input("\nEnter another number:"))
        result=str(num1/num2)
        print ("\nThe answer is " + result)
    elif user_input=="exponent":
        num1=float(input("Enter a number:"))
        num2=float(input("\nEnter another number:"))
        result=str(num1**num2)
        print ("\nThe answer is " + result)
    elif user_input=="quotient":
        num1=float(input("Enter a number:"))
        num2=float(input("\nEnter another number:"))
        result=str(num1//num2)
        print ("\nThe answer is " + result)
    elif user_input=="remainder":
        num1=float(input("Enter a number:"))
        num2=float(input("\nEnter another number:"))
        result=str(num1%num2)
        print ("\nThe answer is " + result)
        
    else:
        print ("Unknown input")
