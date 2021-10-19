import os
from useful_functions import typeWriter, typeWriter2, isInt
from mini_games import kitchenGame, bathroomGame, bathroomGame2, bedroomGame, garageGame

worth_num = 0

dinning_room = {
    "Check out locked safe" : "safe",
}

kitchen = {
    "Check out Glass of wine" : "A single glass of wine appears to have been left on the table with a wet ring on the table next to it",
    "Knife stand looks empty" : "2 knives appear to be missing, though their is no washing up on the side",
    "The Extractor fan looks a little loose" : "game1",
    "Check out pack of tablets on the side" : "Prescription for heavy sleeping"
}

bathroom = {
    "Sleeping Pill" : "More Sleeping pills in the medicine cabinet",
    "Investigate the dirty sink" : "game2",
    "Search room for another code number" : "game5",
}

bedroom = {
    "Check out Mr Worth's laptop" : "laptop",
    "Investiagte a hidden item under the bed": "You find a hidden knife, maybe Mrs worth knows why thats there".center(160) + "\n\n\n" +
    "\033[2;31;40m                ______________________________ ______________________".center(160) + "\n" +
    "     .'                              | (_)     (_)    (_)   \\".center(160) + "\n" +
    "   .'                                |  __________________   }".center(160) + "\n" +
    ".'_.............................____|_(                  )_/".center(160) + "\n\n" + "\033[2;37;40m",

    "Locked Wardbrobe, maybe I can figure out the code" : "game3",
    "Look in the desk" : "You mr Worths will, odd that his wife isn't on it",
}

garage = {
    "Investigate weird mark on the wall" : "game4",
    "Footprint" : "Muddy footprint leading toward the Bathroom",
    "Investiagte the mess" : "It appears messy like there was a struggle here",
}

room_description = {
    "Dinning Room" : "",
    "Kitchen" : "",
    "Bathroom" : "",
    "Bedroom" : "",
    "Garage" : ""
}

rooms = {
    "Dinning Room" : dinning_room,
    "Kitchen" : kitchen,
    "Bathroom" : bathroom,
    "Bedroom" : bedroom,
    "Garage" : garage
}

room_names = []
room_clues = []
room_selection = 0
last_room = 0
last_option = 0
only_once = 0
garage_unlocked = False

def roomMenu(mainMenu):
    global room_selection, only_once, last_room, garage_unlocked
    os.system("cls||clear")
    typeWriter("Room Menu".center(160) + "\n\n\n")

    for num, room in enumerate (rooms, start = 1):
            typeWriter2((str(num) + ". " + str(room)).center(160) + "\n\n")
            last_room = num
            if only_once == 0:
                room_names.append(room)
    
    only_once = 1

    typeWriter2((str(last_room + 1) + ". Go back to Main Menu").center(160) + "\n\n")

    room_selection = isInt(last_room + 2, 0)
    if last_room + 1 == room_selection: mainMenu()
    os.system("cls||clear")
    
    if room_selection == 5 and garage_unlocked == False:
        typeWriter("The garage is currently locked. Maybe you can find away to unlock it?".center(160) + "\n\n")
        input("Continue?".center(160) + "\n".center(160))
        os.system("cls||clear")
        roomMenu(mainMenu)

    last_room = 0
    clueMenu(mainMenu)

def clueMenu(mainMenu):
    global room_selection, last_option, worth_num, garage_unlocked
    room_clues.clear()
    last_option = 0

    typeWriter(f"Choose a clue in the {room_names[room_selection - 1]} to investiagte".center(160) + "\n\n\n")

    for num , clue in enumerate (rooms[room_names[room_selection - 1]].keys(), start = 1 ):
        typeWriter2((str(num) + ". " + clue).center(160) + "\n\n")
        room_clues.append(clue)
        last_option = num

    typeWriter2((str(last_option + 1) + ". Go back").center(160) + "\n\n")
    clue_selection = isInt(last_option + 2, 0) 
    os.system("cls||clear")

    if last_option + 1 == clue_selection: roomMenu(mainMenu)

    dic = rooms[room_names[room_selection - 1]]
    dic_item = room_clues[clue_selection - 1]

    def remove():
        dic.pop(dic_item)
        room_clues.pop(clue_selection - 1)

    if dic.get(dic_item) == "game1":
        kitchenGame(roomMenu, mainMenu, remove)

    elif dic.get(dic_item) == "game2":
        bathroomGame(roomMenu, mainMenu, remove)

    elif dic.get(dic_item) == "game3":
        bedroomGame(roomMenu, mainMenu, remove)

    elif dic.get(dic_item) == "game4":
        garageGame(roomMenu, mainMenu, remove)
    
    elif dic.get(dic_item) == "game5":
        bathroomGame2(roomMenu, mainMenu, remove)

    elif dic.get(dic_item) == "safe":
        os.system("cls||clear")
        typeWriter("You check out the safe to find that of course it's locked, maybe you can find a code for it somewhere?".center(160) + "\n\n")
        
        while True:
            code = input("Try a code or type 'exit' to leave:".center(160) + "\n".center(154))
            if code == "407":
                    os.system("cls||clear")
                    typeWriter("You unlock the safe and find the spare keys to the garage!".center(160) + "\n\n\n")
                    typeWriter2("\033[2;32;40m" +
                        "  ooo,    .--.".center(141) + "\n" +
                        "o`  o   /    |\________________".center(160) + "\n" +
                        "o`   'oooo()  | ________   _   _)".center(160) + "\n" +
                        "`oo   o` \    |/        | | | |".center(158) + "\n" + 
                        ("  `ooo'   `--'          "+'"-" |_|)').center(158) + "\n\n\n" + "\033[2;37;40m")
                    garage_unlocked = True
                    
                    dic.pop(dic_item)
                    room_clues.pop(clue_selection - 1)
                    
                    input("Continue?".center(160) + "\n".center(160))
                    os.system("cls||clear")
                    clueMenu(mainMenu)
            elif code == "exit":
                os.system("cls||clear")
                clueMenu(mainMenu) 
            else:
                typeWriter("\n" + "Incorrect! try again or try and find a password from somewhere".center(160) + "\n\n")
                input("Continue?".center(160) + "\n".center(160))

    elif dic.get(dic_item) == "laptop":
        os.system("cls||clear")
        typeWriter("You open the laptop to find it's locked".center(160) + "\n\n")
    
        while True:
            code = input("Please enter your password or type 'exit' to leave:".center(160) + "\n".center(154))
            if code == "471107":
                os.system("cls||clear")
                typeWriter(
                    "You unlock the computer to find plane tickets for Mr Worth and Mrs Miller".center(160) + "\n" +
                    "That's weird could they of had a love interest I wonder?".center(160) + "\n\n")
                dic.pop(dic_item)
                room_clues.pop(clue_selection - 1)
                input("Continue?".center(160) + "\n".center(160))
                os.system("cls||clear")
                clueMenu(mainMenu)
            elif code == "exit":
                clueMenu(mainMenu) 
            else:
                typeWriter("\n" + "Incorrect! try again or try and find a password from somewhere".center(160) + "\n\n")
                input("Continue?".center(160) + "\n".center(160))
    typeWriter(dic.get(dic_item).center(160) + "\n\n")         
    input("Continue?".center(160) + "\n".center(160))
    os.system("cls||clear")
    remove()
    clueMenu(mainMenu)