#include <stdio.h>

int main(int argc, char **argv) {
    char c;
    int head;
    FILE *ifi, *ofo;

    if(argc < 3){
        ifi = stdin;
        ofo = stdout;
    } else {
        ifi = fopen(argv[1], "r");
        ofo = fopen(argv[2], "r");
    }
    
    while((c = getc(ifi))){
        if(head){

        } else {

        }
    }
}