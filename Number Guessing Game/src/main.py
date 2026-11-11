import random

# secrte number
secret_number = random.randint(1, 100)

# total attempts
attempts = 0

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("ENTER GUESS NUMBER: "))
        print()
    except ValueError:
        print("Oops! It's invalid number. Try again...")
        continue


    if guess > 100 or guess < 1:
        print("Enter number between (1, 100)")
        continue

    attempts += 1
    if guess == secret_number:
        print(f"Congrats! You found the secret number in {attempts} attempts")
        anotherRound = input("Wanna another round? (y/n): ")

        if anotherRound == "y" or anotherRound == "Y":
            print("Starting a new round")
            attempts = 0
            continue
        elif anotherRound == "n" or anotherRound == "N":
            print("Ending the round...")
            break
        else:
            print("Type 'y' - to start new round\nor\n'n' - to end the round. ")
            break
            
    elif guess > secret_number:
        print("Too high. Try again.")
        
    elif guess < secret_number:
        print("Too low. Try again.")
    print()

    if attempts == 7:
        print("You've reached limit attempts!")
        break
    