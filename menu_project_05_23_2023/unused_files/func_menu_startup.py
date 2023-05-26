# Menu Project
# Author: Joey Squillaci / Nolan Vrba
#
#

#Creating menu with all possible options
def menu(): 
    
    #User enters one of the digits as input
    print("[1] Option 1")
    print("[2] Option 2")
    print("[9] Exit the Menu")
    option = input("\nEnter Your option: ")
    option = int(option)

    return option

#Define logic that determines function to be ran
def func_logic(option):

    print(type(option))

    #Perform option 1
    if option == 1:
        #func_print()
        print("Selcted option 1\n")

    #Perform option 2
    elif option == 2:
        #func_add()
        print("Selcted option 2\n")

    #Exit
    elif option == 9:
        print("You have exited\n")
        exit = True
        return exit

    #Error handler
    else:
        print("Invalid input! INVALID!\n")