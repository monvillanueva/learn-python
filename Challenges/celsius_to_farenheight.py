
user_celsius = int(input("Enter the temperature in Celsius: "))

def fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 1)


print("The Fahrenheit equivalent of " + str(user_celsius) + " degrees Celsius is " + str(fahrenheit(user_celsius)))