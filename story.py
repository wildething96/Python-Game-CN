# Imports

import sys, time, os
from useful_functions import typeWriter, isInt
from guests import guestMenu
from rooms import roomMenu
from guess import guessMenu

# Variables

count = 0

a, b, c = ("Detective", "Captin", "Police Officer")

storyDialog = (
    "\n\n" + "Loctation: Durham Police Station\n".center(160) ,
    "Time: 10:43pm\n\n",
    f"{b}: Hi {a}",
    f"{b}: We've just had reports of car going off the road and setting on fire near Manor House".center(160) + "\n\n\n",
    "\n\n\n" + f"{b}: Early reports suggest the estate owner Mr William Worth has been found deceased inside the vechile".center(160),
    f"{b}: Skid marks on the road suggest he was going too fast and lost control",
    f"{b}: Though there was no sign of breaking before he flew off the road",
    f"{b}: Either there was no attempt to break, or his breaks suddenly stopped working",
    f"{b}: I need you to go in and wrap things up detective, we don't want this to take all night\n\n",
    "\n\n" + "Loctation: Manor House".center(160 ) + "\n",
    "Time: 11:09pm\n",
    f"{c}: Hey {a}, from the looks of it, the driver was out of control",
    f"{c}: Seems like he was probably just driving too fast and guests said he'd had a few to drink.",
    f"{c}: Probably was a bit too gone and missed to break",
    f"{c}: Pretty cut and dry I'd say {a}.",
    f"{c}: Have a quick look if you can see anything worth noting and lets get home {a}\n",
    "\n\n\n" + f"*Your Phone rings*".center(160),
    f"{b}: Hi {a}, have you come to a conclusion over the crash?\n\n",
    f"1. Yes {b}, I have enough reason to open as a murder investigation!\n\n",
    f"2. Yes {b}, seems cut and dry, no foul play {b}\n\n")


tutorialClues = [
    "Investigate strong petrol smell coming from the area",
    "Investigate the surrounding area around the crash",
    "Investigate the burnt corpse inside the car"
]

tutorialAnswer = [
    "\n\n\n" + "You check around and notice some liquid on the grass, you smell it and sure enough its petrol seems a little odd".center(160) + "\n" +
    "it didn't burn up in the fire? On the back of mangled car you also just make out the word diesel... very odd".center(160) + "\n\n\n\n",
    "\n\n\n" + "You notice a smuged foostep coming from the direction of the Manor, though you check and it doesn't match any".center(160) + "\n" +
    "of the officers or guests foot prints".center(160) + "\n\n\n\n",
    "\n\n\n" + "After checking out the corpse you notice a thin but long puncture wound, seems unlikely anything in the car could".center(160) + "\n" +
    "of caused it. Seems more like a knife wound, is it possible he was dead before the crash?".center(160) + "\n\n\n\n"]

# Functions

def story(times=1):
    global count
    for i in range(times):
        for char in str(f"{returnStory(count).center(160)}" + "\n\n"):
            sys.stdout.write(char)
            sys.stdout.flush()
            if char == " ":
                time.sleep(0)
            elif char != "\n":
                time.sleep(0.01)
            else:
                time.sleep(0.2)
        count += 1


def returnStory(count):
    global storyDialog
    return(storyDialog[count])


def tutorialMenu():
    while len(tutorialClues) != 0: 
        typeWriter("\n\n" + f"Investigation Menu".center(160) + "\n\n\n")
        for num, clue in enumerate(tutorialClues, start=1):
            typeWriter((str(num) + ". " + clue).center(160) + "\n\n")

        num = isInt(len(tutorialClues) + 1) - 1 
        
        os.system("cls||clear")

        typeWriter(tutorialAnswer[num])
        tutorialClues.pop(num)
        tutorialAnswer.pop(num)

        input("Continue?".center(160) + "\n".center(160))
        os.system("cls||clear")


def startInvestigation():
    num = isInt(2) - 1 
    mainMenu() if num == 0 else endGame("lose badly")


def mainMenu():
    os.system("cls||clear")
    typeWriter("Main Menu".center(160) + "\n\n\n" + 
    "1. Talk to Guests".center(160) + "\n\n" +
    "2. Investigate a Room".center(160) + "\n\n" +
    "3. Take a guess at the Murder".center(160) + "\n\n\n")
    num = isInt(4) - 1 
    guestMenu(mainMenu) if num == 0 else roomMenu(mainMenu) if num == 1 else guessMenu(mainMenu)


def endGame(outcome):
    if outcome == "lose badly":
        os.system("cls||clear")
        typeWriter(
            "The murder overheard your stupidity and decide they should rid the world of such a lazy detective, they quickly cut the".center(160) + "\n" +
            "breaks of your car parked up by the Manor. Due to your poor detective skills you are of course none the wiser.".center(160) + "\n" +
            "On your way back you begin to realise your breaks don't work and deduce that your car probably neeeds ".center(160) + "\n" +
            "warming up. You speed right up to only realise that they of course still don't work. You crash".center(160) + "\n\n" +
            "GAME OVER".center(160) + "\n\n"
                    )
        input("Finish?".center(160) + "\n".center(160))
        sys.exit()
    elif outcome == "lose":
        typeWriter("GAME OVER".center(160) + "\n" + "Better luck next time!".center(160) + "\n\n")
        input("Finish?".center(160) + "\n".center(160))
        sys.exit()
    else:
        typeWriter("Congratulation, you solved the murder!!!".center(160) + "\n\n")
        input("Finish?".center(160) + "\n".center(160))
        sys.exit                
    


