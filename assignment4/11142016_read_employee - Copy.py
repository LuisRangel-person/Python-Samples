import csv
import sys


class Employee:

    def __init__(self, filename=".\employee.csv"):
        # Filename
        self.filename = filename
        # Data from the csv
        self.data = [x for x in csv.reader(open(filename))]

    def get_all_employee_names_by_last_name(self, reverse=False):
        return sorted(map(lambda x: x[0], self.data[2:]), reverse=reverse, key=lambda x: x.split()[1])



def main():
    empl = Employee()
    print empl.get_all_employee_names_by_last_name()

if __name__ == "__main__":
    main()
