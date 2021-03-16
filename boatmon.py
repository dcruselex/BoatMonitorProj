import sys
import os
import re
import random
import time
import glob
from termcolor import colored, cprint


def printHeader():
    print()
    #cprint("██████╗  █████╗  █████╗ ████████╗      ███╗   ███╗ █████╗ ███╗  ██╗██╗████████╗ █████╗ ██████╗ ", "green")
    #cprint("██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝      ████╗ ████║██╔══██╗████╗ ██║██║╚══██╔══╝██╔══██╗██╔══██╗", "green")
    #cprint("██████╦╝██║  ██║███████║   ██║   █████╗██╔████╔██║██║  ██║██╔██╗██║██║   ██║   ██║  ██║██████╔╝", "green")
    #cprint("██╔══██╗██║  ██║██╔══██║   ██║   ╚════╝██║╚██╔╝██║██║  ██║██║╚████║██║   ██║   ██║  ██║██╔══██╗", "green")
    #cprint("██████╦╝╚█████╔╝██║  ██║   ██║         ██║ ╚═╝ ██║╚█████╔╝██║ ╚███║██║   ██║   ╚█████╔╝██║  ██║", "green")
    #cprint("╚═════╝  ╚════╝ ╚═╝  ╚═╝   ╚═╝         ╚═╝     ╚═╝ ╚════╝ ╚═╝  ╚══╝╚═╝   ╚═╝    ╚════╝ ╚═╝  ╚═╝", "green")

def getPower():
    r = random.randint(0,9)  # returns 0.0 - 0.999
    print (r)
    if r < 2:
        return "OFF"
    else:
        return "ON"

# TODO create getVoltage(), getWater() pattern after getPower. use random numbers to decide state. return text

def prompt():
    green = "green"
    print("({})uit, ({})can ({})eboot .".format(colored("Q", green), colored("S", green), colored("R", green)))


#-----------------------main--------------------------
os.system('color') # needed for termcolor to work on Windows
printHeader()
quitnow = False

while True:
    prompt()
    k = input()
    if k == "q" or k == "Q":  # ESC or Q pressed
        cprint("Bye!", "red")
        quit()
    
    elif k == "S" or k == "s":  # SPACE bar pressed, capture two images regular/mirror
        cprint("Scanning...", "white")
        cprint("Power:{}   Voltage:{}   Water:{}".format(getPower(), getPower(), getPower()), "green")

    elif k=="R" or k == "r": # carriage return. Next class
        cprint("Rebooting system...", "red")
        for i in range(10): 
            time.sleep(0.2)
            print('.', end='', flush=True)
        print()
        
