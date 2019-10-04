# Writeup 2 - Pentesting

Name: *Moses Kamoga*
Section: *114320667*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Moses Kamoga*

## Assignment Writeup

### Part 1 (45 pts)

* step 1: i ran the comand nc wattsamp.net 1337 on the terminal  
  step 2: I was prompted to enter the IP address of the web i am trying to access. 
  step 3: I decided to run the command '157.230.179.99 && ls -la' in the place where it says Enter Ip address,
          to find out how many directories that the web service is running on
  step 4: Then after looking at the directories, i decide to check each directory for a file that may possibly contain a flag.
          running '157.230.179.99 & cd <directory name> && ls' on the terminal in the place where it says Enter Ip address
  step 5: I found the file that comntains the flag running '157.230.179.99 & cd home && ls' on the terminal
  step 6: I opened the file to view the flag running the command '157.230.179.99 & cd home && cat flag.txt' in the place of Enter Ip Address

          Good! Here's your flag: CMSC389R-{p1ng_as_a_$erv1c3} 

       Eric Norman should never call out to OS commands from application layout code inorder to protect himself from this vulnerability.
   If Eric Norman feels it is unavoidable to call out to OS comands with user supplied input, then he must enforce strong input validation:-
   Validating against a whitelist of permitted values.
   Validating that the input is a number.
   Validating that the input contains only alphanumeric characters, no other syntax or whitespace.
*




### Part 2 (55 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*
 
 * On the terminal, the user has to specify whether they prefer to enter a shell, download a file using pull and view the help menu with the instructions. 
   If the user enters a command that is not supported, the help menu will be displayed. 
   When the user enters 'shell' into the prompted space, he will be redirected to an interective shell.
   I did this by making a connection to the server and breaking into it. 
   To break into the sever, i sent a charcter A with a semicolon (A;). The purpose of this was to disable the pings by giving them a wrong input and also break into the server 
   by using the semicolon. 
   Now, having access to the server with my new interactive shell, i can view the directories that the server runs on by running an 'ls' command,
   that is executed by "execute_cmd". The server sends data back to me the data that is receieved back from the server is printed on the screen.
   Within here, we can issue commands to change the directory. 
   Every command that is executed, as long as it is supported by the shell. I make the connection to the server and execute it in my mini shell.
   The pull command is utilised in the way that i write the contents of the file from the server on to the buffer and then write the contents to the local file on my machine. 
*