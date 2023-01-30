import csv
import os
import sys

empfile = "EmployeePay.csv"

infile = open(empfile, "r", newline="")

reader = csv.reader(infile)


for row in reader:
    i = 0
    emp_id = row[0]
    fname = row[1]
    lname = row[2]
    salary = row[3]
    bonus = row[4]

    print(
        format(emp_id, "10"),
        format(fname, "<14"),
        format(lname, "<18"),
        format(salary, "<10"),
        format(bonus, "<10"),
    )
