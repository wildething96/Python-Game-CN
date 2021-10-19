
def main():
    # Imports

    import time, os
    from threading import Thread
    from story import story, tutorialMenu, startInvestigation
    from useful_functions import typeWriter2

    
    # Variables 

    animation = ["       ","R       ","Ri     ","Rin    ","Ring   ","Ring.  ","Ring.. ","Ring..."]
    threadRunning = True

    animation2 = [
        "Death at Manor Ho se","Death at Manor House", "Deah at Manor House", "death at Manor House",
        "Death at Man r House", "Death at Manor House", "Death at Manor Ho se", "Death at Manor House"]
    threadRunning2 = True

    # Functions
    def ringFunction():
        idx = 0
        while threadRunning:
            print(animation[idx % len(animation)].center(160), end="\r")
            idx += 1
            time.sleep(0.12)


    def endRingFunction():
        input("Hit enter to answer the phone: ".center(160) + "\n".center(160))


    def titleFunction():
        idx = 0
        while threadRunning2:
            print(animation2[idx % len(animation2)].center(160), end="\r")
            idx += 1
            time.sleep(0.12)


    def endTitleFunction():
        input("Ready to play".center(160) + "\n\n\n")


    # Main Game
    os.system("cls||clear")
    t3 = Thread(target=titleFunction)
    t4 = Thread(target=endTitleFunction)

    t3.start()
    t4.start()
    
    t4.join()
    threadRunning2 = False

    os.system("cls||clear")
    story(4)
    typeWriter2("\033[2;33;40m"  +
    '''                                                                   _.-="_-         _
                                                               _.-="   _-          | ||"""""""---._______     __..
                                                   ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
                                            __.--""     __        ,'                   o \           __        [__|
                                       __-""=======.--""  ""--.=================================.--""  ""--.=======:
                                      ]       [w] : /        \ : |========================|    : /        \ :  [w] :
                                      V___________:|          |: |========================|    :|          |:   _-"
                                       V__________: \        / :_|=======================/_____: \        / :__-"
                                       -----------'  "-____-"  `-------------------------------'  "-____-"'''.center(160) + "\n\n\n" + "\033[2;37;40m"+ "\n\n\n\n\n\n")
    
    input("Continue?".center(160) + "\n".center(160))
    os.system("cls||clear")

    story(5)
    input("Continue?".center(160) + "\n".center(160))
    os.system("cls||clear")

    story(7)
    input("Continue?".center(160) + "\n".center(160))
    os.system("cls||clear")

    tutorialMenu()

    story()
    t1 = Thread(target=ringFunction)
    t2 = Thread(target=endRingFunction)

    t2.start()
    t1.start()

    t2.join()
    threadRunning = False
    os.system("cls||clear")

    story(3)
    startInvestigation()

main()