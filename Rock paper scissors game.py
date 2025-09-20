import  random
p_choice= int(input("Welcome to the rock, paper and scissors game\nChoose one Type 0 for rock, 1 for paper and 2 for scissors\n"))
c_choice= random.randint(0,2)
print(f"Computer chose {c_choice}")
if p_choice == 0 and c_choice == 2:
    print("You win!!!")
elif p_choice == 0 and c_choice == 1:
    print("Awn, You lose")
elif p_choice == 0 and c_choice == 2:
    print("You win!!!")
elif p_choice == 1 and c_choice == 0:
    print("You win!!!")
elif p_choice == 1 and c_choice == 2:
    print("Awn, You lose")
elif p_choice == c_choice:
    print("Its a Tie!")

