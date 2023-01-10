# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 13:55:03 2023

@author: ayush
"""

# Rock, Paper, and Scissors Game 

from random import randint

# Function of the game

def rockPaperScissors(play):
    
    choice = ["rock", "paper", "scissors"]

    computer = choice[randint(0,2)]   
    
    while play == "Y" or play == "y":
        user = input("Enter Choice: Rock, Paper, or Scissors -:  ")
        print("Computer's choice is: ", computer)
        if user == computer:
            print("..Tie!..")
        elif user == "rock" or user == "Rock":
            if computer == "paper":
                print("Sorry! You lose.." , computer, "covers", user)
            else:
                print("Hurrah! You Win..", user, "crushes", computer)
        elif user == "paper" or user == "Paper":
            if computer == "scissors":
                print("Sorry! You lose.." , computer, "cuts", user)
            else:
                print("Hurrah! You Win..", user, "covers", computer)
        elif user == "scissors" or user == "Scissors":
            if computer == "rock":
                print("Sorry! You lose.." , computer, "crushes", user)
            else:
                print("Hurrah! You Win..", user, "cuts", computer)
        else:
            print("You entered an invalid choice.")
        play = input("Would you like to play again? [Y/N]: ")
        print("\n")
        if play == "Y" or play == "y":
            computer = choice[randint(0,2)]
        else:
            print("Thank you for playing!")
            print("Have A Nice Day dear!")

if __name__=="__main__": 
    
    print("....Welcome To Rock Paper Scissors Game....")
    play=input("Are you Ready? [Y/N]: ")
    if play=="Y" or play=="y":
        rockPaperScissors(play)
    else:
        print("Have A Nice Day dear!")

