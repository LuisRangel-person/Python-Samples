#Luis Rangel(luisrngl5@gmail.com & LuisRangel@gmail.com)
#CSCE 4430
#Homework 3-Part 1
#Parse a file and return the number of occurances of argv[2] in argv[1]

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.' #Here for learning purposes
print 'Argument List:', str(sys.argv)
if(len(sys.argv) > 2):#Making sure the proper number of arguments exist
    filename = sys.argv[1]#Gets filename from argv[1]
    print sys.argv[1]#Prints out the file name in order to make sure it's right!
    txt = open(filename)#Opens the file provided by argv[1]
    dev = txt.read()#Gets the number of occurances in the file
    print dev.count(sys.argv[2])#Prints out the number of occurances in the file
else:
    print "\n***ERROR: Bad command!!***"
