# Function for adding two numbers
def add(x, y):
    return x + y
# Function for subtracting two numbers
def subtract(x, y):
    return x - y
# Function for Multiplying two numbers
def multiply(x, y):
    return x * y
# Function for dividing two numbers
def division(x, y):
    if y == 0:
        return "Error:Division by zero"
    else:
        return x / y
# Function for taking modulus
def modulus(x,y):
    return x % y
# Function for taking exponent of number
def exponent(x, y):
    return x ** y

# Function to display Menu
def display_menu():
    print("\n*****Welcome to the Simple Calculator*****")
    print("1.Addition\t\t\t        2.Subtraction")
    print("3.Multiplication\t\t\t4.Division")
    print("5.Modulus\t\t\t        6.Exponent")

# Take input from user
    choice = input("Enter your choice:")
    return choice

def calculator():
    while True:
        choice = display_menu()
        # Checking if choice is valid then taking input from user
        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))

            if choice == '1':
               result = num1 + num2
               print("Result=", result)
            elif choice == '2':
               result = num1 - num2
               print("Result=", result)
            elif choice == '3':
               result = num1 * num2
               print("Result=", result)
            elif choice == '4':
               result = num1 / num2
               print("Result=", result)
            elif choice == '5':
               result = num1 % num2
               print("Result=", result)
            elif choice == '6':
               result = num1 ** num2
               print("Result=", result)

        # To perform further calculations
            next_calculation = input("Do you want to do another calculation?(yes/no):")
        # If calculation is 'no' the break loop
            if next_calculation == "no":
                print("Exiting Calculator....Have a good Day!")
                break
            else:
                print("Continuing with the next calculation. ")
        else:
            print("Invalid Input!Please enter valid choice")
# Run the Calculator
calculator()