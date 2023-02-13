import csv


infile = csv.reader(open("sales.csv", "r", newline=""))
next(infile)
outfile = open("salesreport.csv", "w")


cust_id = "250"
customer_total = 0

outfile.write("Customer  |  Total\n")  # writes the new header

for row in infile:
    if cust_id != row[0]:
        outfile.write(cust_id + "\t" + str(customer_total) + "\n")

        cust_id = row[0]
        customer_total = 0

    total = float(row[3]) + float(row[4]) + float(row[5])
    customer_total += total  # this is a running total

outfile.write(
    cust_id + "\t" + str(customer_total + "\n")
)  # this is how to actual info is being written to the csv


outfile.close()
