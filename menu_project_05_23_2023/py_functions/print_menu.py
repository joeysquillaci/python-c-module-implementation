# Menu Project
# Author: Joey Squillaci / Nolan Vrba
#
#

#Creating menu with all possible options
def func_print_menu(): 
    
    #User enters one of the digits as input
    print("[n] Return number")
    print("[c] Return character")
    print("[s] Return string")
    print("[p] Return a phrase of string & number")
    print("[x] Exit the Menu")
    option = input("\nEnter Your option: ")
    #option = int(option)

    return option