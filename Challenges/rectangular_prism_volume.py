length = int(input("Please enter a length: "))
width = int(input("Please enter a width: "))
height = int(input("Please enter a height: "))

def calculate_volume(l, w, h):
    return l * w * h


print("The volume of the rectangular prism is " + str(calculate_volume(length, width, height)) + " cubic feet.")