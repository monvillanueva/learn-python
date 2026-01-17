
def get_factorial(n):
    product = 1

    for number in range(1, n + 1):
        product *= number
    return product

print("Factorial of 3: " + str(get_factorial(3)))
print("Factorial of 4: " + str(get_factorial(4)))
print("Factorial of 5: " + str(get_factorial(5)))