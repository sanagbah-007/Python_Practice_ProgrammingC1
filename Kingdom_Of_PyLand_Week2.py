# This program's task;
# to become the Royal Python Wizard, must complete seven challenges. 
# Each challenge teaches an important Python concept: user input, if-else statements, and functions.

# Q1 the code is meant to welcome the user and ask them for 2 integers 
# and tell whether they are odd or even numbers.
from unicodedata import category


def introduction():
    print("\nWelcome to the Kingdom of PyLand!")
    print("To become the Royal Python Wizard, you must complete seven challenges.")
    
def check_odd_even(num1=None, num2=None):
    try:
        num1 = int(input("\nPlease enter the first integer: \n"))
    except ValueError:
        print("Please enter an integer in figures.")
        return check_odd_even()
    try:
        num2 = int(input("\nPlease enter the second integer: \n"))
    except ValueError:
        print("Please enter an integer in figures.")
        return check_odd_even()
    nums = [num1, num2]

    for num in nums:
        if num % 2 == 0:
            print(f"\n{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
    return num1, num2


# Q2 the code is meant to ask the user for their marks under 
# a 100 and tell them whether they have passed or failed.
def check_result(mark=None):
    try:
        mark = int(input("\nPlease enter your recent test score (1 to 100): \n"))
    except ValueError:
        print("Please enter a valid integer.")
        return check_result()
    if not 0 <= mark <= 100:
        print("Please enter a mark between 0 and 100.")
        return check_result()
    if mark >= 50:
        print("Congratulations! You have passed.")
    else:
        print("Sorry, you have failed.")

    return mark


# Q3 the code is meant to create calculate_grade(mark). Award A (80–100), B (70–79), C (60–69), D (50–59), F (<50).
def calculate_grade(mark):
    if 80 <= mark <= 100:
        return "A"
    elif 70 <= mark < 80:
        return "B"
    elif 60 <= mark < 70:
        return "C"
    elif 50 <= mark < 60:
        return "D"
    else:
        return "F"
    

# Q4 the code is meant to create age_category(age). 
# Display Child (0–12), Teenager (13–19), Adult (20–59), Senior (60+).
def age_category(age=None):
    try:
        age = int(input("\nPlease enter your age: \n"))
    except ValueError:
        print("Please enter a valid integer.")
        return age_category()
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age <= 59:
        return "Adult"
    elif age >= 60:
        return "Senior"
    else:
        return "Invalid age"


# Q5 the code is meant to create add(), subtract(), multiply(), divide(). 
# Ask for two numbers and an operator (+,-,*,/).Use if-elif-else to call the correct function.
def add(num3, num4):
    try:
        return num3 + num4
    except TypeError:
        return float(num3) + float(num4)


def subtract(num3, num4):
    try:
        return num3 - num4          
    except TypeError:
        return float(num3) - float(num4)


def multiply(num3, num4):
    try:
        return num3 * num4
    except TypeError:
        return float(num3) * float(num4)


def divide(num3, num4):
    try:
        if float(num4) == 0:
            print("Error: Division by zero.")
            return None
        return num3 / num4
    except TypeError:
        if float(num4) == 0:
            print("Error: Division by zero.")
            return None
        return float(num3) / float(num4)

def calculator():
    print("\nWelcome to the calculator!")
    print("Please enter two numbers and an operator (+, -, *, /) to perform a calculation.\n")
    try:
        num3 = float(input("\nEnter the first number: \n"))
    except ValueError:
        print("Please enter a valid number.")
        return calculator()
    try:
        num4 = float(input("\nEnter the second number: \n"))
    except ValueError:
        print("Please enter a valid number.")
        return calculator()
    
    operator = input("\nEnter an operator (+, -, *, /): \n")
    
    if operator == '+':
        result = add(num3, num4)
    elif operator == '-':
        result = subtract(num3, num4)
    elif operator == '*':
        result = multiply(num3, num4)
    elif operator == '/':
        result = divide(num3, num4)
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return calculator()
    
    if result is not None:
        print(f"\nThe result of {num3} {operator} {num4} is: {result}\n")


# Q6 the code is meant to to help the user to guess a secret number which is 
# 7 and give them hints if this high or low. 
# The user has 3 attempts to guess the number.
def guess_secret_number():
    secret_number = 7
    attempts = 3
    
    print("\nGuess the secret number (between 1 and 10). You have 3 attempts.")
    
    for attempt in range(attempts):
        try:
            guess = int(input(f"\nAttempt {attempt + 1}: Enter your guess: \n"))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        if guess < 1 or guess > 10:
            print("Please guess a number between 1 and 10.")
            continue
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the secret number!")
            return True
    
    print(f"Sorry, you've used all attempts. The secret number was {secret_number}.")
    return False


# Q7 the code is meant to Create deposit(), withdraw(), and check_balance(). Start with balance=1000. 
# Display a menu and use if-elif-else to choose the correct function. Prevent withdrawals larger than the balance.
def bank_homepage():
    print("\nWelcome to the Kingdom of PyLand Bank!")
    print("You can deposit, withdraw, and check your balance.")
    print("Your starting balance is 1000 coins.\n")
balance = 1000
def deposit(balance):
    try:
        amount = float(input("\nEnter the amount to deposit: \n"))
    except ValueError:
        print("Please enter a valid number.")
        return balance
    if amount <= 0:
        print("Deposit amount must be positive.")
        return balance
    balance += amount
    print(f"\nYou have deposited {amount}. Your new balance is: {balance}\n")
    return balance

def withdraw(balance):
    try:
        amount = float(input("\nEnter the amount to withdraw: \n"))
    except ValueError:
        print("Please enter a valid number.")
        return balance
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return balance
    if amount > balance:
        print("Insufficient funds.")
        return balance
    balance -= amount
    print(f"\nYou have withdrawn {amount}. Your new balance is: {balance}\n")
    return balance

def check_balance(balance):
    print(f"\nYour current balance is: {balance}\n")
    return balance

def bank_menu(balance):
    while True:
        print("\nBank Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("\nEnter option (1-4): \n")
        
        if choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            balance = withdraw(balance)
        elif choice == '3':
            check_balance(balance)
        elif choice == '4':
            print("Exiting the bank menu.")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")
    
    return balance

introduction()

check_odd_even()

mark = check_result()

grade = calculate_grade(mark)
print(f"\nYour grade is: {grade}")

age = age_category()
print(f"\nYour age category is: {age}")

calculator()

guess_secret_number()

bank_homepage()

bank_menu(balance)