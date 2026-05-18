num1 = float(input("10: "))
operator = input("Enter operator (+ /): ")
num2 = float(input("30: "))

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")
