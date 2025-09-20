print("Welcome to the SkullReaper rollercoaster")
height = int(input("Whats your height in cm(s)? "))
bill =0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? ")) 
    if age <= 12:
        bill = 5
        print("Child tickets are 5$.")
    elif age<= 18:
        bill = 7
        print("Youth tickets are 7$.")
    else:
        bill = 12
        print("Adult tickets are 12$.")
    
    pic = input("Do you want to have your picture taken?Type Yes or No ")
    if pic == "Yes":
        bill += 3
        print(f"Your final bill is ${bill}")    
    else:
        print("Please Pay intial bill")
else:
    print("You cannot ride the rollercoaster")