#!/usr/bin/env python2

import sys
import struct
from datetime import datetime
import base64


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

#printing the timestamp
timestamp, = struct.unpack("<l", data[8:12])
print("TIMESTAMP: %d (%s)" % (timestamp, datetime.fromtimestamp(timestamp)))

#printing the author name
author = struct.unpack("<cccccccc", data[12:20])
print(author)

#Number of sections count
section_count, = struct.unpack("<L", data[20:24])
print("SECTION COUNT: %d" % section_count)

#data length
print("DATA LENGTH : %d" % len(data))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print(" ")
print("-------  BODY  -------")



#methods to help me with the printing of characters of the messages
def print_char(entry, end, encoding):
    char, = entry
    char = char.decode(encoding)
    sys.stdout.write(char)

def print_int(entry, end):
    num, = entry
    sys.stdout.write(num)

def print_me(entry, end):
    print(entry)


# type: (size,format_string,end)
stype_dict = {
    1: (1, "<c", print_char, {'end': "", 'encoding' : 'ascii'}),
    2: (1, "<c", print_char, {'end': "", 'encoding' : 'utf-8'}),
    3: (4, "<L", print_int, {'end': ""}),
    4: (8, "<q", print_me , {'end': ""}),
    5: (8, "<d", print_int, {'end' : ""}),
    6: (16, "<dd", print_me , {'end': ""}),
    7: (4, "<L", print_int, {'end': ""})
}

offset = 24

section_count = 0

while (offset < len(data)):

    section_count += 1

    type_s, len_s = struct.unpack_from("<LL", data, offset)
    
    print(" ")
    print("SECTION TYPE: %d" % type_s)
    print("SECTION LENGTH: %d" % len_s)

    offset += 8
    start_offset = offset

    if (type_s in stype_dict):

        if (len_s == 80):
            decoded_string = base64.b64decode(data[offset:offset+len_s])
            print("The decoded String is -----> %s" %decoded_string)

        elif (len_s == 44):
             print("Reversed String, Another flag found:---> %s" %data[offset:offset+len_s][::-1])

        (size,format_string,out_fun,args) = stype_dict[type_s]

        for index in range(0, int(len_s / size)):

            entry = struct.unpack_from(format_string, data, offset)
            offset += size
            out_fun(entry, **args)
        


        print(" ")
        
    if (offset != start_offset + len_s):
        print("ENTRY SKIPPED")
        offset = start_offset + len_s

    

print(" ")
print("-------  BODY  -------")

print("NUMBER OF SECTIONS %d" % section_count)