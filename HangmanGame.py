import random

with open('list.txt', 'r') as file:
    words = file.readlines()

word = random.choice(words)[-1] #the last character in text file is \n

amountofTries = 10
guesses = [] #all letters
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end= " ")
    print(" ")

    guess = input(f"Amount of tries left: {amountofTries}, Take your next guess ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        amountofTries = amountofTries - 1
        if amountofTries == 0:
            break
    
    done = True 
    for letter in word:
        if letter.lower() not in guesses:
            done = False



if done:
    print(f"You have found the word! It was {word}")
else:
    print(f"Sorry dude! You did not find the word! It was {word}")