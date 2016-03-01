#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int main(int argc, char**argv){
    char password[] = "\x87\xcf\x8d\xa0\x9c\xcb\xb1\xa0\x9d\x9a\xa0\xb1\xce\x9c\xcc\xc4\xd6";

    if(argc != 2){
        printf("Veillez fournir un mot de passe.\n");
        printf("Exemple d'utilisation: %s password\n", argv[0]);
    }
    else{
        char *guess = argv[1];
        for(int i=0; guess[i] !='\0'; i++){
            guess[i] ^= 255;
        }
        if(!strcmp(guess, password)){
            printf("Félicitation, utilisez ce mot de passe pour valider le challenge.\n");
        }
        else{
            printf("Dommage, ce n'est pas le bon mot de passe.\n");
        }
    }
    return EXIT_SUCCESS;
}
