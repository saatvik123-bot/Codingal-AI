
import random

choices =  ["Rock", "Paper", "Scissor"]

def play():
    user_choice = input("Choose any choice ('Rock', 'Paper', 'Scissor'): ") .capitalize()
    computer_choice = random.choice(choices)

    print(f"Computer chose {computer_choice}")

       
    if user_choice == computer_choice:
        print("It a tie")
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper") :
          print("You Win !!🎉")
    elif user_choice not in choices:
         print("Invalied input!!")
         return
    else:
         print("Computer Wins!! 🎉💻")

play()