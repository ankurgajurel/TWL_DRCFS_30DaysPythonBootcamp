import random

choices = ["rock", "paper", "scissor"]
khelne = True

while khelne:

    bot_decision = random.choice(choices)

    user_choice = input("Enter either rock, paper or scissor: ").lower()
    
    print("bot chose: {}".format(bot_decision))
    print("user chose: {}".format(user_choice))

    if bot_decision == user_choice:
        print("tiee")
    elif bot_decision == "rock" and user_choice == "scissor":
        print("bot wins")
    elif bot_decision == "rock" and user_choice == "paper":
        print("you win")
    elif bot_decision == "paper" and user_choice == "scissor":
        print("you win")
    else:
        print("you lose")

    ch = input("ajhai khelne? Y/n: ")
    if ch.lower() == "y":
        khelne = True
    else:
        khelne = False