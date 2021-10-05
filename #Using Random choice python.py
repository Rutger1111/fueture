#Using Random choice python
#Running Race game
import time
import random

lives = 3

thislist = ['will', 'shoe', 'kick', 'poop']
gamelist = ['You lose the race', 'You win the race']

print (lives)

Player = input('Rutger')
print(' Hello ' + Player + ' , welcome to the game of hanging around')
time.sleep(2)
word = (random.choice(thislist))
guess = input("enter letter----:")

while True:

if word == "will":
    guess = input("enter letter----:")
    if guess == "l":
        print ("--ll")
    elif guess =="w":
        print ("w---")
    elif guess == "i":
        print("-i--")
        
    else:
        lives -= 1
if word == "shoe":
    print (you won)
    break

if word == "kick":
    print (you won)
    break

if word == "poop":
    print (you won)
    break

if word == "will":
    print (you won)
    break



