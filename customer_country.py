import csv

custfile = "customers.csv"

infile = open(custfile, "r", newline="")
reader = csv.reader(infile, delimiter=",")
outfile = open("customer_country.csv", "w", newline="")

next(reader)
writer = csv.writer(outfile)

header = ["Customer Name", "Country"]
writer.writerow(header)
i = 0


for row in reader:
    first_name = row[1]
    last_name = row[2]
    country = row[4]

    info = [[first_name + " " + last_name, country]]

    writer.writerows(info)
    i += 1

print(i)
outfile.close()
