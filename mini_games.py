import os, random, operator
from useful_functions import typeWriter, typeWriter2

kitchen_message = (
    "You are in the kitchen. As you switch on the extractor fan,".center(160) + "\n" +
    "you realise that it’s not working. You check and find that it’s loose.".center(160) + "\n" +
    "Then you remove it and you find a piece of paper with some questions:".center(160) + "\n\n")

bathroom_message = (
    "In the bathroom, you find dirty marks left uncleaned in the sink which is very unusual.".center(160) + "\n" +
    "There might an item hiding around which could be of use to the investigation.".center(160) + "\n\n" +
    "Find the item by playing a HANGMAN game to reveal the name of the clue hiding in the bathroom.".center(160) + "\n\n")

bathroom_message2 = (
    "In your search for the code you must first complete some common phrases to help lead you".center(160) + "\n\n" +
    "to part of a code which might be helpful in continuing your investigation".center(160) + "\n\n")

bedroom_message = (
        "You are in the bedroom, and everything seems to be in order".center(160) + "\n" +
        "but a safe locked wardrobe draws your attention.".center(160) + "\n" +
        "You believe there may be an important clue in it. But you need a code!".center(160) + "\n\n" +
        "Answer the following 5 maths questions correctly to unlock the code to the wardrobe.".center(160) + "\n\n\n")

garage_message = (
    "After getting closer to it you realise that its actually a small droplet of blood".center(160) + "\n" +
    "It must be from the victim, you realise you should probably run it to check it was from Mr Worth".center(160) + "\n" +
    "The body was so burnt it was hard to get a proper ID from the victim, so we should run it just to double check".center(160) + "\n\n" +
    "Crack the code to show the full genetic sequence of the blood and find who it belonged to".center(160) + "\n"
)

# Kitchen Game

questions = [
    "If I am 20 years older than my nephew, and he is 10 years older than my niece, how old I would be if my niece is 17 years old?:".center(160) + "\n".center(160),
    "If I have 3 friends: one has 20K in savings; another has 5 times that amount, but he has a debt of 40K that ".center(160) + "\n" +
    "must be paid today to my third friend, who actually owes me 10K and had nothing in savings.".center(160) +
    "\n" + "How much do my friends have as a sum after paying their debts? (in K)".center(160) + "\n".center(160),
    "You take the queue and you are number 26, the last number that was called was number 5,".center(160) +
    "\n" + "and you know that every person takes about 3 minutes to be served until they shout the next number.".center(160) + "\n" +
    "How long will you have to wait until your turn? (in minutes)".center(160) + "\n".center(160),
]

answers =[
    "47",
    "110",
    "7"
]

def kitchenGame(roomMenu, mainMenu, remove):
    os.system("cls||clear")
    typeWriter(kitchen_message)
    
    input("Continue?".center(160) + "\n".center(160))
    iteration = 0

    for i in range(len(questions)):
        while True:
            try:
                answer = answers[iteration]
                os.system("cls||clear")

                saying = (input(questions[iteration]))
                if saying == answer:
                    input("Yes! Next question.".center(160) + "\n".center(160))
                    break
                elif saying == "exit":
                     roomMenu(mainMenu)
                else:
                    input("No, try again or Type 'exit' to leave".center(160) + "\n".center(160))
            except ValueError:
                    print("Provide an answer without full stop".center(160) + "\n")
                    input("Continue.".center(160) + "\n".center(160))
        iteration = iteration + 1
    typeWriter(
        "You have figured out the code 471107, it must be for something but what?".center(160) + "\n" +
        "I guess I'll just try to remember it for now".center(160) + "\n\n")
    remove()
    input("Continue?".center(160) + "\n".center(160))
    roomMenu(mainMenu)


# Bathroom Game

