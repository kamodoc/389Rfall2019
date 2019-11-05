# Writeup 8 - Binaries II

Name: *Moses Kamoga*
Section: *114320667*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Moses Kamoga*

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?
   The password is on the stack and a string from stdin, is cyphered by adding 13 to the individual characters in the string.
   We can access the memory address on the stack where the password is. And retrieve the generated password.
   the weakness is that we can use string specifiers to move the pointer to the next address, with the printf that does ot have a specifier. This will print the string at the location.
   Hence, using a stack and is very velnerable. 

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.
   line 46 -- printf 
   The attacker can fool the print statement to print an address or a variety of addresses by passing in a string with various spring format specifers like %d, %f etc.
   To prevent this, we need to specify the string format as part of the program not as an input. 

   Also you can use format guards to guard such vulnerabilities in your program.

   line 68 ---  storing a string in a buffer.
   a buffer overflow may happen since we have a buffer of 32 bytes. This is also a vulnerability that may be exploited. 
   The input that is stored in the buffer from the stdin can be larger than the size of the buffer and thus lead to th eoverflow of the buffer and comprising the system.
   Before storing the values in the buffer, there should be a check to ensure that the sixe of the input is not greater than the buffer size. 

3. What is the flag?
   CMSC389R-{expl017-2-w1n}

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.
   The printf statement in the code is vulnerable to a %s,%f etc. Knowing this, i used "%29$f", after trying with a lot of values, to pad the stdin where i was prompted to enter the message to cypher.
   I was able to print out the password of the server having exploited the stack by shifting the pointer to the memory address where the password was located. 
   I authenticated the password to be able to access other features on the server.
   like 4 which is executing the command.
   At this point, i looked at the source code and realized in the method of 'void exec_command(void)' that the input from the stdin is stored in the buffer of 32 bits and thus randomly putting in diffrent characters over 32 bits. I overflowed the buffer and the message that was printed on the stdout gave me an idea of what was going on behind the scenes. 
   That meant that, i was comparing the buffer with the commands and my input had overwritten the memory of the commands. Thus the comprison with the strcasestr
   was done with my input and so, i put in the same information repeatedly and thus got the desired effect in the if block, but could not execute the command. Because of the various other characters that i used to overflow the buffer. 
   After alot of playing around, i realised that i had to pad the bits with white space characters. 
   So, my first input was 'ls' with white space characters that is --> 'ls                                ls                                ls                   '. I overflowed the buffer and the commands which was 62 bits.
   I was able to execute this and saw the files and there included a flag file.
   My next command i executed was a 'cat flag' with white space characters padded in my input-- 3 times that is --> ' cat flag                         cat flag                         cat flag   ' .
   This gave me the flag. 
