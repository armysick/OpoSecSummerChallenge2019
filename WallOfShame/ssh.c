#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


int isSub(char* a1, int size1, char* a2, int size2){
   int sub_counter = 0;
   for(int i = 0; i < size1; i++){
      if(a1[i] == a2[sub_counter]){
         sub_counter++;
         if(sub_counter == size2){
            return 1;
         }
      }
      else{
         sub_counter = 0;
      }
   }
   return 0;
}

int main(int argc, char *argv[]){
   int a1 = 948723981;
   int a2 = 3982;
   int a5 = 108974;
   int thereis = 0;
   int a3 = a2 * a5;
   for (int i = 1; i < argc; i++){
      if(isSub(argv[i], argc, "-p", 2)){
          thereis = 1;
      }
   }
   int a4 = a3 + a1;
   if(!thereis){
      char pwd[60];
      printf("Password: ");
      fgets(pwd, 60, stdin);
      if(strcmp("bDMzdHIwMHQK\n", pwd) == 0){
          printf("You have been busted by the Blue team! #wall_of_shame . Go and search elsewhere for the flag!");
          char final[10000];
          char* user = getlogin();
          char res[10];
          snprintf(res, 10, "%d", a4);
          char* arg = "-d \"";
          strcat(final, arg);
          strcat(final,user);
          strcat(final,res);

          execl("/usr/bin/curl", "/usr/bin/curl", final, "http://localhost:8123", (char*) NULL);
          return 0;
      }
      printf("Access Denied.\n");
      return 0;
   }
   execv("/usr/bin/ssh", argv);
}

