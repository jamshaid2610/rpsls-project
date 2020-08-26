# rock-paper-scissor-project

import random

#Converting the name to number function



def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error: Wrong name entered"
        
#Function to convert number to name

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error: Number out of range"
        
        
def rpsls(player_choice):
    #Print a blank line
    print ("")
    #Print what player chose
    print ("The Player's choice is ", player_choice, ".")
    #convert player's choice to number
    player_number = name_to_number(player_choice)
    
    #Computer guess by taking in a random number
    comp_number = random.randrange(0,4)
    
    #Convert computer's number to name
    comp_choice = number_to_name(comp_number)
    
    #Print computer's choice
    print("The Computer's choice is ", comp_choice, ".")
    
    #difference between scores
    diff = (player_number - comp_number) % 5
    
    if diff == 0:
        print ("It is a tie!")
    elif diff <=2:
        print ("Computer wins!")
    elif diff >=3:
        print ("Player wins!")
    else:
        print ("There is an error!")
        
        
        
 #To run this put your option in rpsls()
