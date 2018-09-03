from random import randint
from time import sleep

choices = ["ROCK", "PAPER", "SCISSORS"]

outcome = {
  "winner": "You Won! Hip Hip Hooray!!! ^_^",
  "loser": "You Lost! Humanity is Doomed!!! -_-",
  "tie": "It's A Tie! Meh, humans and machines will continue to coexist ¯\_(ツ)_/¯"
}

def winner(user, computer):
  print("Your choice: %s" % user)
  print("Skynet chooses: %s" % computer)
  if user == computer:
    print(outcome["tie"])
  elif user == choices[0] and computer == choices[2]:
    print(outcome["winner"])
  elif user == choices[1] and computer == choices[0]:
    print(outcome["winner"])
  elif user == choices[2] and computer == choices[1]:
    print(outcome["winner"])
  else:
    print(outcome["loser"])

def start_game():
  print("Your goal is to defeat Skynet in a game of Rock, Paper, or Scissors...")
  sleep(3)
  print("Choose wisely, the fate of humanity depends on your decision!")
  sleep(1)
  user = input("Choose between Rock, Paper, or Scissors: ")
  user = user.upper()
  print("Skynet is choosing...")
  sleep(2)
  computer = choices[randint(0, 2)]
  winner(user, computer)

start_game()