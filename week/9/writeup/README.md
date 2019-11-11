# Writeup 9 - Forensics II

Name: *Moses Kamoga*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Moses Kamoga*


## Assignment details

### Part 1 (45 Pts)
1. 142.93.136.81
   Using wireshark and analysizing the communication between networks.
   I realized that this IP sent the SYN-ACK to the attacking IP. 
   Meaning that the IP was vulnerable. and to complete the communication.
   We observe that the attacking IP sent an ACK to the attacked IP above.

2. nmap
   From wireshark, we observe that the attacking IP is sending SYNs to multiple ports at the attacked 
   IP address. 
   Thus, the tool that does this is a nmap which is used to send various SYNs to ports
   until a vulnerable port is found.

3. 159.203.113.181
   This is the IP address observed to be sending out various SYNs. 
   Hence meaning, it is the attacking IP address. 

4. 21
   We can observer that this port sent back a SYN + ACK.
   Which means a channel of communication was established when 
   the attacking IP address sent an ACK.

5. findme,
   it is a jpeg.
   The file is a picture.

6. greetz.fpff

7. You can run a Nmap on your system and find out which ports are open.
   When you find these ports, you can determine if they need to be patched or not
   depending on what inofrmation one can access by attacking those ports.

   Also using a firewall, you can turn a hackers couple of minutes work into a 
   7 hour work by redirecting their port scans. 

### Part 2 (55 Pts)

i.    TIMESTAMP: 1553660105 (2019-03-27 00:15:05)

ii.   Fl1nch

iii.  SECTION TYPE: 1
      SECTION LENGTH: 24
      Hey you, keep looking :) 
 
      SECTION TYPE: 6
      SECTION LENGTH: 16
      (52.336035, 4.880673)
 
 
      SECTION TYPE: 8
      SECTION LENGTH: 202776
      ENTRY SKIPPED
 
      SECTION TYPE: 1
      SECTION LENGTH: 44
      Reversed String, Another flag found:---> CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}
      }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC 
 
      SECTION TYPE: 1
      SECTION LENGTH: 80
      The decoded String is -----> CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}
      Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30= 
 


iv.   CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}

      CMSC389R-{hey_h3y_y0U_you_I_dont_like_your_base64_encoding}