def bathroomGame(roomMenu, mainMenu, remove):
    os.system("cls||clear")
    typeWriter(bathroom_message)

    word = "muddyshoes"
    allowed_errors = 7
    guesses = []
    done = False

    input("Ready to play?".center(160) + "\n".center(160))
    os.system("cls||clear")
   
    while not done:
        for num, letter in enumerate(word):
            if letter.lower() in guesses:  
                if num == 0:
                    print("".center(70) + letter, end=" ")
                else:
                    print(letter, end=" ")
            else:
                if num == 0:
                    print("".center(70)  + "_", end=" ")
                else:
                    print("_", end=" ")

        guess = input("\n\n\n".center(126) + f"Allowed Errors Left {allowed_errors}, Next Guess: ")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            allowed_errors -= 1
            if allowed_errors == 0:
                break

        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False

    if done:
        os.system("cls||clear")
        typeWriter("\n\n" + f"You found the word! It was {word}!".center(160) + "\n\n")
        typeWriter("Somebody tried to hide Muddy Shoes in a pile of clothes, I wonder what they're trying to hide?".center(160) + "\n\n")
        typeWriter("Also with this object, you found a piece of paper with code number: 4".center(160) + "\nzn")
        remove()
        input("Continue?".center(160) + "\n".center(160))
        roomMenu(mainMenu)
    else:
        typeWriter(f"Game Over! Try again!".center(160))
        end = input("Play again? y/n".center(160))
        bathroomGame(roomMenu, mainMenu, remove) if end == "y" else roomMenu(mainMenu)

# Extra bathroom game

questions2 = [
    "Water dropping day by day... ",
    "Kill two birds... ",
    "The early bird... ",
    "You can't judge a book... ",
    "Better to ask away... "
]

answers2 =[
    "wears the hardest rock away",
    "with one stone",
    "gets the worm",
    "by its cover",
    "than go astray"]

def bathroomGame2(roomMenu, mainMenu, remove):
    typeWriter(bathroom_message2.center(160) + "\n\n")
    iteration = 0
    input("Continue?".center(160) + "\n".center(160))
    for i in range(len(questions2)):
        os.system("cls||clear")
        while True:
            try:
                answer = answers2[iteration] 
                saying = (input(questions2[iteration].center(160) + "\n\n".center(145)))
                if saying == answer:
                    print("Yes! Next question.\n".center(160))
                    break
                elif saying == "exit":
                    os.system("cls||clear")
                    roomMenu(mainMenu)
                else:
                    print("No, try again or Type 'exit' to leave.".center(160) + "\n")
            except ValueError:
                    print("Provide an answer without full stop".center(160) )
                    print("Continue".center(160))
        iteration = iteration + 1
    typeWriter("Congratulations!, you find piece of wripped up paper with number 0 on it ".center(160))
    remove()
    input()
    roomMenu(mainMenu)

# Bedroom Game

def random_problem():
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "%": operator.mod,
    }


    num_1 = random.randint(10, 30)
    num_2 = random.randint(10, 30)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print("\n" + f"What is {num_1} {operation} {num_2}?".center(160) + "\n")
    return answer


def ask_question():
    answer = random_problem()
    while True:
        try:
            num = int(input("\n".center(150) + "Answer: "))
            break
        except ValueError:
            typeWriter("Only numbers please!".center(160) + "\n\n")
    return num == answer 


