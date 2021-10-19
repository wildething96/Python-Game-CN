#Imports 

import sys, time

# Functions

def isInt(top, bottom = 0):
    while True:
        try:
            num = int(input("Choose a number to investigate: ".center(160) + "\n".center(160)))
            if num < top and num > bottom:
                break
            else:
                typeWriter("\n" + "Please enter only a number from the one's listed above".center(160) + "\n\n")
        except ValueError:
            typeWriter("Only numbers please!".center(160) + "\n\n")
    return num

def typeWriter(line):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            if char == " ":
                time.sleep(0)
            elif char != "\n":
                time.sleep(0.01)
            else:
                time.sleep(0.2)

def typeWriter2(line):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            if char == " ":
                time.sleep(0)
            elif char != "\n":
                time.sleep(0.001)
            else:
                time.sleep(0.0)