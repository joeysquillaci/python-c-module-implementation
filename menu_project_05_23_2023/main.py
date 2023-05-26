# Menu Project
# Author: Joey Squillaci / Nolan Vrba
#

#importing external .py files and their functions
import ctypes
from py_functions.print_menu import *
from py_functions.menu_sel import *

#Initialize option variable

def main():
    option = func_print_menu()

    while option != "x":
            func_logic(option)
            option = func_print_menu()
    
    print("You have exited")
main()