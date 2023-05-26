#include <stdio.h>
#include "return_string_and_num.h"

//Grabs the user's inputted string and returns it. an alternate methd is included for printing a predetermined string.
void return_string_and_num() {
    char str[100]; //What is the maximum size that we can allow?
    int num = 5;

    //Get user input for string
    printf("Please Enter your String: \n");
    fgets(str, 100, stdin);

    printf("\nYou entered the string: %sThe returned number is: %d  \n", str, num); //Print the string back out to the user.
}