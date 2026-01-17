slogan = "Just do it!"
sloga1 = "01234567890"
print(slogan[10]) # !
print(slogan[5:7]) # do
print(slogan[8:]) # it!
print(slogan[:4]) # Just
print("Don't" + " " + slogan[5:]) # Don't do it!

########
# type(), str(), and escape sequences

my_float = 1.234
print(type(my_float))

my_string = str(my_float) + " is a float."
print(my_string)

hello = "\"Hello, I'm Monica, it's nice to meet you!\""
print(hello)