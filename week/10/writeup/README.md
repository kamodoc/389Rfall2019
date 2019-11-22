# Writeup 10 - Crypto I

Name: *Moses Kamoga*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Moses Kamoga*


## Assignment details

### Part 1 (45 Pts)
1) The structure of the ledger format consists of the keyhash, ciphertext hash, ciphertext,
   innitialization vector.
   The byte offsets are 16 bytes each of the above mentioned. The length of the cipher text is 
   the size of the file, removing the 48bytes.

2) The program uses md5hash and aes128. 
   With hashing that is (md5hash) you can not decrypt a hash, but collisions are invevitable with a bounded hash space.
   md5 is very prune to brutal attacks.

   Aes128 is reversible with knowledge of the key. An attacker can attack and crack the md5 gettting to the key 
   and eventually getting to the key that can reverse aes128. 

3) It is a bunch of characters that currently do not make sense to me. 
   I can see some hexadecimal numbers and some weird characters.

4) The application ensure confidentiality by encrypting the message. 
   The encryption key is derived using aes128 and md5hash. 

5) The application ensures integrity by checking if the ciphertext hash from the file and the actual hash are the same.
 

6) The application checks for authenticity by checking if the key hash inside the file is equal to the hash provided by the key.

7) The initialization vector is generated randomly. Hence ensuring no re-use of the initialization vector. 

### Part 2 (45 Pts)

In my crack.c file, i generate a password randomly using rand. 
The (rand()%26) + 'a' . This generates random characters from a to z.
That are in the readable form for the c program.

I use the verify function to check if the generated password is equal to the first 16 bytes of the ledger.
By hashing the first 2 bytes of the generated password and then checking for equality.

In the main, as soon as the result is verified in the verify function.
The original generated string is printed out and excuted with the ./ledger './crack' to decrypt the ledger.
And eventually got this frag.
 
CMSC389R - {k3y5p4c3_2_sm411}


### Part 3 (10 Pts)
Security through obscurity is not a good measure to ensure security. Just by hiding your scheme does not guarantee security.
As in class we learnt about social enginneering, where someone can trick you into giving them information voluntarily.
So, obscurity is not really safe. 
I am not saying obscurity is all bad news. We can use obscurity but also ensure that if an attacker figures out our scheme.
We are not vulnerable. The system is secure. 
Having access to a ledger's source does not certainly make it easier to attack. Because, no security expert will expose
their ledger file and make it easy to be attacked. This is not entirely true and fully embodies kerckchoff's principle. 
A cryptosystem is secure even if everything is public knowledge except the sensitive info like the key.
