# Take input, evaluate against answer choices, evaluate input against computer selection

import random
import time

playerScore = 0
compScore = 0

while True:
    ansChoices = ["rock", "paper", "scissors"]
    playerChoice = input("\nType Rock, Paper, Scissors, or 'q' to quit: ").lower()

    if playerChoice == 'q':
        print("\nThanks for playing!")
        quit()
    
    if playerChoice not in ansChoices:
        print("Response invalid; try again")
        continue
    
    randomNum = random.randint(0,2)
    computerChoice = ansChoices[randomNum]

    print("\nComputer chose...\n")
    time.sleep(1)
    print(computerChoice, "...\n")

    if playerChoice == "rock" and computerChoice == "scissors":
        playerScore += 1
        print("You win!\n\nPlayer Score:",playerScore,"\nComputer Score:", compScore)
    elif playerChoice == "paper" and computerChoice == "rock":
        playerScore += 1
        print("You win!\n\nPlayer Score:",playerScore,"\nComputer Score:", compScore)
    elif playerChoice == "scissors" and computerChoice == "paper":
        playerScore += 1
        print("You win!\n\nPlayer Score:",playerScore,"\nComputer Score:", compScore)
    else:
        compScore += 1
        print("Better luck next time :(\n\nPlayer Score:",playerScore,"\nComputer Score:", compScore)    


