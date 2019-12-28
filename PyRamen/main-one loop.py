import csv
from pathlib import Path

# find out current directory
print(f"Current Working Directory: {Path.cwd()}")

# file path
menupath = Path("PyRamen/Resources/menu_data.csv")
salespath = Path("PyRamen/Resources/sales_data.csv")

# initialize variables of dicts
menu = {}
report = {}

# open sales and menu data, and put into dicts
with open(menupath, 'r') as menufile:
    menureader = csv.reader(menufile, delimiter=',')
    next(menureader)
    for row in menureader:
        menu[row[0]] = {
            "price": float(row[3]),
            "cost": float(row[4]),
            }

menufile.close()

with open(salespath, 'r') as salesfile:
    salesreader = csv.reader(salesfile, delimiter=',')
    next(salesreader)
    for row in salesreader:

        if row[4] not in report:
            report[row[4]] = {
                "01-count": 0,
                "02-revenue": 0,
                "03-cogs": 0,
                "04-profit": 0,
                }

        try:
            report[row[4]]["02-revenue"] += int(menu[row[4]]["price"]) * int(row[3])
            report[row[4]]["03-cogs"] += int(menu[row[4]]['cost']) * int(row[3])
            report[row[4]]["04-profit"] = report[row[4]]["02-revenue"] - report[row[4]]["03-cogs"]
            report[row[4]]["01-count"] += int(row[3])
        except:
            print(f"{row[4]} does not equal any item on menu! NO MATCH!")   

salesfile.close()

# output result
output_path = Path("PyRamen/output.txt")

with open(output_path, 'w') as outputfile:
    for k, v in report.items():
        outputfile.write(f"{str(k)} {str(v)}")
        outputfile.write(f"\n")
        

outputfile.close()