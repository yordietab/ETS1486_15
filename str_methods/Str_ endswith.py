text = "Hello, world!"
print(text.endswith("world!"))  # Output: True
print(text.endswith("Hello"))   # Output: False


text = "Python is fun"
print(text.endswith("fun", 0, 13))  # Output: True
print(text.endswith("is", 0, 10))   # Output: False
#when we specify the start and end this code will check with the given route if we don't specify the start and end it will by default check from the start of the sentence to the end this also works for find(),index(), startswith()!!! 
