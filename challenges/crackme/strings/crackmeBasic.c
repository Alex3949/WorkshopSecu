#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char**argv){
    if(argc != 2){
        printf("Veillez fournir un mot de passe.\n");
        printf("Exemple d'utilisation: %s password\n", argv[0]);
    }
    else{
        if(!strcmp(argv[1], "D4T_P455w0rD!")){
            printf("Félicitation, utilisez ce mot de passe pour valider le challenge.\n");
        }
        else{
            printf("Dommage, ce n'est pas le bon mot de passe.\n");
        }
    }
    return EXIT_SUCCESS;
}
