# Question 1
fruits={"Apple","Pear","Banana","Mango"}

# for loop to print each fruit in the list
for fruit in fruits:
    print(fruit)

# Question 2 while loop creating creating a countdown from 10 to 1
countdown = 5
while countdown > 0:
     print(countdown)
     countdown += -1

# Question 3 using a for loop with range to first 10 square numbers
for i in range(1, 11):
    print(i**2)

# Question 4 using the random module
import random
from venv import create

colors = ["Red","Green","Blue","Yellow"]

for i in range(3):
    print(random.choice(colors))

# Question 5 creating and using a custom module
import math_operation 

#create a simple calculator using a while loop
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator.")
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {math_operation.add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {math_operation.subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {math_operation.multiply(num1, num2)}")
    elif choice == '4':
        result = math_operation.divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input")