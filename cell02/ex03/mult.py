n1 = float(input("Please enter the first number: "))
n2 = float(input("Please enter the second number: "))

result = n1 * n2

print(f"The result of multiplying {n1} and {n2} is {result}.")

if result > 0:
    print("The result of the multiplication is positive.")
elif result < 0:
    print("The result of the multiplication is negative.")
else:
    print("The result of the multiplication is zero.")