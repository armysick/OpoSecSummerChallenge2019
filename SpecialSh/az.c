
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
        if (argc > 4){
                printf("Too many arguments");
        }
        else{
                setuid(0);
                seteuid(0);
                char *env[] = {"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin", "HOME=/root", NULL};
                if (argc < 2){
                        printf("\n\n\n\nIMPORTANT NOTE:: Only valid arguments are: az network * or az vm *\n\n\n");
                        execle("/usr/bin/az", NULL, env);
                }
                else if (strcmp(argv[1],"network") != 0 && strcmp(argv[1], "vm") != 0){
                        printf("\n\n\n\nIMPORTANT NOTE:: Only valid arguments are: az network * or az vm *\n\n\n");
                        execle("/usr/bin/az", NULL, env); 
                }
                else if (argc == 2){
                        if (execle("/usr/bin/az", "/usr/bin/az", argv[1], (char*) NULL, env)) {
                                perror("fuck");
                        }
                }
                else if (argc == 3 && (!strcmp(argv[2], "list") || !strcmp(argv[2], "--help"))){
                        if (execle("/usr/bin/az", "/usr/bin/az", argv[1], argv[2], (char*) NULL, env)) {
                                perror("fuck");
                        }
                }
                else if (argc == 4 && (!strcmp(argv[3], "list") || !strcmp(argv[3], "--help"))){
                        if (execle("/usr/bin/az", "/usr/bin/az", argv[1], argv[2], argv[3], (char*) NULL, env)) {
                                perror("fuck");
                        }
                }
                else{
                        printf("Invalid arguments.\n\n");
                }
        }
}

