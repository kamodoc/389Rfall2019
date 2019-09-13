# Writeup 2 - OSINT

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (45 pts)

*Please use this space to writeup your answers and solutions (and how you found them!) for part 1.*

1) Eric Norman
2) Wattsamp
   http://wattsamp.net
3) Histagram @EricNorman84 - to find this, i used OSINT framework and searched under "instant   
   username search"
   
   Twitter @EricNorman84 - to find this, i went on the website of his work listed on his histagram. Under wattsamp news i found a link to the UMD Cybersecurity twitter account. 
   i scratched through people following the account the account and thats where i found Eric Norman accounnt.

   The information below found it using whois wattsamp.net on kali 
   phone number - + 1 202 656 2837
   email - ejnorman84@gmail.com
   address - 1300 Adabel Dr
             EL paso, Texas 79835


4) I found the ip addresses from https://ipinfo.info/html/ip_checker.php
   157.230.179.99 for wattsamp.net
   
   I discovered the servers from the whois wattsamp.net on kali terminal
   216.239.32.109 for NS-CLOUD-D1.GOOGLEDOMAINS.COM
   216.239.34.109 for NS-CLOUD-D2.GOOGLEDOMAINS.COM
   216.239.36.109 for NS-CLOUD-D3.GOOGLEDOMAINS.COM
   216.239.38.109 for NS-CLOUD-D4.GOOGLEDOMAINS.COM

5) hidden directory 
   /assets/

6) Ports open on the website - I discovered the ports using nmap and putting in the IP address of the wattsamp.net
   Discovered open port 22/tcp on 157.230.179.99
   Discovered open port 80/tcp on 157.230.179.99
   Discovered open port 1337

7)Server: Apache/2.4.29 (Ubuntu)
  I discovered the operating using the terminal and i put in this command below
  curl -s -I wattsamp.net | grep Server


8) I did find the hidden flag using http://wattsamp.net/robots.txt
   User-agent: *
   Good for you! Bonus: *CMSC389R-{n0_indexing_pls}
   .
### Part 2 (75 pts)
*I used the username of ejnorman84 with access to the server through the IP and an open port. 
In kali i had access to the wordlist that i unzipped to extract the file of rockyou.txt.
I created a shared file folder between the guest and the host machine to access the list then ran through the whole list to find the password.
I ran the password against against the server and got in. I accessed the file of flag.txt and the contents are below.
Good! Here's your flag: CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}*
