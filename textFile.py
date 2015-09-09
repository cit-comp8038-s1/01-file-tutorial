__author__ = 'larkin cunningham'

infile = open("Data.txt", 'r')
employees = [line.rstrip() for line in infile]
infile.close()

for employee in employees:
    employeeDetails = employee.split(';')
    print("The employee named {0:s} earns {1:.2f} per annum.".format(employeeDetails[0], float(employeeDetails[1])))