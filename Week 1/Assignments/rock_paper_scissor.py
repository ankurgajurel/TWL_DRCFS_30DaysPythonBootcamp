import random

choices = ["rock", "paper", "scissor"]
khelne = True

bot_score = 0
user_score = 0

while khelne:

    bot_decision = random.choice(choices)

    user_choice = input("Enter either rock, paper or scissor: ").lower()
    
    print("bot chose: {}".format(bot_decision))
    print("user chose: {}".format(user_choice))

    if bot_decision == user_choice:
        print("tiee")
    elif bot_decision == "rock" and user_choice == "scissor":
        print("bot wins")
        bot_score += 1
    elif bot_decision == "rock" and user_choice == "paper":
        print("you win")
        user_score += 1
    elif bot_decision == "paper" and user_choice == "scissor":
        print("you win")
        user_score += 1
    else:
        print("you lose")
        bot_score += 1

    ch = input("ajhai khelne? Y/n: ")
    if ch.lower() == "y":
        khelne = True
    else:
        khelne = False

print("bot score {}".format(bot_score))
print("user score: {}".format(user_score))