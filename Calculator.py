import sys
import os

number1 = 0
operation = ""
number2 = 0
result = 0
user_choice = ""

def screenClean():
    input("\nPress Enter to continue...")
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def is_number(value):
    return value.replace('.', '', 1).replace('-', '', 1).isdigit()
    

while True:
    print("== Advanced Calculator ==\n\n1. Start calculation\n2. Show last result\n3. Exit")
    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        number1 = input("\nEnter the first number: ")
        operation = input("Enter a mathematical operation (+, -, *, /): ")
        number2 = input("Enter the second number: ")
        
        if is_number(number1) and is_number(number2):
            if operation == "+":
                result = float(number1) + float(number2)
                print("Your result is", result)
            if operation == "-":
                result = float(number1) - float(number2)
                print("Your result is", result)
            if operation == "*":
                result = float(number1) * float(number2)
                print("Your result is", result)
            if operation == "/":
                if number2 == "0":
                    print("Division by zero!")
                else:
                    result = float(number1) / float(number2)
                    print("Your result is", result)
        else:
            print("Error, incorrect number. Try again.")

    elif user_choice == "2":
        print("Your latest result is", result)
    elif user_choice == "3":
        sys.exit()
    else:
        print("Invalid choice, please try again.")
    screenClean()