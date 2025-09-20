#Code to check even or odd numbers
print("Welcome to the even or odd number checker")
no_to_check=int(input("Which number would you like to check today? "))
number = (no_to_check % 2)
if number ==0:
    print("Number is even")
else:
    print("Number is Odd")