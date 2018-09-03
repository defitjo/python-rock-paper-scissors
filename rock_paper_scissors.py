from random import randint

choices = ["ROCK", "PAPER", "SCISSORS"]

outcome = {
  "winner": "You Won! ^_^",
  "loser": "You Lost! -_-",
  "tie": "It's A Tie! ¯\_(ツ)_/¯"
}

def winner(user, computer):
  print("Your choice: %s" % user)
  print("Computer chooses: %s" % computer)
  if user == computer:
    print(outcome["tie"])
  elif user == choices[0] and computer == choices[2]:
    print(outcome["winner"])
  elif user == choices[1] and computer == choices[0]:
    print(outcome["winner"])
  elif user == choices[2] and computer == choices[1]:
    print(outcome["winner"])

