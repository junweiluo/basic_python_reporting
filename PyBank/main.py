import csv
from pathlib import Path

# find out current directory
print(f"Current Working Directory: {Path.cwd()}")

# file path
csvpath = Path("Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv")

# initialize variables
count_months = 0
total_profit_loss = 0
last_month_profit_loss = 0
profit_loss = 0
change = 0
max_change = 0                                # assuming there is positive change
max_change_date = []
min_change = 0                                # assuming there is negative change
min_change_date = []
total_change = 0

# open csv
with open(csvpath, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    next(csvreader)                            # skip first row - header

    for row in csvreader:
        profit_loss = int(row[1])              # current month p/l
        count_months += 1                      # count months
        total_profit_loss += int(row[1])       # accumulate p/l

        if last_month_profit_loss == 0:        # assume no change for first month
            last_month_profit_loss = profit_loss

        change = profit_loss - last_month_profit_loss  # calculate change from last month
        total_change += change                 # accumulate changes
        if change > max_change:                # record max change and month, assuming there is + change.
            max_change = change
            max_change_date = row[0]
        if change < min_change:                # record min change and month, assuming there is - change.
            min_change = change
            min_change_date = row[0]
        last_month_profit_loss = profit_loss   # assign p/l to last_month variable for next loop
file.close()                                   # close csv file

print(f"financial analysis")
print(f"--------------------")
print(f"Total Months:  {count_months}")
print(f"Total:   ${total_profit_loss}")
print(f"Average change:  ${round(total_change/(count_months-1))}")  # should take out the first month with no change
print(f"The greatest increase in profits over the entire period: {max_change_date} (${max_change})")
print(f"The greatest decrease in profits over the entire period: {min_change_date} (${min_change})")