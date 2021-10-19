import os, sys
from useful_functions import typeWriter


guests = [
    "Host - Mr William Worth",
    "Host's Wife - Mrs Bella Worth",
    "Gardener - Mr Garcon Bouchet",
    "Best Friend - Mr Jeffrey Miller",
    "Best Friend's Wife - Mrs Claudia Miller",
    "Work Colleague - Mr Ricardo simpson",
    "Work Colleague's Wife - Mrs Jane simpson",
    "Neighbour - Mrs Gwendal daryl"
]

def guessMenu(mainMenu):
    os.system("cls||clear")
    typeWriter(
        "Ready to make a guess? you only get one chance...".center(160) + "\n\n\n" +
        "List of Guests:".center(160) + "\n\n\n")
    
    for guest in (guests):
        typeWriter(guest.center(160) + "\n\n")

    typeWriter("Are you ready to make your guess 'y' for yes anything else to exit back to saftey".center(160) + "\n\n".center(160))
    choice1 = input()
    os.system("cls||clear")

    if choice1 == "y":
        typeWriter("Are you sure? there's no going back!!! 'y' ".center(160) + "\n\n".center(160))
        choice2 = input()
        os.system("cls||clear")

        if choice2 == "y":
            typeWriter("I hope you know what you're doing...".center(160) + "\n")
            input()
            input("Continue?".center(160) + "\n".center(160))
            os.system("cls||clear")

            for guest in (guests):
                typeWriter("\n" + guest.center(160) + "\n")

            final_choice  = input(typeWriter("\n\n" + "Please select your Murderer: ".center(160) + "\n"))
            if final_choice == "Mr William Worth":
                typeWriter("Congratulations, I guess you were paying attention after all.".center(160) + "\n")
                input()
                typeWriter("\n\n" + "Go forth as the incredible winner, detective and just generally amazing person you are".center(160) +  "\n".center(160))
                input()
                typeWriter("\n\n" + "Goodbye Champ!".center(160) + "\n")
                input()
                sys.exit()
            else:
                os.system("cls||clear")
                typeWriter("Owphhh, so wrong. How did you even get this far?".center(160) + "\n")
                input()
                typeWriter("\n\n\n" + "End the game as the amazing loser you are?".center(160) + "\n".center(160))
                input()
                sys.exit()
            
        else:
            typeWriter("Nawwww, you were almost brave enough... almost".center(160) + "\n\n")
            input("Continue?".center(160) + "\n".center(160))
            mainMenu()
    else:
        typeWriter("It's ok, maybe you'll be brave enough next time...".center(160) + "\n\n")
        input("Continue?".center(160) + "\n".center(160))
        mainMenu()
