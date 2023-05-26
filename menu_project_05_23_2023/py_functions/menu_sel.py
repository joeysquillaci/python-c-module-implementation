# Menu Project
# Author: Joey Squillaci / Nolan Vrba
#
#

#Importing specific external functions to be used here
import ctypes

#Define logic that determines function to be ran
def func_logic(option):

    #Perform option 1: NUMBER return
    if option == "n":
        print("*****Return NUMBER selected***** \n")
        #Call ctypes RETURN NUMBER
        shared_object = ctypes.WinDLL("M:/Engineering/Shared/Interns/menu_project/c_h_so_files/return_num/return_num.so")
        shared_object.return_num(5);

    #Perform option 2: CHARACTER return
    elif option == "c":
        print("*****Return CHARACTER selected***** \n")
        #Call ctypes RETURN CHARACTER
        shared_object = ctypes.WinDLL("M:/Engineering/Shared/Interns/menu_project/c_h_so_files/return_char/return_char.so")
        shared_object.return_char(97);

    #Perform option 3: STRING return
    elif option == "s":
        print("*****Return STRING selected***** \n")
        #Call ctypes RETURN STRING
        shared_object = ctypes.WinDLL("M:/Engineering/Shared/Interns/menu_project/c_h_so_files/return_string/return_string.so")
        shared_object.return_string();

    #Perform option 4: STRING AND NUMBER
    elif option == "p":
        print("*****Return STRING AND NUMBER selected***** \n")
        #Call ctypes RETURN STRING AND NUMBER
        shared_object = ctypes.WinDLL("M:/Engineering/Shared/Interns/menu_project/c_h_so_files/return_string_and_num/return_string_and_num.so")
        shared_object.return_string_and_num();

    #Exit
    elif option == "x":
        print("You have exited. \n")
        return "x"

    #Error handler
    else:
        print("Invalid input! INVALID!\n")

    #Print newline
    print("\n")