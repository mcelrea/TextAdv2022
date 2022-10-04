import os
import time
from colorama import Fore
from colorama import Style
from colorama import Back

#global variables - variables that exist across the entire program
choice = ""
player_state = {"wall" : False,
                "brick" : False,
                "cell open": False,
                "start": True}

inventory = [] #an empty list, a list is a College Board REQUIREMENT
location = "cell"


def clear_screen():
    os.system('clear')

def jail_cell(choice):
    global location
    if (player_state.get("start") == True):
        print(f"{Fore.RED}You awake in a jail cell{Fore.RESET}")
        player_state["start"] = False
    elif(choice == ""):
        print("")
    elif (choice.find("key") >= 0):
        print("You search but find no key")
    elif (choice.find("wall") >= 0):
        print(f"You search the walls and find a loose {Fore.BLUE}brick{Fore.RESET}")
        player_state["wall"] = True
    elif (choice.find("brick") >= 0 and player_state.get("wall") == True):
        print(f"You manage to pull the loose brick from the wall and create a small {Fore.BLUE}hole{Fore.RESET}")
        player_state["brick"] = True
    elif (choice.find("hole") >= 0 and player_state.get("brick") == True):
        print(f"You try to squeeze through he hole in the wall, but it is too small. In the small hole you find a hand-made {Fore.RED}screwdriver{Fore.RESET}")
        inventory.append("screwdriver") #add a screwdriver to player inventory
    elif (searchInventory("screwdriver") and choice.find("screwdriver") >= 0):
        print(f"You open the jail cell door, you can {Fore.BLUE}leave{Fore.RESET} now.")
        player_state["cell open"] = True
    elif (player_state.get("cell open") == True and choice.find("leave") >= 0):
        print("You exit the jail cell")
        location = "hallway"
    else:
        print("Command does not exist")

def hallway(choice):
    global location
    print("You are a hallway surrounded by jail cells.")
    print(f"Darkness looms to your {Fore.BLUE}left{Fore.RESET} and {Fore.BLUE}right{Fore.RESET}")
    if(choice.find("left") >= 0):
        print("You walk to your left")
        location = "locked door"
    elif(choice.find("right") >= 0):
        print("You walk to your right")
        location = "dead end"

def locked_door(choice):
    print("locked door")

def dead_end(choice):
    print("dead end")

def searchInventory(item):
    #go through everything in the inventory
    for temp in inventory:
        if temp == item: #if temp matches item being searching for
            return True #WE FOUND IT!!! return True

    return False #went through the whole list, didn't find it, return false

#start of the program, NO FUNCTION DEFINITION AFTER THIS
while(True):
    if location == "cell":
        jail_cell(choice)
    elif location == "hallway":
        hallway(choice)
    elif location == "locked door":
        locked_door(choice)
    elif location == "dead end":
        dead_end(choice)
    choice = input("Enter command: ")
    choice = choice.lower()
    clear_screen()