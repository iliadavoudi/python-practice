import random

def main():
    random_number = random.randint(1,50)
    while True:
        guess = input("Enter your guess: ").strip().lower()
        if guess == "":
            print("you must enter number")
            continue
        if guess == "exit":
            print("you want to exit")
            break
        guess_number = int(guess)
        if guess_number > random_number:
            print("smaller")
        if guess_number < random_number:
            print("bigger")
        result = play(random_number,guess_number)
        print(result)
        if random_number == guess:
            break

def play(random_number,guess_number):
    if random_number == guess_number:
         return "correct"
    distance = abs(guess_number - random_number)
    if distance <= 2:
        return "very close"
    if distance <= 4:
        return "close"
    if distance <= 6:
        return "far"
    else:
        return "very far"
main()
