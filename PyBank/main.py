import csv
from pathlib import Path

print(f"Current Working Directory: {Path.cwd()}")

csvpath = Path("Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv")

count_months = 0
total_profit_loss = 0
last_month_profit_loss = 0
profit_loss = 0
change = 0
max_change = 0
max_change_date = []
min_change = 0
min_change_date = []
total_change = 0

with open(csvpath, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    next(csvreader)
    for row in csvreader:
        profit_loss = int(row[1])
        count_months += 1
        total_profit_loss += int(row[1])

        if last_month_profit_loss == 0:
            last_month_profit_loss = profit_loss

        change = profit_loss - last_month_profit_loss
        total_change += change
        if change > max_change:
            max_change = change
            max_change_date = row[0]
        if change < min_change:
            min_change = change
            min_change_date = row[0]
        last_month_profit_loss = profit_loss

print(f"financial analysis")
print(f"--------------------")
print(f"Total Months:  {count_months}")
print(f"Total:   ${total_profit_loss}")
print(f"Average change:  ${round(total_change/(count_months-1))}")
print(f"The greatest increase in profits over the entire period: {max_change_date} (${max_change})")
print(f"The greatest decrease in profits over the entire period: {min_change_date} (${min_change})")