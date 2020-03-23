#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
        if (argc != 3 || strlen(argv[1])+strlen(argv[2]) > 100){
                printf("Invalid Arguments\nUse tcpdump <host> <dst_port>\n");
        }
        else{
                setuid(0);
                seteuid(0);
                char arguments[1000] = "host ";
                strcat(arguments, argv[1]);
                strcat(arguments, " and dst port ");
                strcat(arguments, argv[2]);
                char args2[1000] = "-x";
                printf("%s\n", arguments);
                if (execl("/usr/sbin/tcpdump", "/usr/sbin/tcpdump", arguments, args2, (char*) NULL)) {
                        perror("fuck");
                }
        }
}
