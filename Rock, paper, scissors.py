import random
while True:
    choices = ["rock", "paper", "scissors"]
    def play(computer_choice, user_choice):
        if computer_choice == user_choice:
            return "equal!!"
        if (user_choice == "rock" and computer_choice == "scissors"
                or user_choice == "paper" and computer_choice == "rock"
                or user_choice == "scissors" and computer_choice == "paper"):
            return "you are the winner!!"
        else:
            return "computer is the winner"

    def main():
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock, paper, scissors): ")
        print(f"user: {user_choice} computer: {computer_choice}")
        if user_choice not in choices:
            print("wrong choice!!")
            return
        print(play(computer_choice, user_choice))
    main()
