import csv
import os
import sys

custfile = "customers.csv"

infile = open(custfile, "r", newline="")

reader = csv.reader(infile)


for row in reader:
    i = 0
    first_name = row[1]
    last_name = row[2]
    country = row[4]
    i += 1

    print(format(first_name, "<14"), format(last_name, "<16"), format(country, "<14"))
