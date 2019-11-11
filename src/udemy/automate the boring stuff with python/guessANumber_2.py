import random

name = input("Hello, What is your name?");

print("Well, "+name+" I'm thinking of a number between 1 to 20")
secretNumber = random.randint(1, 20)
print("DEBUG : Secret Number is: "+str(secretNumber))
for guessesTaken in range(1, 7):
    print("Take a guess...")
    guess = int(input())
    
    if guess < secretNumber:
        print(" Your guess is too low..")
    elif guess > secretNumber:
        print(" your guess is too high...")
    else:
        print("Good job, "+name+ " you guessed my number "+str(guess)+" = "+str(secretNumber))
        break

if secretNumber == guess:
    print(" you took "+str(guessesTaken)+" guesses and creaked it!!!!! ")
else:
    print("Nope, The number I was thinking of was "+str(secretNumber))