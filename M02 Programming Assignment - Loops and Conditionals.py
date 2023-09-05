# Choose a secret number between 1 and 10
secret = int(input("Enter number between 1 to 10: "))
# Choose a guess number between 1 and 10
guess = int(input("Enter a number between 1 to 10: "))
# Check if the guess is too low, too high, or just right
if guess < secret:
    print("Too low")
elif guess > secret:
    print("Too high")
else:
    print("Just right")
