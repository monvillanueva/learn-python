positive_int = int(input("Enter a positive integer: "))
my_sum = 0

print("The user entered " + str(positive_int))
while positive_int > 0:
    print(positive_int)

    my_sum += positive_int
    if positive_int == 1:
        print("The sum is: " + str(my_sum))
    positive_int -= 1