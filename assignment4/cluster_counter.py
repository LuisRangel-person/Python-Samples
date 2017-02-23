#Luis Rangel(luisrngl5@gmail.com & LuisRangel@gmail.com)
#CSCE 4430
#Homework 3-Part 2
#Parse a file and return the list of groups and the number of clusters those groups have

import sys

def Snake(lis, c, r, x, y, num, bol):#Snake function will search out clusters
    matching = bol
    if x > 0 and x <= c and y > 0 and y <= r + 1:#Making sure it stays in range
        for a in range(x - 1, x + 1):#Go though the neighbors
            for b in range(y - 1, y + 1):
                if lis[a][b] == 'O':#If the neighbor equals the char given
                    matching = True
                    lis[a][b] = 'X'
                    num = Snake(lis, c, r, a, b, num, bol)#RECURSION
                else:
                    if matching == True:
                        num = num + 1
                        matching = False
    return num

matrix = [] #setting up a matrix
clone = [] #This is to hold a copy of the matrix
crow = []#Clone row
row = [] #this reps the rows in the matrix
m = 0 #number of columns
n = 0 # number of rows
temp = 0 #tempoary
groups = [] #list of groups
print 'Number of arguments:', len(sys.argv), 'arguments.' #Here for learning purposes
print 'Argument List:', str(sys.argv)
if(len(sys.argv) > 1):#Making sure the proper number of arguments exist
    filename = sys.argv[1]#Gets filename from argv[1]
    print sys.argv[1]#Prints out the file name in order to make sure it's right!
    txt = open(filename)#Opens the file provided by argv[1]
    dev = txt.read()#Gets the number of occurances in the file
    print dev
    dev.upper()#So casing doesn't matter
    for i in range(0,len(dev)):#Reading in the matrix
        if dev[i] != '\n' and dev[i] != " " and dev != '\r':
            temp = temp + 1 #Add 1 to m
        if dev[i] == '\r':#Getting number of columns
            m = temp - 1#setting number of columns
            n = n + 1#settinbg number of rows
            temp = 0#reset temp variable
        if dev[i] != " " and dev[i] != '\r' and dev[i] != '\n':#Making sure only characters we want are placed in the matrix
            row.append(dev[i]) #add i to a row
        if len(row) == m:#If the row is the length of a matrix row
            matrix.append(list(row))#Add row to Matrix
            row = []#Empty out the row
    print matrix
    for i in range(0, n):#Go though every row
        for j in range(0, len(matrix[i])):#For the length of the row
            if groups.count(matrix[i][j]) == 0:#If it isn't already in the group list
                groups.append(matrix[i][j])#Add it to the group list
    for k in range(0, len(groups)):#Go though group list to get clusters
        num = 0
        fail = 0
        temp = k#Getting the cluster number
        for i in range(0, n):#Go though every row
            for j in range(0, len(matrix[i])):#For the length of the row
                if(matrix[i][j] == groups[k]):
                    crow.append('O') #add i to a row
                else:
                    crow.append('X')
                if len(crow) == m:#If the row is the length of a matrix row
                    clone.append(list(crow))#Add row to Matrix
                    crow = []#Empty out the row
        for i in range(0, n):#Go though every row
            for j in range(0, m):#For the length of the row
                num = Snake(clone, m, n, i, j, num, False)#Call Snake
        temp = 0
        clone = []
        print "Number of Clusters of ", groups[k], " is" , num, "\n\n"
    print m ,"x", n#Printing out matrix demensions
    print "These Groups Exist " , groups#Printing put the groups in the matrix
else:
    print "\n***ERROR: Bad command!!***"
