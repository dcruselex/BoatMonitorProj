import sys
import os
import re
import random
import time
import glob
from termcolor import colored, cprint
import datetime
import TempSensor

def ftoc(fahrenheit):
    celsius = ( fahrenheit- 32) * 5.0/9.0
    return celsius  # fahrenheit to Celsius conversion


def printHeader():
    print()
    cprint("██████╗  █████╗  █████╗ ████████╗      ███╗   ███╗ █████╗ ███╗  ██╗██╗████████╗ █████╗ ██████╗ ", "green")
    cprint("██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝      ████╗ ████║██╔══██╗████╗ ██║██║╚══██╔══╝██╔══██╗██╔══██╗", "green")
    cprint("██████╦╝██║  ██║███████║   ██║   █████╗██╔████╔██║██║  ██║██╔██╗██║██║   ██║   ██║  ██║██████╔╝", "green")
    cprint("██╔══██╗██║  ██║██╔══██║   ██║   ╚════╝██║╚██╔╝██║██║  ██║██║╚████║██║   ██║   ██║  ██║██╔══██╗", "green")
    cprint("██████╦╝╚█████╔╝██║  ██║   ██║         ██║ ╚═╝ ██║╚█████╔╝██║ ╚███║██║   ██║   ╚█████╔╝██║  ██║", "green")
    cprint("╚═════╝  ╚════╝ ╚═╝  ╚═╝   ╚═╝         ╚═╝     ╚═╝ ╚════╝ ╚═╝  ╚══╝╚═╝   ╚═╝    ╚════╝ ╚═╝  ╚═╝", "green")

def getPower():
    r = random.randint(0,9)  # returns 0.0 - 0.999
    #print (r)
    if r < 2:
        return "OFF"
    else:
        return "ON"

def getWater():
    r = random.randint(0,9)  # returns 0.0 - 0.999
    #print (r)
    if r < 4:
        return "LOW"
    else:
        return "HIGH"

def getVoltage():
    r = random.randint(0,9)  # returns 0.0 - 0.999
    #print (r)
    if r < 3:
        return "12V"
    else:
        return "10V"


# TODO create getVoltage(), getWater() pattern after getPower. use random numbers to decide state. return text

def prompt():
    green = "green"
    print("({})uit, ({})can ({})eboot ({})ode .".format(colored("Q", green), colored("S", green), colored("R", green), colored("M", green)))

def printdate():
    now = datetime.datetime.now()
    return (str(now)) 



#-----------------------main--------------------------
mode="e"  # e for english, m for metric
#os.system('color') # needed for termcolor to work on Windows
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
        ts = TempSensor.TempSensor()
        temp = ts.getTemp (mode)
        cprint("{} Power:{}   Voltage:{}   Water:{} Temp:{}".format (printdate(), getPower(), getVoltage(), getWater(), temp), "green")

    elif k=="R" or k == "r": # carriage return. Next class
        cprint("Rebooting system...", "red")
        for i in range(10): 
            time.sleep(0.2)
            print('.', end='', flush=True)
        print()
    
    elif k=="M" or k == "m": # switch modes english to metric
        if mode=="e":
            mode="m"
            print("mode:", "Metric")
        else:
            mode="e"
            print("mode:", "English")
        

    elif k=="F" or k == "c": # switch modes fahrenheit to celsius
        if mode=="f":
             mode="c"
        else:
            mode="f"
        print("mode:", mode)

