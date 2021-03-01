import sys
import os
import re
import random
import glob
from termcolor import colored, cprint

def printHeader():
    print()
    cprint("██████╗░░█████╗░░█████╗░████████╗░░░░░░███╗░░░███╗░█████╗░███╗░░██╗██╗████████╗░█████╗░██████╗░", "green")
    cprint("██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝░░░░░░████╗░████║██╔══██╗████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗", "green")
    cprint("██████╦╝██║░░██║███████║░░░██║░░░█████╗██╔████╔██║██║░░██║██╔██╗██║██║░░░██║░░░██║░░██║██████╔╝", "green")
    cprint("██╔══██╗██║░░██║██╔══██║░░░██║░░░╚════╝██║╚██╔╝██║██║░░██║██║╚████║██║░░░██║░░░██║░░██║██╔══██╗", "green")
    cprint("██████╦╝╚█████╔╝██║░░██║░░░██║░░░░░░░░░██║░╚═╝░██║╚█████╔╝██║░╚███║██║░░░██║░░░╚█████╔╝██║░░██║", "green")
    cprint("╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░░░░╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝", "green")


def prompt():
    global gest, img_counter
    green = "green"
    print("({})uit, ({})ext ({}) .".format(colored("Q", green), colored("N", green), colored("SPACE", green)))

        
#-----------------------main--------------------------
os.system('color') # needed for termcolor to work on Windows
printHeader()
quitnow = False
prompt()
while True:
    prompt()
    k = input()
    if k == 27 or k == ord("q") or k == ord("Q"):  # ESC or Q pressed
        cprint("Escape/Quit. Closing...", "red")
        break
    
    elif k == 32:  # SPACE bar pressed, capture two images regular/mirror
        cprint("Spacebar...", "red")

        
    elif k==13 or k== ord("N") or k =
    
    = ord("n"): # carriage return. Next class
        cprint("Next", "orange")
