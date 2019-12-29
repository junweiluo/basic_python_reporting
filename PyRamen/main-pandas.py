import pandas as pd
from pathlib import Path

# find out current directory
print(f"Current Working Directory: {Path.cwd()}")

# initialize report for reporting
report = {}

# file path
menupath = Path("PyRamen/Resources/menu_data.csv")
salespath = Path("PyRamen/Resources/sales_data.csv")

# import as dataframe
menu = pd.read_csv(menupath)
sales = pd.read_csv(salespath)

# merge 2 dataframe
df = pd.merge(sales, menu, left_on = "Menu_Item", right_on="item", how="inner")

# convert to numeric
df[["Quantity", "price", "cost"]] = df[["Quantity", "price", "cost"]].apply(pd.to_numeric)

# calculate extra column
df["01-count"] = df["Quantity"]
df["02-revenue"] = df["Quantity"] * df["price"]
df["03-cogs"] = df["Quantity"] * df["cost"]
df["04-profits"] = df["02-revenue"] - df["03-cogs"]

# summarize by sales item
df_summary = df.groupby(["item"]).sum()

# select only relevant columns
df_summary2 = df_summary[["01-count","02-revenue","03-cogs","04-profits"]]

# convert dataframe to dict for required reporting
report = df_summary2.to_dict("index")

        #    print(f"{row[4]} does not equal any item on menu! NO MATCH!")   

#output result
output_path = Path("PyRamen/output.txt")

with open(output_path, 'w') as outputfile:
    for k, v in report.items():
        outputfile.write(f"{str(k)} {str(v)}")
        outputfile.write(f"\n")
        
