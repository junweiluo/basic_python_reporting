import csv
from pathlib import Path
import collections

# find out current directory
print(f"Current Working Directory: {Path.cwd()}")

# file path
menupath = Path("PyRamen/Resources/menu_data.csv")
salespath = Path("PyRamen/Resources/sales_data.csv")

# initialize variables of dicts
menu = {}
sales = {}
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
        sales[row[0]] = {
            "Quantity": int(row[3]),
            "Menu_item": row[4],
            }

        if row[4] not in report:
            report[row[4]] = {
                "01-count": 0,
                "02-revenue": 0,
                "03-cogs": 0,
                "04-profit": 0,
                }

salesfile.close()

# nested loop through sales and menu to find match, and then accumulate metrics
for sales_item in sales.values():
    match = 0
    for item_on_menu, price_cost in menu.items():
        if  sales_item["Menu_item"] == item_on_menu:
            report[sales_item["Menu_item"]]["01-count"] += sales_item["Quantity"]
            report[sales_item["Menu_item"]]["02-revenue"] += price_cost["price"] * sales_item["Quantity"]
            report[sales_item["Menu_item"]]["03-cogs"] += price_cost['cost'] * sales_item["Quantity"]
            report[sales_item["Menu_item"]]["04-profit"] = report[sales_item["Menu_item"]]["02-revenue"] - report[sales_item["Menu_item"]]["03-cogs"]
            match = 1
    if match == 0:
        print(f"{sales_item} does not equal any item on menu! NO MATCH!")   # There is some confusion on the instruction file.

# output result
output_path = Path("PyRamen/output.txt")

# Open the output_path as a file object in "write" mode ('w')
# Write a header line and write the contents of 'text' to the file
with open(output_path, 'w') as outputfile:
    for k, v in report.items():
        outputfile.write(f"{str(k)} {str(v)}")
        outputfile.write(f"\n")
        

outputfile.close()