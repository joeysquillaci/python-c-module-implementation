#include <stdio.h>
#include <string.h>
#include "return_string.h"

//Grabs the user's inputted string and returns it. an alternate methd is included for printing a predetermined string.
void return_string() {
    char str[100]; //What is the maximum size that we can allow?

    printf("Please Enter your String: \n");
    //scanf("%s", str);//stores the user entry into the char array
    fgets(str, 100, stdin);

    printf("\nYou Entered the string: %s", str); //Print the string back out to the user.

    /* ALTERNATE METHOD: for loop, print out each char at a time. can be used if we wish to print some predetermined strings.
    int i = 0;
    for (i = 0; str[i] != '\0'; c++)
        printf("%c", s[i]);
    */
}