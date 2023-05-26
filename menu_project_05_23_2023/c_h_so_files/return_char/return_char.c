#include <stdio.h>
#include "return_char.h"

//takes an integer (within the ASCII range) and returns its respective char.
char return_char(int tmp) {
    printf("Your returned character is: %c", tmp);
    //char character = (char) tmp;
    return ((char) tmp);
}