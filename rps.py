import random

print('Welcome to Rock Paper Scissors!')
user = input('Enter "Rock", "Paper", or "Scissors": ').lower()

options = ['rock', 'paper', 'scissors']

if user not in options:
    print('Please type either "Rock", "Paper", or "Scissors".')

computer = random.choice(options)

print(f"You chose {user}, and the computer chose {computer}.")

if user == computer:
    print('You tie!')
elif user == 'rock' and computer == 'scissors':
    print('You win!')
elif user == 'rock' and computer == 'paper':
    print('You lose!')
elif user == 'scissors' and computer == 'rock':
    print('You Lose')
elif user == 'scissors' and computer == 'paper':
    print('You win!')
elif user == 'paper' and computer == 'rock':
    print('You win!')
elif user == 'paper' and computer == 'scissors':
    print('You lose!')