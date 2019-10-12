# Writeup 6 - Binaries I

Name: *Moses Kamoga*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Moses Kamoga*

## Assignment Writeup

### Part 1 (50 pts)

*CMSC389R-{di5a55_0r_d13}*

### Part 2 (50 pts)

*I ran the ./ crackme and the program printed out, "did you even try disassembling?". I followed the code and realised that the comparison function is executing the false branch.
The cmp function is comparing argc and 1. Meaning that the number of arguments should be equal to 1. I knew along with ./ crackme, i had to add one argument. I submitted ./crackme 1, the stdout was "multi-word arguments can be quoted ;). I realised that the check1 function was not executing in the right way and thus the cmp function was always false. The check1 function had a string "Oh God" and also called a strcmp, if everything checked out, 0 was stored in an eax register. Back to main, This eax registed is compared to 0 and if its true then it will successful execute this block of code. So, i ran ./crackme "Oh God", stdout printed "I wish you cared more about the environment", the comparison with a 32 bit number was failing. So, i checked check2 function. Immediately, i noticed the getenv and FOOBAR. 
From this, i knew that something had to with the enviroment and the string "seye my ". On further inspection, i realised that the string "seye my " was being reversed and i was able to decode it as a " my eyes" string. Since the getenv is after FOOBAR in the code, I figured that the progam is trying to change to the environment FOOBAR and this enviroment contains " my eyes".
I created the enviroment FOOBAR and putting " my eyes" in the environment. I then ran the ./crackme "Oh God", stdout printed out, open sesame. I decided to investigate check3. Since the program was failing around that. I immediately noticed an open, which meant a file was being opened and that file name is sesame, and there is memset and read. Information from the file was being read into the program. Meaning that i had to have a file called sesame in the same environmet. My next mission was to figure out what information should be contained in the file. I realised there is a loop iterating over characters and checking them if they are are equal. I realised that this was checking the contents of the file and so i translated the hexadecimal values that the were being compared. Translating them i generated a word " theyburn". So, i created a file sesame and input the contents they burn. At first, it failed and printed out "hard-coded string comaprison". I played around with the string. Finally getting the " they burn" string.  I finally ran ./crackme "Oh God" and got the flag  CMSC389R-{di5a55_0r_d13}*