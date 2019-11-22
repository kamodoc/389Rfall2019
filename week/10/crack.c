#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>

#include "crypto.h"

#define SIZE 16
#define FILE_LEDGER "ledger.bin"
#define PERMISSIONS (S_IRUSR | S_IWUSR)

struct cipher_params param;

char* verify(unsigned char input[16],unsigned char keyBin[16]);

int main(int argc, char **argv) {
    int fd;
    fd = open(FILE_LEDGER, O_RDONLY,PERMISSIONS);
    unsigned char fd_key_hash1[16];
    read(fd, fd_key_hash1,16);
    
    unsigned char generateBuffer[SIZE+1];
    memset(generateBuffer, 0, SIZE+1);
    char* result;
     srand(time(NULL));
    
  do{
     
       for(int i = 0; i < SIZE; i++){
                                     
         // generateBuffer[i] = (rand()%127)+1;
          generateBuffer[i] = (rand() %26) + 'a';
       }
       result = verify(generateBuffer,fd_key_hash1);

   }while(strcmp(result, "no success") == 0);

    printf("%s\n", generateBuffer);

    close(fd);

    return 0;
}

char* verify(unsigned char input[16], unsigned char keyBin[16]) {
   unsigned char *hash1;
   unsigned char *hash2;
   
   hash1 = md5_hash(input,16);
   memset(hash1+2, 0, 14);
   hash2 = md5_hash(hash1, 2);
   memcpy(param.key_hash, hash2, 16);
   free(hash2);
   //printf("generatedpassword-->%s",param.key_hash);
   //printf("real password ----> %s",keyBin);
   if(memcmp(param.key_hash,keyBin, 16) == 0){
     return param.key_hash;
   } 
  return "no success";
}
