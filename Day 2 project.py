print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15%?"))
no_of_splits = int(input("How many people to split the bill?"))
percentage_tip=tip/100
solution = str(round(((percentage_tip*total_bill)+total_bill)/no_of_splits, 2))
print("Each person should pay: $"+solution)