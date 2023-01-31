import csv


salesfile = "sales.csv"

infile = open(salesfile, "r", newline="")
reader = csv.reader(infile, delimiter=",")
next(reader)

outfile = open("salesreport.csv", "w", newline="")
writer = csv.writer(outfile, delimiter=" ")
header = ["Customer", "|" "Total"]
writer.writerow(header)


cust_id = 250
subtotal = 0
tax = 0
freight = 0


for row in reader:
    if float(row[0]) == cust_id:
        subtotal += float(row[3])
        tax += float(row[4])
        freight += float(row[5])
    else:
        total = subtotal + tax + freight
        custnum = int(row[0])
        newinfo = [[custnum, total]]
        writer.writerows(newinfo)
        cust_id = int(row[0])
        subtotal = float(row[3])
        tax = float(row[4])
        freight = float(row[5])


outfile.close()
