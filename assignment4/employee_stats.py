#Luis Rangel(luisrngl5@gmail.com & LuisRangel@gmail.com)
#CSCE 4430
#Homework 3-Part 3
#Parse a file and parse employee info

import sys
import csv

print 'Number of arguments:', len(sys.argv), 'arguments.' #Here for learning purposes
print 'Argument List:', str(sys.argv)
if(len(sys.argv) > 2):#Making sure the proper number of arguments exist
    filename = sys.argv[1]#Gets filename from argv[1]
    print sys.argv[1]#Prints out the file name in order to make sure it's right!
    txt = open(filename)#Opens the file provided by argv[1]
else:
    print "\n***ERROR: Bad command!!***"

class Employee:

    def __init__(self, filename="employee.csv"):
        # Filename
        self.filename = filename
        # Data from the csv
        self.data = [x for x in csv.reader(open(filename))]

    def get_all_employee_names_by_last_name(self, reverse=False):
        hold = []
        sorted(map(lambda x: x[0], self.data[2:]), reverse=reverse, key=lambda x: x.split()[1])
        for i in range(2,len(self.data)):#Go though all the employees
            hold.append(self.data[i][0].split()[1])#Puts all the last names in a list
        hold.sort()
        for i in range(2, len(hold)):
            print hold[i]

    def getEmployeeAvg(self):#This will get the employees avarage wages
        for i in range(2,len(self.data)):#Go though all the employees
            #Getting the total worked hours over the five weeks
            sum = int(self.data[i][4]) + int(self.data[i][5]) + int(self.data[i][6]) + int(self.data[i][7]) + int(self.data[i][8])
            wage = sum * float(self.data[i][3])#Getting the total wages
            avg = wage / 5#Gets the average wage over the five weeks
            print self.data[i][0], "\t\tAverage:$", avg #Printing out the names

    def getHighestEarners(self):#This will get the highest earners from each classification
        e = 0.0;#setting up the varaibles
        m = 0.0;
        s = 0.0;
        HighEntry = ""
        HighMiddle = ""
        HighSenior = ""
        for i in range(2,len(self.data)):#Go though all the employees
            #Getting the total worked hours over the five weeks
            sum = int(self.data[i][4]) + int(self.data[i][5]) + int(self.data[i][6]) + int(self.data[i][7]) + int(self.data[i][8])
            wage = sum * float(self.data[i][3])#Getting the total wages, don't need to get the average this time
            if self.data[i][1] == "Entry Level":#Entry Level Employees
                if wage > e:#Higher than current maximum
                    e = wage#Record Wage
                    HighEntry = self.data[i][0]#Record Employee Name
            if self.data[i][1] == "Middle Level":#Entry Level Employees
                if wage > m:#Higher than current maximum
                    m = wage#Record Wage
                    HighMiddle = self.data[i][0]#Record Employee Name
            if self.data[i][1] == "Senior Level":#Entry Level Employees
                if wage > s:#Higher than current maximum
                    s = wage#Record Wage
                    HighSenior = self.data[i][0]#Record Employee Name
        print "The Highest Earning Entry Level Employee is", HighEntry, " earning $", e#Out of loop print results
        print "The Highest Earning Middle Level Employee is", HighMiddle, " earning $", m
        print "The Highest Earning Senior Level Employee is", HighSenior, " earning $", s

def main():
    empl = Employee()
    if sys.argv[2] == '1':#First Choice
        empl.get_all_employee_names_by_last_name()
    if sys.argv[2] == '2':#Second Choice
        empl.getEmployeeAvg()#Getting Average Employee Wages
    if sys.argv[2] == '3':#Third Choice
        empl.getHighestEarners()#Getting the highest earners
    if sys.argv[2] != '1' and sys.argv[2] != '2' and sys.argv[2] != '3':#Error Handling
        print "***ERROR: Number Not Vaild!!!***"
if __name__ == "__main__":
    main()
