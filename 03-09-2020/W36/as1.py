#!/usr/bin/env python3.8

from csv import DictReader


total_global_sales = 0
publishers = dict()

# Read the vgsales file
with open("vgsales.csv") as f:
    for row in DictReader(f):
        # Some computation, that include row["Global_Sales"]
        total_global_sales += float(row["Global_Sales"])
        publishers[row["Publisher"]] = publishers.get(row["Publisher"], 0) \
            + float(row["Global_Sales"])
        
        # more aggregation 
        # ...
        
# Read the vgsales file
publishers = dict()
with open("vgsales.csv") as f:
    for row in DictReader(f):
        publishers.setdefault(row["Publisher"], list()).append(float(row["Global_Sales"]))

publishers = { pub: sum(publist) for pub, publist in publishers.items() }
total_global_sales = sum(publishers.values())

# 1.  Find the sum of all global sales (`Global_Sales`)
print(f"The global sales are {total_global_sales:.2f}M")

# 2.  Find all publishers
print(f"The number of publishers are {len(publishers)}")

biggest_gross = 0
best_pub = None
for pub, gross in publishers.items():
    if gross > biggest_gross:
        biggest_gross = gross
        best_pub = pub
    
best_pub, biggest_gross = max(publishers.items(), key=lambda x: x[1])


# 3.  Find the highest grosing publisher
print(f"The highest grossing publisher is {best_pub} with {biggest_gross:.2f}")

# 4.  Do it by year
