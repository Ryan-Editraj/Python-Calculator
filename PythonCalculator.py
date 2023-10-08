import math

# Define the four basic arithmetic functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# Define additional mathematical functions
def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)


def log(x):
    return math.log(x)

def exp(x):
    return math.exp(x)

# Prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, sin, cos, tan, log, exp): ")

# Perform the calculation
if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":


elif operator == "/":
    result = divide(num1, num2)
elif operator == "sin":
    result = sin(num1)
elif operator == "cos":
    result = cos(num1)
elif operator == "tan":
    result = tan(num1)

elif operator == "log":
    result = log(num1)
elif operator == "exp":
    result = exp(num1)
else:
    print("Invalid operator.")
    exit()

# Display the result
print("The result is:", result)