def bedroomGame(roomMenu, mainMenu, remove):
    os.system("cls||clear")
    global bedroom_message
    typeWriter(bedroom_message)
    typeWriter("--------------------".center(160) + "\n")
    typeWriter("How well do you know maths?".center(160) + "\n\n".center(160))
    score = 0
    for i in range(5):
        if ask_question() == True:
            score += 1
            os.system("cls||clear")
            typeWriter("\n" + "Correct!".center(160) + "\n")
            typeWriter(f"Your score is {score}".center(160) + "\n\n")
            typeWriter("---------------".center(160))
        else:
            os.system("cls||clear")
            typeWriter("Incorrect!".center(160) + "\n")
            typeWriter(f"Your score is {score}".center(160) + "\n\n")
            print("---------------".center(160))

    if score >= 4:
        typeWriter("\n" + "You've answered enough correctly. CONGRATULATIONS!".center(160) + "\n\n") 
        typeWriter(
            "The code to unlock the wardrobe is: 3275.".center(160) +
            "\n" + "You open it and find that the wardrobe seems empty and looks hastely emptied.".center(160) +
            "\n" + "At the bottom there is a piece of paper with code number: 7".center(160))
        remove()
        input("\n" + "Continue?".center(160) + "\n".center(160))
        roomMenu(mainMenu)
    else:
        typeWriter("\n" + "Try again. You must score 4 points to unlock the code!".center(160))   
        end = input("\n" + "Play again? y/n".center(160) + "\n\n".center(160))
        bedroomGame(roomMenu, mainMenu, remove) if end == "y" else roomMenu(mainMenu)
    
# Garage Game

secret_number = ""
correct_number = 0
perfect_number = 0
guess = 0

def createNumber():
    global secret_number
    for i in range(6):
        number = str(random.randint(0,9))
        secret_number = secret_number + number
    return secret_number


def garageGame(roomMenu, mainMenu, remove):
    typeWriter(garage_message)
    input("Continue?".center(160) + "\n".center(160))
    os.system("cls||clear")
    
    global secret_number, guess
    createNumber()
    while guess != secret_number:
        while True:
                guess = input("Take a guess at the 6 digit Number or type 'exit' to return to Main Menu: ".center(160) + "\n".center(160))   
                if guess == "exit": 
                    roomMenu(mainMenu)
                elif len(guess) == 6 or guess == "exit":
                    break
                else:
                    typeWriter("\n\n" + "Only 6 digits numbers or 'exit'!".center(160) + "\n".center(160))
                    input()
                    os.system("cls||clear")
                typeWriter("Only 6 digits numbers or 'exit'!".center(160) + "\n".center(160))
                input()
                os.system("cls||clear")
        perfect_number = 0
        correct_number = 0

        for num1 ,i in enumerate(secret_number):
            
            for num2, j in enumerate(guess):
                if i == j and num1 == num2:
                        perfect_number = perfect_number + 1

                try:
                    if guess.index(j) < num2:
                        pass
                    else:
                        if i == j and num1 != num2:
                            correct_number = correct_number + 1
                except ValueError:
                    if i == j and num1 != num2:
                            correct_number = correct_number + 1

        if perfect_number == 6:
            typeWriter("No way! you cracked the code and sequenced the genes".center(160) + "\n\n")
            typeWriter2("\033[2;34;40m" + 
                '`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;"`-:-.   ,-;'.center(160) + "\n" +
                " `=`,'=/     `=`,'=/     `=`,'=/     `=`,'=/".center(160) + "\n" +
                "   y==/        y==/        y==/        y==/".center(160) + "\n" +
                "  ,=,-<=`.    ,=,-<=`.    ,=,-<=`.    ,=,-<=`.".center(160) + "\n" +
                ",-'-'   `-=_,-'-'   `-=_,-'-'   `-=_,-'-'   `-=_".center(160) + "\n\n\n" + "\033[2;37;40m")
            remove()
            input("Continue?".center(160) + "\n".center(160))
            typeWriter("Strangely enough it didn't belong to Mr Worth, it belonged to Mr Miller!".center(160) + "\n" +
                "So who was it him in the crashed car".center(160) + "\n\n")
            input("Continue?".center(160) + "\n".center(160))
            roomMenu(mainMenu)
        elif perfect_number == 0 and correct_number == 0:
            typeWriter("No matches, try again".center(160) + "\n\n")
        else:
            typeWriter(f"You had {correct_number} numbers somewhere in the sqeuence and {perfect_number} numbers in the right place".center(160) + "\n\n")

garageGame(1,1,1)