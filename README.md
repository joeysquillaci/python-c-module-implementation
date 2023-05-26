# python-c-module-implementation
This is a frontend program that was developed as a way to communicate through command line/terminal to a battery management system. 
The uploaded content currently includes python files and functions that also use ctypes to import c modules to read sensor data that will be implemented later. 

Setup for this program:
Python version 3.11.3 (32-bit)
MinGW version 6.3.0 (32-bit)

All .so files must be generated via "gcc -shared -o sharedObjectName.so -fPIC cFileName.c" if the c files are updated.
The python script can be ran by opening command line/terminal and running "python -u "main.py" to initiate the menu and select different functions. 
Later, these functions will read sensor values, but for now they just return a number, character, string, or string and a number.
